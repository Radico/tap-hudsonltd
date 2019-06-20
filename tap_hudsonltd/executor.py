from tap_kit import TapExecutor
from tap_kit.utils import timestamp_to_iso8601, transform_write_and_count, \
    format_last_updated_for_request

import singer
import base64
import pendulum
from xml.etree import ElementTree
from bs4 import BeautifulSoup

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

        self.replication_key_format = 'datetime_string'
        self.url = (f'https://{self.config.get("accountdomain")}.hudsonltd.'
                    f'net/api/ReadRecords')

    def call_full_stream(self, stream):
        """Extract a full stream"""
        request_config = {
            'url': self.url,
            'headers': self.build_headers(),
            'run': True,
            'data': self.build_body(stream)
        }

        res = self.client.make_request(request_config, method='POST')

        if res.status_code != 200:
            raise AttributeError(f'Received status_code {res.status_code}')

        records = self.convert_to_json(res)
        transform_write_and_count(stream, records)

    def build_headers(self):
        return {
            'Content-Type': 'application/xml',
            'X-Authorization': self.build_x_authorization()
        }

    def build_x_authorization(self):
        """Encodes the id and pw to base64"""
        encoding_string = (f'{self.config.get("user_id")}:'
                           f'{self.config.get("pw")}').encode('ascii')
        return base64.b64encode(encoding_string).decode('utf-8')

    def build_body(self, stream):
        """Builds request in xml format"""
        stream_request_token = stream.stream_metadata['request-token']
        today = pendulum.today('UTC')
        week_earlier = today.subtract(weeks=1).to_date_string()
        week_later = today.add(weeks=1).to_date_string()
        xml_string = f"""<?xml version='1.0'?>
<ReadRecords>
    <SiteId>a15515</SiteId>
    <RequestToken>{stream_request_token}</RequestToken>
    <FilterDate1>{week_earlier}</FilterDate1>
    <FilterDate2>{week_later}</FilterDate2>
</ReadRecords>"""
        return xml_string

    @staticmethod
    def convert_to_json(res):
        """Converts xml request to json"""
        soup = BeautifulSoup(res.text, 'html.parser')
        export_records = []
        head = soup.find('gdfrecords')
        records = head.find_all('record')
        for record in records:
            record_dict = {}
            children = record.findChildren()
            for child in children:
                record_dict[child.name] = child.text
            export_records.append(record_dict)
        return export_records
