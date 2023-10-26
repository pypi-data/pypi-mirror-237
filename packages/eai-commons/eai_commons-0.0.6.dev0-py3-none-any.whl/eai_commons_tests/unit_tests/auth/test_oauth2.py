import os

from eai_commons.auth.oauth2 import DatastoryOauth2Service


oauth_service = DatastoryOauth2Service(
    os.getenv("DS_API_BASE"),
    os.getenv("DS_CLIENT_ID"),
    os.getenv("DS_CLIENT_SECRET"),
    os.getenv("DS_REDIRECT_URL"),
)


def test_oauth_code():
    auth_code = "Akvq27fwcWK3el9a"
    atk, expired_at = oauth_service.authcode_to_access_token(auth_code)
    payload = oauth_service.access_token_to_userinfo(atk)
    print(payload)

    assert payload["id"] is not None
