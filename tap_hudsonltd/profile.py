from tap_kit.streams import Stream
import singer


_META_FIELDS = {
    'table-key-properties': 'key_properties',
    'forced-replication-method': 'replication_method',
    'valid-replication-keys': 'valid_replication_keys',
    'replication-key': 'replication_key',
    'selected-by-default': 'selected_by_default',
    'incremental-search-key': 'incremental_search_key',
    'api-path': 'api_path',
    'request-token': 'request_token',
}

class ProfileStream(Stream):

    def build_base_metadata(self, metadata):
        for field in _META_FIELDS:
            if self.meta_fields.get(_META_FIELDS[field]) is not None:
                self.write_base_metadata(
                    metadata, field, self.meta_fields[_META_FIELDS[field]]
                )

        self.write_base_metadata(metadata, 'inclusion', 'available')
        self.write_base_metadata(metadata, 'schema-name', self.stream)

    stream = 'profile'

    meta_fields = dict(
        key_properties=['id'],
        replication_method='full',
        replication_key='pickuptod',
        request_token='ProfilesSimon-Filter',
    )

    schema = \
    {
      "properties": {
        "ID": {
          "type": [
            "null",
            "integer"
          ]
        },
        "ProfileType": {
          "type": [
            "null",
            "string"
          ]
        },
        "WebID": {
          "type": [
            "null",
            "string"
          ]
        },
        "Name": {
          "type": [
            "null",
            "string"
          ]
        },
        "Address": {
          "type": [
            "null",
            "string"
          ]
        },
        "City": {
          "type": [
            "null",
            "string"
          ]
        },
        "State": {
          "type": [
            "null",
            "string"
          ]
        },
        "ZipCode": {
          "type": [
            "null",
            "string"
          ]
        },
        "Telephone": {
          "type": [
            "null",
            "integer"
          ]
        },
        "Telephone2": {
          "type": [
            "null",
            "integer"
          ]
        },
        "EmailAddress": {
          "type": [
            "null",
            "string"
          ]
        },
        "ReservationCount": {
          "type": [
            "null",
            "integer"
          ]
        },
        "ReservationFirstTOD": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time"
        },
        "ReservationLastTOD": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time"
        },
        "LastUpdateName": {
          "type": [
            "null",
            "string"
          ]
        },
        "RecordUpdateTOD": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time"
        },
        "SourceTOD": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time"
        },
        "JobType": {
          "type": [
            "null",
            "string"
          ]
        },
        "SpecialInstr": {
          "type": [
            "null",
            "string"
          ]
        },
        "SpecialInstr2": {
          "type": [
            "null",
            "string"
          ]
        },
        "AgentNotification": {
          "type": [
            "null",
            "string"
          ]
        },
        "Platform": {
          "type": [
            "null",
            "string"
          ]
        },
        "Status": {
          "type": [
            "null",
            "string"
          ]
        },
      }
    }
