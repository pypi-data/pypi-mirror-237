from __future__ import annotations
import json
import logging
from http.client import HTTPResponse
from typing import MutableMapping
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zut.json import ExtendedJSONDecoder, ExtendedJSONEncoder

class JSONApiClient:
    base_url : str = None
    timeout: float = None
    """ Timeout in seconds. """

    force_trailing_slash: bool = False

    default_headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json; charset=utf-8',
    }

    json_encoder_cls: type[json.JSONEncoder] = ExtendedJSONEncoder
    json_decoder_cls: type[json.JSONDecoder] = ExtendedJSONDecoder
    
    nonjson_error_maxlen = 400


    def __init__(self):
        self.logger = logging.getLogger(type(self).__module__ + '.' + type(self).__name__)


    def __enter__(self):
        return self


    def __exit__(self, exc_type = None, exc_value = None, exc_traceback = None):
        pass


    def get(self, endpoint: str, *, params: dict = None):
        return self.request(endpoint, params=params)


    def post(self, endpoint: str, data, *, params: dict = None):
        return self.request(endpoint, data, params=params)
    

    def request(self, endpoint: str, data = None, *, method = None, params: dict = None):
        url = self.prepare_url(endpoint, params=params)

        headers = self.get_request_headers(url)
        
        if data is not None:
            if not method:
                method = 'POST'
            
            self.logger.debug('%s %s', method, url)
            request = Request(url,
                method=method,
                headers=headers,
                data=json.dumps(data, ensure_ascii=False, cls=self.json_encoder_cls).encode('utf-8'),
            )
        else:
            if not method:
                method = 'GET'
            
            self.logger.debug('%s %s', method, url)
            request = Request(url,
                method=method,
                headers=headers,
            )

        try:
            response: HTTPResponse
            with urlopen(request, timeout=self.timeout) as response:
                if self.logger.isEnabledFor(logging.DEBUG):
                    content_type = response.headers.get('content-type', '-')
                    self.logger.debug('%s %s %s %s', response.status, url, response.length, content_type)
                return self.decode_response(response)
        except HTTPError as error:
            with error:
                http_data = self.decode_response(error)
            built_error = self.build_client_error(error, http_data)
        except URLError as error:
            built_error = self.build_client_error(error, None)

        if isinstance(built_error, Exception):
            raise built_error from None
        else:
            return built_error


    def prepare_url(self, endpoint: str, *, params: dict = None, base_url: str = None):
        if not base_url and self.base_url:
            base_url = self.base_url

        if '://' in endpoint or not base_url:
            url = endpoint
            
        else:            
            if endpoint.startswith('/'):
                if base_url.endswith('/'):                    
                    endpoint = endpoint[1:]
            else:
                if not base_url.endswith('/'):
                    endpoint = f'/{endpoint}'
            
            if getattr(self, 'force_trailing_slash', False) and not endpoint.endswith('/'):
                endpoint = f'{endpoint}/'

            url = f'{base_url}{endpoint}'

        if params:
            url += "?" + urlencode(params)
        
        return url
    

    def get_request_headers(self, url: str) -> MutableMapping[str,str]:
        headers = {**self.default_headers}
        return headers


    def decode_response(self, response: HTTPResponse):
        rawdata = response.read()
        try:
            strdata = rawdata.decode('utf-8')
        except UnicodeDecodeError:
            strdata = str(rawdata)
            if len(strdata) > self.nonjson_error_maxlen:
                strdata = strdata[0:self.nonjson_error_maxlen] + '…'
            return f"[non-utf-8] {strdata}"
        
        try:
            jsondata = json.loads(strdata, cls=self.json_decoder_cls)
        except json.JSONDecodeError:
            if len(strdata) > self.nonjson_error_maxlen:
                strdata = strdata[0:self.nonjson_error_maxlen] + '…'
            return f"[non-json] {strdata}"
        
        return jsondata


    def build_client_error(self, error: URLError, http_data):
        if isinstance(error, HTTPError):
            return ApiClientError(error.reason, code=error.status, code_nature='status', data=http_data)
        else:
            return ApiClientError(error.reason, code=error.errno, code_nature='errno', data=http_data)
        

class ApiClientError(Exception):
    def __init__(self, message: str, *, code: int = None, code_nature = None, data = None):
        self.raw_message = message
        self.code = code
        self.code_nature = code_nature
        self.data = data

        super().__init__(self.raw_to_message())


    def raw_to_message(self):
        message = self.raw_message

        if self.code:
            message = (message + ' ' if message else '') + f"[{self.code_nature or 'code'}: {self.code}]"
        
        if self.data:
            if isinstance(self.data, dict):
                for key, value in self.data.items():
                    message = (message + '\n' if message else '') + f"{key}: {value}"
            else:
                message = (message + '\n' if message else '') + str(self.data)

        return message
