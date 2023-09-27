from decouple import config
import hmac
import hashlib
import time


def hmac_connection(API_SECRET, payload):
    signature = hmac.new(API_SECRET.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
    return signature.hexdigest()
