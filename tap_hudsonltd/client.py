import singer
import requests
import time

from tap_kit import BaseClient


LOGGER = singer.get_logger()


class RateLimitException(Exception):
    pass


class HudsonClient(BaseClient):

    @staticmethod
    def requests_method(method, request_config, body):
        retries = 5
        delay = 30
        backoff = 1.5
        attempt = 1
        while retries >= attempt:

            response = requests.request(
                method,
                request_config['url'],
                headers=request_config['headers'],
                data=request_config['data']
            )
            if response.status_code in [500]:
                LOGGER.info(f"[Error {response.status_code}] with this "
                            f"response:\n {response}")
                time.sleep(delay)
                delay *= backoff
                attempt += 1
            else:
                return response

        LOGGER.info(f"Reached maximum retries ({retries}), failing...")
        raise ValueError("Maximum retries reached")
