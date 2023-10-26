from __future__ import annotations

import time
from io import FileIO, IOBase
from typing import BinaryIO, Any

import requests
from requests import Request

from semantha_sdk.request.semantha_request import SemanthaRequest


def _convert_value(value: Any):
    if isinstance(value, IOBase):
        return value

    if isinstance(value, bool):
        return str(value).lower()

    return str(value)


def _filter_and_convert_to_str(data: dict, remove_empty_lists=False):
    data = {k: v for k, v in data.items() if v is not None}

    if remove_empty_lists:
        data = {k: v for k, v in data.items() if not (isinstance(v, list) and len(v) == 0)}

    data = {k: _convert_value(v) for k, v in data.items()}
    return data


def _filter_json(data: dict):
    data = {k: v for k, v in data.items() if v is not None}
    return data


class MediaType:
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    JSON = "application/json"
    PDF = "application/pdf"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    ZIP = "application/zip"


class RestClient:
    __expire_time: float
    # in seconds
    LEEWAY = 30
    def __init__(self, server_url: str, api_key: str = None, client_id: str = None, client_secret: str = None,
                 token_url: str = None):
        self.__server_url = server_url
        self.__api_key = api_key
        self.__client_id = client_id
        self.__client_secret = client_secret
        self.__token_url = token_url
        self.__expire_time = 0.0
        self.__access_token = None

    def __build_headers_for_json_request(self) -> dict[str, str]:
        return {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.__get_token()}'
        }

    def __build_headers_for_request(self) -> dict[str, str]:
        return {
            'Authorization': f'Bearer {self.__get_token()}'
        }

    def __get_token(self):
        if self.__api_key:
            return self.__api_key
        if (self.__client_id and self.__client_secret and self.__token_url and
                (self.__access_token is None or self.__expire_time < time.monotonic())):
            headers = {'Accept': 'application/json'}
            data = {'grant_type': 'client_credentials', 'client_id': self.__client_id,
                    'client_secret': self.__client_secret, 'scope': 'openid'}
            r = requests.post(self.__token_url, headers=headers, data=data)
            if r.status_code >= requests.codes.bad_request:
                # example for error response: {"error":"invalid_client","error_description":"Invalid client or Invalid client credentials"}
                # we have no token -> this leads to a permission error
                return ""
            resp = r.json()
            # example response: {"access_token":"<TOKEN>","expires_in":300,"refresh_expires_in":0,"token_type":"Bearer","id_token":"<TOKEN>","not-before-policy":0,"scope":"openid profile email"}
            self.__access_token = resp['access_token'] if 'id_token' not in resp else resp['id_token']
            self.__expire_time = time.monotonic() + (resp['expires_in'] - RestClient.LEEWAY)
        return self.__access_token

    def __request(self,
                  method,
                  url,
                  headers=None,
                  files=None,
                  data=None,
                  params=None,
                  auth=None,
                  cookies=None,
                  hooks=None,
                  json: dict | list = None
                  ) -> SemanthaRequest:
        if headers is None:
            headers = self.__build_headers_for_json_request()
        else:
            headers = {**headers, **self.__build_headers_for_request()}

        if json is not None and type(json) is dict:
            json = _filter_json(json)

        if data is not None:
            data = _filter_and_convert_to_str(data, remove_empty_lists=True)

        if files is not None:
            files = _filter_and_convert_to_str(files, remove_empty_lists=True)

        if params is not None:
            params = _filter_and_convert_to_str(params)

        headers['User-Agent'] = 'semantha Python SDK; '
        request = Request(
            method=method,
            url=self.__server_url + url,
            headers=headers,
            files=files,
            data=data,
            params=params,
            auth=auth,
            cookies=cookies,
            hooks=hooks,
            json=json
        )
        prepared_request = request.prepare()
        return SemanthaRequest(prepared_request)

    def get(self, url: str, q_params: dict[str, str] = None, headers: dict[str, str] = None) -> SemanthaRequest:
        return self.__request("GET", url, params=q_params, headers=headers)

    def post(
            self,
            url: str,
            body: dict = None,
            json: dict | list = None,
            q_params: dict = None,
            headers: dict[str, str] = None,
    ) -> SemanthaRequest:
        if body is None and json is None:
            raise ValueError("Either a body (files/form-data) or a json must be provided!")
        return self.__request("POST", url, files=body, json=json, params=q_params, headers=headers)

    def delete(self, url: str, q_params: dict[str, str] = None, json: dict | list = None) -> SemanthaRequest:
        return self.__request("DELETE", url, params=q_params, json=json)

    def patch(self, url: str, body: dict = None, json: dict | list = None,
              q_params: dict[str, str] = None) -> SemanthaRequest:
        if body is None and json is None:
            raise ValueError("Either a body (files/form-data) or a json must be provided!")
        return self.__request("PATCH", url, files=body, json=json, params=q_params)

    def put(self, url: str, body: dict = None, json: dict | list = None,
            q_params: dict[str, str] = None) -> SemanthaRequest:
        if body is None and json is None:
            raise ValueError("Either a body (files/form-data) or a json must be provided!")
        return self.__request("PUT", url, files=body, json=json, params=q_params)

    def to_header(accept_mime_type: str, content_type: str = None):
        if content_type:
            return {"Accept": accept_mime_type, "Content-Type": content_type}
        else:
            return {"Accept": accept_mime_type}
