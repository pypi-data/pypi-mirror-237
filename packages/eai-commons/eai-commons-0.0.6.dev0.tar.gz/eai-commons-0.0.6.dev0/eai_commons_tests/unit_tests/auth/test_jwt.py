import time

from eai_commons_tests.unit_tests.auth import user_payload
from eai_commons.auth.jwt import Jwt

jwt = Jwt("590BC6AB96564EC9AD8561D09D5655CB", expired=2, leeway=1)


def test_jwt_encrypt_decrypt():
    encrypt = jwt.create_jwt(user_payload)
    decrypt_payload = jwt.verify_jwt(encrypt)
    assert user_payload["id"] == decrypt_payload["id"]


def test_jwt_expire():
    encrypt = jwt.create_jwt(user_payload)
    time.sleep(2)
    decrypt_payload = jwt.verify_jwt(encrypt)
    assert user_payload["id"] == decrypt_payload["id"]

    time.sleep(2)
    try:
        jwt.verify_jwt(encrypt)
    except:
        pass
