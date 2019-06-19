import singer
import requests
import backoff
import time
from requests.auth import HTTPBasicAuth

LOGGER = singer.get_logger()


class RateLimitException(Exception):
    pass


class BaseClient:
    RATE_LIMIT_PAUSE = 30
    url = None
    auth_type = None

    def __init__(self, config):
        self.config = config
