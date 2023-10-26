from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import json

from pytdv2.device import Meta


def get_private_key(base64_private_key):
    try:
        # private_key_data = b64decode(base64_private_key)
        private_key = RSA.import_key(base64_private_key)
        return private_key
    except Exception as e:
        raise Exception("Error generating private key") from e


class Utils:
    def __init__(self, private_key):
        self.private_key = private_key

    def decrypt_response(self, encrypted_meta):
        try:
            encrypted_bytes = b64decode(encrypted_meta)
            private_key = get_private_key(self.private_key)
            cipher = PKCS1_v1_5.new(private_key)
            decrypted_bytes = cipher.decrypt(encrypted_bytes, None)
            json_string = decrypted_bytes.decode("utf-8")
            return Meta(**json.loads(json_string))
        except Exception as e:
            print(str(e))
            return Meta()