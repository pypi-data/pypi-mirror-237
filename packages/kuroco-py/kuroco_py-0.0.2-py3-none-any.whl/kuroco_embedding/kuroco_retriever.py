import asyncio
from typing import List

from langchain.schema.retriever import BaseRetriever
from langchain.schema.document import Document
from langchain.docstore.document import Document

THRESHOLD = 0.8

class KurocoRetriever (BaseRetriever):
    """
    KurcoRetriever is a retriever that uses KurocoEmbedding to search for similar documents.
    It is designed to be used in Langchain.

    It requires a KurocoEmbedding instance and a list of relevant columns to search for.

    Attributes:
        metadata (dict): Metadata of the retriever.
        metadata["embedder"] (KurocoEmbedding): KurocoEmbedding instance.
        metadata["relevant"] (list): List of relevant columns to search for.
        metadata["limit"] (int): Limit of results. 0 for no limit.

    Examples:
        >>> from kuroco import KurocoAPI, KurocoEmbedding
        >>> k_api = KurocoAPI.load_from_file(path='kuroco.json')
        >>> k_emb = KurocoEmbedding(('Shops', 'Zones'), k_api)
        >>> k_retriever = KurocoRetriever(k_emb, 'subject')
        >>> def format_docs(docs):
        >>>     return "\n\n".join([d.page_content for d in docs])
        >>> chain = (
        >>>     {"context": k_retriever | format_docs, "question": RunnablePassthrough()}
        >>>     | prompt
        >>>     | model
        >>>     | StrOutputParser()
        >>> )
        >>> chain.invoke("query")

    """
    def __init__(self, k_emb: 'KurocoEmbedding', relevant: list, limit: int = None):
        BaseRetriever.__init__(self)
        self.metadata = {}
        self.metadata["embedder"] = k_emb
        self.metadata["relevant"] = relevant if isinstance(relevant, list) else [relevant]
        self.metadata["limit"] = limit

    class Config:
        """
        Pydantic configuration.
        """
        arbitrary_types_allowed = True
    
    def _get_relevant_documents(
        self, query: str, *, run_manager 
    ) -> List[Document]:
        loop = asyncio.new_event_loop()
        results = loop.run_until_complete(self.metadata["embedder"].similarity_search(query, limit=self.metadata['limit'], with_score=False, threshold=THRESHOLD))
        loop.close()
        selected_columns = [col for col in self.metadata["relevant"] if col in results.columns]
        return [Document(page_content=w, 
                         metadata={"source": "kuroco", 
                                    "field": selected_columns[i]})
                        for v in results.loc[:, selected_columns].values.tolist()
                        for i, w in enumerate(v) if w
                ]
    