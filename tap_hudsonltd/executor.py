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
        self.MAX_RECORDS = 10000

    def call_incremental_stream(self, stream):
        start_date, end_date = self.intialize_dates(self)

        request_config = {
            'url': self.url,
            'headers': self.build_headers(),
            'run': True,
            'data': self.build_body(stream, start_date)
        }

        while request_config['run']:
            res = self.client.make_request(request_config, method='POST')

            if res.status_code != 200:
                raise AttributeError(f'Received status_code {res.status_code}')

            records = self.convert_to_json(res)
            if len(records) == self.MAX_RECORDS:
                raise ValueError('Number of records returned is equal to '
                                 'hudson\'s limit. This means that we will be '
                                 'missing data.')
            transform_write_and_count(stream, records)

            start_date = start_date.add(days=1)
            if start_date == end_date:
                request_config['run'] = False
            else:
                request_config['data'] = self.build_body(stream, start_date)

    @staticmethod
    def intialize_dates(self):
        """Returns the dates a week before and a week after"""
        today = pendulum.today('UTC')
        week_earlier = today.subtract(weeks=1)
        week_later = today.add(weeks=1)
        return (week_earlier, week_later)

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

    def build_body(self, stream, start_date):
        """Builds request in xml format"""
        stream_request_token = stream.stream_metadata['request-token']
        start_date_str = start_date.to_date_string()
        next_day = start_date.add(days=1).to_date_string()
        xml_string = f"""<?xml version='1.0'?>
<ReadRecords>
    <SiteId>a15515</SiteId>
    <RequestToken>{stream_request_token}</RequestToken>
    <FilterDate1>{start_date_str}</FilterDate1>
    <FilterDate2>{next_day}</FilterDate2>
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
            record_dict['date_pulled'] = pendulum.now(
                'UTC').to_datetime_string()
            export_records.append(record_dict)
        return export_records

    def sync_stream(self, stream):
        """Not using a bookmark for incremental stream"""
        stream.write_schema()

        if stream.is_incremental:
            stream.set_stream_state(self.state)
            last_updated = self.call_incremental_stream(stream)
        else:
            self.call_full_stream(stream)
