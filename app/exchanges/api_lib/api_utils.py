import time


class BaseAPI:
    pass


def get_timestamp():
    return int(time.time() * 1000)
