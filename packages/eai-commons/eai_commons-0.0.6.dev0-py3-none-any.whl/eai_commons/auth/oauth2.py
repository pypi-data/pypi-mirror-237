import requests
import json
from abc import abstractmethod

from eai_commons.logging import logger
from eai_commons.utils.cryptor import base64_encode
from eai_commons.error.errors import ForbiddenException, UNAUTHORIZED


def _verify_request_success(response: requests.Response) -> None:
    if response.status_code != 200:
        logger.error(
            f"access error. url = {response.request.url}, "
            f"http code = {response.status_code}, error msg = {response.text}"
        )
        raise ForbiddenException(UNAUTHORIZED)


class OAuth2Service:
    @abstractmethod
    def authcode_to_access_token(self, authcode: str):
        raise NotImplementedError

    @abstractmethod
    def access_token_to_userinfo(self, access_token: str):
        raise NotImplementedError


class DatastoryOauth2Service(OAuth2Service):
    def __init__(
        self, api_base: str, client_id: str, client_secret: str, redirect_url: str
    ) -> None:
        self.api_base = api_base
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        super().__init__()

    def authcode_to_access_token(
        self, authcode: str
    ) -> tuple[str:"access_token", int:"expire_time"]:
        logger.info(f"oauth2 callback success, auth code = {authcode}")
        query_params = {
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_url,
            "code": authcode,
        }

        basic_auth = base64_encode(f"{self.client_id}:{self.client_secret}")
        response = requests.post(
            url=f"{self.api_base}/oauth/token",
            headers={"Authorization": f"Basic {basic_auth}"},
            params=query_params,
        )
        _verify_request_success(response)

        _dict = json.loads(response.content)
        return _dict.pop("access_token"), _dict.pop("expires_in")

    def access_token_to_userinfo(self, access_token: str, **kwargs) -> dict:
        query_params = {
            "fieldMask": kwargs["field_mask"] if "field_mask" in kwargs else "*",
        }
        response = requests.get(
            url=f"{self.api_base}/api/v1/me",
            headers={"Authorization": f"Bearer {access_token}"},
            params=query_params,
        )
        _verify_request_success(response)

        return json.loads(response.content)
