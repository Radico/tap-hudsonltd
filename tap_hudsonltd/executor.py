from tap_kit import TapExecutor
from tap_kit.utils import timestamp_to_iso8601

import singer


LOGGER = singer.get_logger()


class HudsonltdExecutor(TapExecutor):

    def __init__(self, streams, args, client):
        """
        Args:
            streams: arr[Stream]
            args: dict
            client: BaseClient
        """
        super().__init__(streams, args, client)

        self.url = (f'https://{self.config.get("accountdomain")}.hudsonltd.'
                    f'net/api/')
