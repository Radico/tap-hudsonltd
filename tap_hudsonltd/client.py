import singer
import requests
import backoff

from tap_kit import BaseClient


LOGGER = singer.get_logger()


class RateLimitException(Exception):
    pass


class HudsonClient(BaseClient):

    @staticmethod
    def requests_method(method, request_config, body):
        return requests.request(
            method,
            request_config['url'],
            headers=request_config['headers'],
            data=request_config['data'])
