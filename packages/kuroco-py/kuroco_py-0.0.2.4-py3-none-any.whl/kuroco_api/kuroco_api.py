import os
import aiohttp
import asyncio
import logging
import json
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from urllib.parse import quote
from typing import List, Dict
from dataclasses import dataclass

from .kuroco_response import KurocoResponse
from .CONFIG import KUROCO_ACCESS_TOKEN, KUROCO_API_DOMAIN, KUROCO_API_VERSION

ACCESS_TOKEN_KEY: str = "x-rcms-api-access-token"

GET_KW: str = "GET"
POST_KW: str = "post"
PUT_KW: str = "POST"
DELETE_KW: str = "POST"

API_NAME: str = "Kuroco API"

KEYS_FOR_INIT: List[str] = [
    KUROCO_ACCESS_TOKEN,
    KUROCO_API_DOMAIN,
    KUROCO_API_VERSION
]


@dataclass
class KurocoAPI:
    """
    A class used to represent a KurocoAPI object
    
    Attributes:
    access_token (str): The access token used for Kuroco API requests
    endpoint (str): The endpoint used for Kuroco API requests
    version (str): The version used for Kuroco API requests
    
    Examples:
    >>> api = KurocoAPI("ACCESS_TOKEN", "test.api.com", 1)
    
    >>> api = KurocoAPI()
    >>> api.post("test", {"test": "test"})
    """
    _access_token: str
    _api_domain: str
    _version: int

    def __init__(self, access_token: str, api_domain: str, api_version: int) -> None:
        """
        Parameters:
        access_token (str): The access token used for Kuroco API requests
        api_domain (str): The domain of the Kuroco API
        api_version (int): The version of the Kuroco API

        Note:
        The access token must be set before making any Kuroco API requests        
        """
        self.access_token = access_token
        self.api_domain = api_domain    
        self.version = api_version
        self.path = KurocoAPI.get_path(self.api_domain, self.version, "")

    @property
    def access_token(self):
        return self._access_token
    
    @access_token.setter
    def access_token(self, value: str):
        self._access_token = KurocoAPI.Checkers.access_token(value)

    @property
    def api_domain(self):
        return self._api_domain
    
    @api_domain.setter
    def api_domain(self, value):
        self._api_domain = KurocoAPI.Checkers.api_domain(value)

    @property
    def version(self):
        """
        Get the version of the Kuroco API.

        Returns:
            str: The version of the Kuroco API.
        """
        return self._version
    
    @version.setter
    def version(self, value):
        self._version = KurocoAPI.Checkers.version(value)

    class Checkers:
        """
        A class used to represent the checkers for the KurocoAPI class
        """    
        @staticmethod
        def access_token(value: str) -> str:
            """
            Checks that the access token is a string.

            Args:
                value (str): The access token to check.

            Returns:
                str: The access token if it is a string.

            Raises:
                AssertionError: If the access token is not a string.
            """
            assert isinstance(value, str), f"{API_NAME} Access token must be a string"
            return value

        @staticmethod
        def api_domain(value: str) -> str:
            """
            Checks that the API domain is a string.

            Args:
                value (str): The API domain to check.

            Returns:
                str: The API domain if it is a string.

            Raises:
                AssertionError: If the API domain is not a string.
            """
            assert isinstance(value, str), f"{API_NAME} domain must be a string"
            return value

        @staticmethod
        def version(value) -> int:
            """
            Converts the version to an integer.

            Args:
                value: The version to convert.

            Returns:
                int: The version as an integer.

            Raises:
                AssertionError: If the version is not an integer or not castable to integer.
            """
            assert isinstance(value, int) or int(value), f"{API_NAME} version must be an integer or a castable type to integer"
            return int(value)

    class Converters:
        @staticmethod  
        def version(value):
            """
            Converts the given value to an integer and returns it as a string.

            Args:
                value (Any): The value to be converted to an integer.

            Returns:
                str: The integer value as a string.
            """
            return f"{int(value)}"

    @classmethod
    def load_from_file(cls, path: str) -> 'KurocoAPI':
        """
        Load the Kuroco API from a configuration file

        Parameters:
        path (str): The path to the file containing the Kuroco API configuration as json

        Returns:
        None
        """
        values_for_init = {}
        with open(path) as f:
            values = json.load(f)
            values_for_init = {str(k).replace("KUROCO_", "").lower(): v for k, v in values.items() if k in KEYS_FOR_INIT}
        return cls(**values_for_init)
    
    @staticmethod
    def get_path(api_domain: str, version: int, endpoint: str) -> dict:
        """
        Get the path to the Kuroco API
        
        Parameters:
        api_domain (str): The domain of the Kuroco API
        version (int): The version of the Kuroco API
        endpoint (str): The endpoint of the Kuroco API
        
        Returns:
        str: The path to the Kuroco API
        """
        assert isinstance(api_domain, str), "API domain must be a string"
        assert isinstance(endpoint, str), "API endpoint must be a string"
        return {"domain": api_domain, "version": KurocoAPI.Converters.version(version), "endpoint": endpoint}

    async def get_endpoints(self) -> List[Dict]:
        """
        Get all endpoints for the Kuroco API

        Returns:
        list: A list of all endpoints for the Kuroco API and their definitions
        """
        # TODO: Implement
        pass

    @staticmethod
    def set_access_token(token: str) -> None:
        """
        Set the access token used for Kuroco API requests
        
        Parameters:
        token (str): The access token to be set
        
        Returns:
        None

        Note:
        Need to be used at least once before making any Kuroco API requests
        """
        assert isinstance(token, str), "Access token must be a string"
        os.environ[KUROCO_ACCESS_TOKEN] = token

    @staticmethod
    async def call(url, method=GET_KW, params=None, data=None, headers=None) -> KurocoResponse:
        logger.info("[%s] URL: %s", method.upper(), url)
        if params:
            params = {k: quote(v) if isinstance(v, str) else v for k, v in params.items() if v is not None}
        s_time = time.time()
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, params=params, data=data, headers=headers) as response:
                if response.status < 400:
                    elapsed_time =  time.time() - s_time
                    logger.info(
                        "[%s] URL: %s, Status: %s, Latency: %.3f s",
                        method.upper(),
                        url,
                        response.status,
                        elapsed_time,
                    )
                    return KurocoResponse(response.status, await response.json())
                else:
                    logger.error(f"Error: {response.status}, {await response.text()}")
                    return KurocoResponse(response.status, await response.text())
    
    async def call_send(self, url, method=GET_KW, params=None, data=None, headers=None) -> KurocoResponse:
        headers = headers or {}
        headers[ACCESS_TOKEN_KEY] = self.access_token
        if data:
            data = json.dumps(data)
        headers["Content-Type"] = "application/json"
        return await KurocoAPI.call(url, method, params, data, headers)

    @staticmethod
    def call_sync(url, method=GET_KW, params=None, data=None, headers=None) -> KurocoResponse:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(KurocoAPI.call(url, method, params, data, headers))

    def call_send_sync(self, url, method=GET_KW, params=None, data=None, headers=None) -> KurocoResponse:
        headers = headers or {}
        headers[ACCESS_TOKEN_KEY] = self.access_token
        if data:
            headers["Content-Type"] = "application/json"
            data = json.dumps(data)
        return KurocoAPI.call_sync(url, method, params, data, headers)
        
    @staticmethod
    def path_maker(base: dict, *endpoint: str) -> str:
        if endpoint and endpoint[0]:
            return os.path.join(base["domain"], base["version"], base["endpoint"], *endpoint)
        else:
            return os.path.join(base["domain"])

    async def post(self, url: str, params: dict = None, data: object = None, no_auto_domain: bool = False) -> KurocoResponse:
        """"
        Make a post request to the Kuroco API
        
        Parameters:
        url (str): The url to make the post request to
        params (dict): The parameters to be sent with the post request
        data (object): The data to be sent with the post request#
        no_auto_domain (bool): Whether to automatically add the api domain to the url
            
        Returns:
        None

        Note:
        The access token is automatically added
        This method is async, so it must be awaited. Use post_sync for a synchronous version
        """
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url)
        return await self.call_send(url=url, method=POST_KW, params=params, data=data)

    def post_sync(self, url: str, params: dict = None, data: object = None, no_auto_domain: bool = False) -> KurocoResponse:
        """"
        Make a post request to the Kuroco API
        
        Parameters:
        url (str): The url to make the post request to
        params (dict): The parameters to be sent with the post request
        data (object): The data to be sent with the post request#
        no_auto_domain (bool): Whether to automatically add the api domain to the url
            
        Returns:
        None

        Note:
        The access token is automatically added
        This method is synchronous, so it must not be awaited. Use post for an asynchronous version
        """
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url)
        return self.call_send_sync(url=url, method=POST_KW, params=params, data=data)

    async def get(self, url: str, params: dict, no_auto_domain: bool = False) -> KurocoResponse:
        """
        Make a get request to the Kuroco API

        Parameters:
        url (str): The url to make the get request to
        params (dict): The parameters to be sent with the get request
        no_auto_domain (bool): Whether to automatically add the api domain to the url

        Returns:
        None

        Note:
        The access token is automatically added to the params
        This method is async, so it must be awaited. Use get_sync for a synchronous version
        """
        if "filter" in params:
            if not params["filter"]:
                del params["filter"]
            else:
                # Format filter as string
                params["filter"] = "&".join([f"{k}={v}" for k, v in params["filter"].items()])
                # Remove top &
                params["filter"] = params["filter"][1:]
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url)
        return await self.call_send(url, GET_KW, params)

    def get_sync(self, url: str, params: dict, no_auto_domain: bool = False) -> KurocoResponse:
        """
        Make a get request to the Kuroco API

        Parameters:
        url (str): The url to make the get request to
        params (dict): The parameters to be sent with the get request
        no_auto_domain (bool): Whether to automatically add the api domain to the url

        Returns:
        None

        Note:
        The access token is automatically added to the params
        This method is synchronous, so it must not be awaited. Use get for an asynchronous version
        """
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url)
        return self.call_send_sync(url, GET_KW, params)

    async def put(self, url: str, key: str, params: dict = None, data: object = None, no_auto_domain: bool = False) -> KurocoResponse:
        """
        Make a put request to the Kuroco API

        Parameters:
        url (str): The url to make the put request to
        params (dict): The parameters to be sent with the put request
        data (object): The data to be sent with the put request
        no_auto_domain (bool): Whether to automatically add the api domain to the url

        Returns:
        None

        Note:
        The access token is automatically added to the params
        This method is async, so it must be awaited. Use put_sync for a synchronous version
        """
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url, key)
        return await self.call_send(method=PUT_KW, url=url, params=params, data=data)

    def put_sync(self, url: str, key: str, params: dict = None, data: object = None, no_auto_domain: bool = False) -> KurocoResponse:
        """
        Make a put request to the Kuroco API

        Parameters:
        url (str): The url to make the put request to
        params (dict): The parameters to be sent with the put request
        data (object): The data to be sent with the put request
        no_auto_domain (bool): Whether to automatically add the api domain to the url

        Returns:
        None

        Note:
        The access token is automatically added to the params
        This method is synchronous, so it must not be awaited. Use put for an asynchronous version
        """
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url, key)
        return self.call_send_sync(method=PUT_KW, url=url, params=params, data=data)

    async def delete(self, url: str, key: str, no_auto_domain: bool = False) -> KurocoResponse:
        """
        Make a delete request to the Kuroco API

        Parameters:
        url (str): The url to make the delete request to
        key (str): The key to make the delete request to
        no_auto_domain (bool): Whether to automatically add the api domain to the url

        Returns:
        None

        Note:
        The access token is automatically added to the params
        This method is async, so it must be awaited. Use delete_sync for a synchronous version
        """
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url, key)
        return await self.call_send(url, DELETE_KW, {})
    
    def delete_sync(self, url: str, key: str, no_auto_domain: bool = False) -> KurocoResponse:
        """
        Make a delete request to the Kuroco API

        Parameters:
        url (str): The url to make the delete request to
        key (str): The key to make the delete request to
        no_auto_domain (bool): Whether to automatically add the api domain to the url

        Returns:
        None

        Note:
        The access token is automatically added to the params
        This method is synchronous, so it must not be awaited. Use delete for an asynchronous version
        """
        if not no_auto_domain:
            url = KurocoAPI.path_maker(self.path, url, key)
        return self.call_send_sync(url, DELETE_KW, {})
