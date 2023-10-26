import os
import lzma
import asyncio

import pandas as pd
from pandas import DataFrame
from typing import List
from functools import wraps

from kuroco_api import KurocoAPI, KurocoContent

from .kuroco_retriever import KurocoRetriever

QUERY_KW: str = "vector_search"
VECTOR_KW: str = "vector"

SIZE_VECTOR_KW: str = "size_vector"
DOCUMENT_KW: str = "document"

EMBEDDING_COLUMN_VECTORS: str = "EMBEDDING_COLUMN_VECTORS"

COLUMN_NAME_FOR_TOPICS_ID: str = "topics_id"
SCORE_DISTANCE_COLUMN_NAME: str = "vector_distance"

def check_params_types(types: dict):
    """
    Decorator that checks the types of the parameters of the decorated function

    Parameters:
    types (dict): The types of the parameters to check, keys are the names of the parameters and values are the types

    Returns:
    None

    Raises:
    AssertionError: If the types of the parameters are not correct
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            assert 'params' in kwargs, "Params argument not found"
            params = kwargs['params']
            assert isinstance(params, dict), "Params must be a dict"
            for key, value in types.items():
                assert key in params, f"Key {key} not found in params"
                assert isinstance(params[key], value), f"Key {key} must be of type {value}"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def prepare_request(path: str, params: dict, limit: int = 10) -> dict:
    """
    Prepare the request to be sent to the Kuroco API

    Parameters:
    path (str): The path to the Kuroco API
    params (dict): The parameters to be sent with the get request, must contain the vector
    limit (int): The maximum number of entries to return, 0 for all

    Returns:
    tuple: The request to be sent to the Kuroco API and its parameters (path, params)
    """
    assert isinstance(params, dict), "Params must be a dict"
    assert VECTOR_KW in params or QUERY_KW in params or DOCUMENT_KW in params, "Vector or raw Query or Document must be provided in params"
    assert isinstance(limit, int), "Limit must be an integer"
    data = {}
    if VECTOR_KW in params:
        query_path: str = os.path.join(path)
        params.pop(QUERY_KW, None)
        data[VECTOR_KW] = compress_vector(params[VECTOR_KW])
    elif QUERY_KW in params:
        query_path: str = os.path.join(path)
        params.pop(VECTOR_KW, None)
    elif DOCUMENT_KW in params:
        query_path: str = os.path.join(path, DOCUMENT_KW)
        params.pop(VECTOR_KW, None)
        params.pop(QUERY_KW, None)
        data[DOCUMENT_KW] = params.pop(DOCUMENT_KW)

    if limit > 0:
        params = {} if params is None else params
        params["limit"] = limit

    return {"url": query_path, "params": params, "data": data}

@check_params_types({ "filter": dict | None})
async def send_queries(paths: list | tuple, kuroco_handler: KurocoAPI, params: dict, limit: int = 10, threshold: float = 0.0) -> list:
    """
    Send multiple queries to the Kuroco API for embedding

    Parameters:
    paths (list | tuple): The paths to the Kuroco API
    kuroco_handler (KurocoAPI): The KurocoAPI object used for Kuroco API requests
    params (dict): The parameters to be sent with the get request
    limit (int): The maximum number of entries to return, 0 for all

    Returns:
    DataFrame: A dataframe of embedded entries similar to the query in multiple queries specified in paths
    """
    values = DataFrame(pd.concat(await asyncio.gather(*[send_query(path, kuroco_handler, params, limit) for path in paths]))).sort_values(SCORE_DISTANCE_COLUMN_NAME, ascending=True)
    # Deal with limit of multiple calls (limit only managed on server side for one call)
    if limit > 0 and len(values) > limit:
        values = values.drop(values.index[limit:])
    return values if threshold <= 0.0 else values[values[SCORE_DISTANCE_COLUMN_NAME] <= threshold]

async def send_query(path: str, kuroco_handler: KurocoAPI, params: dict, limit: int = 10) -> list:
    """
    Send a query to the Kuroco API for embedding

    Parameters:
    path (str): The path to the Kuroco API
    kuroco_handler (KurocoAPI): The KurocoAPI object used for Kuroco API requests
    params (dict): The parameters to be sent with the get request
    limit (int): The maximum number of entries to return, 0 for all

    Returns:
    list: A list of embedded entries similar to the query

    Note:
    This method is asynchronous. 
    """
    query = prepare_request(path=path, params=params, limit=limit)
    query.pop("data", None)
    _, resp = await kuroco_handler.get(**query)
    return convert_respond_to_dataframe(resp['list'])


# Decorator to check that topics_ids is a list of integers with minimum length
def check_topics_ids(min_length: int = 1):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            topics_ids = kwargs.get("topics_ids", [])
            assert isinstance(topics_ids, list), "Topics_ids must be a list"
            assert len(topics_ids) >= min_length, f"Topics_ids must be a list of integers with minimum length {min_length}"
            assert all(isinstance(x, int) for x in topics_ids), "Topics_ids must be a list of integers"
            return await func(*args, **kwargs)
        return wrapper
    return decorator

def compress_vector(vector: List[float]) -> bytes:
    """
    Compress a vector using lzma

    Parameters:
    vector (list): The vector to compress

    Returns:
    bytes: The compressed vector
    """
    return lzma.compress(vector.tobytes())

def convert_respond_to_dataframe(respond: dict) -> DataFrame:
    """
    Convert the respond from the Kuroco API to a dataframe

    Parameters:
    respond (dict): The respond from the Kuroco API

    Returns:
    dataframe: The dataframe of the respond
    """
    return DataFrame(respond).set_index(COLUMN_NAME_FOR_TOPICS_ID)


class KurocoEmbedding:
    """
    A class used to represent a KurocoEmbedding object

    Attributes:
    _kuroco_handler (KurocoAPI): The KurocoAPI object used for Kuroco API requests
    _content (KurocoContent): The KurocoContent object used for embedding requests

    Examples:
    >>> # Embedding Instantiated on a single endpoint

    >>> k_emb = KurocoEmbedding(content="test", kuroco_handler= KurocoAPI())

    >>> k_emb.similarity_search("test query")
    """
    _kuroco_embedding_endpoint: str = "embedding"
    _kuroco_handler: KurocoAPI = None
    _content: KurocoContent = None

    _column_vector: str = None
    _size_vector: int = None
    _column_vector: str = "vector"

    def __init__(self, 
                content: KurocoContent | tuple | list | None = None,
                kuroco_handler: KurocoAPI | str | None = None,
                column_vector: list | str = "vector-1586",
                config_path: str | None = None) -> None:  
        assert column_vector or config_path, "Either column_vector or config_path must be provided"
        if isinstance(content, KurocoAPI):
            kuroco_handler = content
            content = None
        elif isinstance(kuroco_handler, str):
            assert os.path.exists(kuroco_handler), "Kuroco API config file not found"
            kuroco_handler = KurocoAPI.load_from_file(path=kuroco_handler)
        if isinstance(content, str | list | tuple):
            if isinstance(content, str):
                content = (content,)
            assert len(set(content)) == len(content), "Content must be a list of unique strings"
            content = [KurocoContent(x, x, kuroco_handler) for x in content]
        self._content = content
        if config_path and not column_vector:
            with open(config_path, "r") as f:
                config_path = f.read()
            self.column_vector = config_path[EMBEDDING_COLUMN_VECTORS]
        else:
            self.column_vector = column_vector
        self.kuroco_handler = self.content.kuroco_handler if kuroco_handler is None else kuroco_handler

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        assert isinstance(value, KurocoContent | None), "Content must be a KurocoContent object"
        self._content = value

    @property
    def column_vector(self):
        return self._column_vector
    
    @column_vector.setter
    def column_vector(self, value):
        assert isinstance(value, str), "Column vector must be a string"
        self._column_vector = value

    @property
    def kuroco_handler(self):
        return self._kuroco_handler
    
    @kuroco_handler.setter
    def kuroco_handler(self, value):
        assert isinstance(value, KurocoAPI), "Kuroco handler must be a KurocoAPI object"
        self._kuroco_handler = value

    @property
    def size_vector(self):
        if self._size_vector is None:
            self.get_size_table_vector()
        return self._size_vector

    @size_vector.setter
    def size_vector(self, value):
        assert isinstance(value, int), "Size vector must be an integer"
        self._size_vector = value

    def get_size_table_vector(self) -> int:
        """
        Get the size of the table vector by sending a request to the Kuroco API

        Parameters:
        None

        Returns:
        int: The size of the table vector
        """
        assert self._content is not None, "KurocoContent must be set before getting the size of the category vector"
        url = self.build_api_path()
        response = self._kuroco_handler.get_sync(url)
        self.size_vector = response.json()[SIZE_VECTOR_KW]
        return self._size_vector

    @property
    def paths(self):
        return (content.path for content in self.content)

    def build_api_path(self) -> dict:
        """
        Build the API request to be sent to the Kuroco API

        Parameters:
        None

        Returns:
        dict: The API request to be sent to the Kuroco API
        """
        return self.paths
    
    # Methods for indirect query search
    async def similarity_search(self, query: str, limit: int = 10, filter: str = None, with_score: bool = False, threshold: float = 0.0) -> DataFrame:
        """
        Search for similar entries to a query

        Parameters:
        query (str): The query to search for similar entries to
        limit (int): The maximum number of entries to return, 0 for all
        filter (str): The filter to apply to the query
        with_score (bool): Whether to return the similarity score or not
        threshold (float): The similarity threshold to apply to the query

        Returns:
        dataframe: A dataframe of similar entries to the query, with their similarity score as last column if needed and limited to limit passed as parameter and by respecting the threshold provided

        Note:
        This method is asynchronous.
        """
        values = await self.similarity_search_by_query(query=query, limit=limit, filter=filter, threshold=threshold) if not with_score else await self.similarity_search_by_query_with_score(query=query, limit=limit, filter=filter, threshold=threshold)
        return values


    async def similarity_search_by_query(self, query: str, limit: int = 10, filter: str = None, threshold: float = 0.0) -> DataFrame:
        """
        Search for similar entries to a query

        Parameters:
        query (str): The query to search for similar entries to
        limit (int): The maximum number of entries to return, 0 for all
        filter (str): The filter to apply to the query
        threshold (float): The similarity threshold to apply to the query

        Returns:
        dataframe: A dataframe of similar entries to the query

        Note:
        This method is asynchronous.
        """
        # Cleaning the chain of characters
        query = query.strip().encode('utf-8', 'ignore').decode('utf-8')
        params = { QUERY_KW: query, "filter": filter }
        return (await send_queries(paths=self.paths, 
                                   kuroco_handler=self.kuroco_handler, 
                                   params=params, 
                                   limit=limit, 
                                   threshold=threshold)).drop(columns=[SCORE_DISTANCE_COLUMN_NAME], errors='ignore')

    async def similarity_search_by_query_with_score(self, query: str, limit: int = 10, filter: str = None, threshold: float = 0.0) -> DataFrame:
        """
        Search for similar entries to a query and return the similarity score

        Parameters:
        query (str): The query to search for similar entries to
        limit (int): The maximum number of entries to return, 0 for all
        filter (str): The filter to apply to the query
        threshold (float): The similarity threshold to apply to the query

        Returns:
        dataframe: A dataframe of similar entries to the query with their similarity score for last column

        Note:
        This method is asynchronous.
        """
        params = { QUERY_KW: query, "filter": filter }
        return await send_queries(paths=self.paths, 
                                  kuroco_handler=self.kuroco_handler,
                                  params=params, 
                                  limit=limit, 
                                  threshold=threshold)

    async def similarity_search_with_score(self, query: str, limit: int = 10, threshold: float = 0.0) -> DataFrame:
        """
        Search for similar entries to a query and return the similarity score

        Parameters:
        query (str): The query to search for similar entries to
        limit (int): The maximum number of entries to return, 0 for all

        Returns:
        dataframe: A dataframe of similar entries to the query with their similarity score for last column 
        
        Note:
        This method is asynchronous. Use similarity_search_with_score_sync for a synchronous version
        """
        return await self.similarity_search_by_query_with_score(query, limit, threshold)

    async def similarity_search_by_document(self, document: list, limit: int = 10) -> DataFrame:
        """
        Search for similar entries to a document

        Parameters:
        document (list): The document to search for similar entries to
        limit (int): The maximum number of entries to return, 0 for all

        Returns:
        dataframe: A dataframe of similar entries to the document

        Note:
        This method is asynchronous.
        """
        params = { DOCUMENT_KW: document }
        return self.send_query(limit=limit, params=params)

    async def document_similarity_search(self, document: list, limit: int = 10) -> DataFrame:
        """
        Search for similar entries to a document

        Parameters:
        document (list): The document to search for similar entries to
        limit (int): The maximum number of entries to return, 0 for all

        Returns:
        dataframe: A dataframe of similar entries to the document

        Note:
        This method is asynchronous. Use document_similarity_search_sync for a synchronous version
        """
        return await self.similarity_search_by_document(document, limit)

    # Methods for direct vector search
    def prepare_similarity_search_by_vector(self, vector: List[float], params: dict = None) -> dict:
        """
        Prepare the request to be sent to the Kuroco API

        Parameters:
        vector (list): The vector to search for similar entries to (must be a list of floats)
        params (dict): The parameters to be sent with the get request

        Returns:
        dict: The request parameters to be sent to the Kuroco API
        """
        assert isinstance(vector, list) and len(vector) > 0 and len(vector) == self.size_vector, f"Vector must be an none empty list, equals to the size of the table vector (here: {self.size_vector})"
        assert all(isinstance(x, float) for x in vector), "Vector must be a list of floats"
        assert params is None or isinstance(params, dict), "Params must be a dict or not provided"

        params = {} if params is None else params
        params[VECTOR_KW] = vector
        return params

    async def similarity_search_by_vector(self, vector: List[float] , limit: int) -> DataFrame:
        """
        Search for similar documents to a vector

        Parameters:
        vector (list): The vector to search for similar documents to (must be a list of floats)
        limit (int): The maximum number of documents to return, 0 for all

        Returns:
        dataframe: A dataframe of similar entries to the vector

        Note:
        This method is asynchronous.
        """
        return await self.send_query(limit=limit, params=self.prepare_similarity_search_by_vector(vector))

    async def similarity_search_by_vector_with_score(self, vector: List[float], limit: int, threshold: float = 0.0) -> DataFrame:
        """
        Search for similar documents to a vector and return the similarity score

        Parameters:
        vector (list): The vector to search for similar documents to (must be a list of floats)
        limit (int): The maximum number of documents to return, 0 for all

        Returns:
        dataframe: A dataframe of similar entries to the vector with their similarity score as last column

        Note:
        This method is asynchronous.
        """
        return await self.send_query(limit=limit, params=KurocoVectorStore.prepare_similarity_search_by_vector(vector, { "score": True }))

    @check_topics_ids()
    async def get_vectors(self, topics_ids: list = []) -> List[float]:
        """
        Get the vector of an entry

        Parameters:
        topics_ids (list): The topics_ids of topics to return the vector from

        Returns:
        list: The vector of the entry

        Note:
        This method is asynchronous.
        """
        url = os.path.join(self.build_api_path(), VECTOR_KW)
        response = await self._kuroco_handler.get(url, { "topics_ids": topics_ids })
        return lzma.decompress(response.json()[VECTOR_KW])
    
    @check_topics_ids(min_length=2)
    async def table_vectors_mean(self, topics_ids: list = []) -> List[float]:
        """
        Get the mean vector of a list of topics

        Parameters:
        topics_ids (list): The topics_ids to get the mean vector from

        Returns:
        list: The mean vector of the entries

        Note:
        if topics_ids is empty, the mean vector of the whole category is returned
        """
        url = os.path.join(self.build_api_path(), VECTOR_KW, "mean")
        result = await self._kuroco_handler.get(url, { "topics_ids": topics_ids })
        return result
    
    @check_topics_ids(min_length=2)
    async def join_vectors(self, topics_ids: list = []) -> List[float]:
        """
        Join the vectors of a list of topics.

        Parameters:
        topics_ids (list): The topics_ids to join vectors from

        Returns:
        list: The joined vector of the topics

        Note:
        if topics_ids is empty, the joined vector of the whole table is returned
        """
        url = os.path.join(self.build_api_path(), VECTOR_KW, "join")
        result = await self._kuroco_handler.get(url, { "topics_ids": topics_ids })
        return result
    
    @check_topics_ids()
    async def get_vector_keywords(self, topics_ids: list = [], limit: int = 5) -> List[float]:
        """
        Get the keywords of a list of topics.
        Keywords are the words that are most similar to the vector of the topics.

        Parameters:
        topics_ids (list): The topics_ids to get the keywords from
        limit (int): The maximum number of keywords to return, 0 for all

        Returns:
        list: The keywords of the topics

        Note:
        if topics_ids is empty, the keywords of the whole table is returned
        """
        url = os.path.join(self.build_api_path(), VECTOR_KW, "keywords")
        result = await self._kuroco_handler.get(url, { "topics_ids": topics_ids, "limit": limit })
        return result
    
    def as_retriever(self, relevant: str | list | tuple = "subject", limit: int = None):
        return KurocoRetriever(self, relevant=relevant, limit=limit)