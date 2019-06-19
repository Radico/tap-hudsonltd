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

class ReservationStream(Stream):

    def build_base_metadata(self, metadata):
        for field in _META_FIELDS:
            if self.meta_fields.get(_META_FIELDS[field]) is not None:
                self.write_base_metadata(
                    metadata, field, self.meta_fields[_META_FIELDS[field]]
                )

        self.write_base_metadata(metadata, 'inclusion', 'available')
        self.write_base_metadata(metadata, 'schema-name', self.stream)

    stream = 'reservation'

    meta_fields = dict(
        key_properties=['id'],
        replication_method='incremental',
        replication_key='PickupTOD',
        request_token='ReservationsSimon-Filter',
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
            "CompID": {
              "type": [
                "string",
                "null"
              ]
            },
            "WResID": {
              "type": [
                "string",
                "null"
              ]
            },
            "PickupTOD": {
              "type": [
                "string",
                "null"
              ],
              "format": "date-time"
            },
            "PickupLocation": {
              "type": [
                "string",
                "null"
              ]
            },
            "PickupAddr": {
              "type": [
                "string",
                "null"
              ]
            },
            "PickupCity": {
              "type": [
                "string",
                "null"
              ]
            },
            "PickupState": {
              "type": [
                "string",
                "null"
              ]
            },
            "PickupZip": {
              "type": [
                "string",
                "null"
              ]
            },
            "DropOffTOD": {
              "type": [
                "string",
                "null"
              ],
              "format": "date-time"
            },
            "DropOffLocation": {
              "type": [
                "string",
                "null"
              ]
            },
            "DropOffAddr": {
              "type": [
                "string",
                "null"
              ]
            },
            "DropOffCity": {
              "type": [
                "string",
                "null"
              ]
            },
            "DropOffState": {
              "type": [
                "string",
                "null"
              ]
            },
            "DropOffZip": {
              "type": [
                "string",
                "null"
              ]
            },
            "Direction": {
              "type": [
                "string",
                "null"
              ]
            },
            "Passengers": {
              "type": [
                "integer",
                "null"
              ]
            },
            "AltPassengers": {
              "type": [
                "integer",
                "null"
              ]
            },
            "AltPassengers2": {
              "type": [
                "integer",
                "null"
              ]
            },
            "AltPassengers3": {
              "type": [
                "integer",
                "null"
              ]
            },
            "BaseFare": {
              "type": [
                "string",
                "null"
              ]
            },
            "AltFare": {
              "type": [
                "string",
                "null"
              ]
            },
            "BaggageCharge": {
              "type": [
                "string",
                "null"
              ]
            },
            "MiscCharge": {
              "type": [
                "string",
                "null"
              ]
            },
            "UserGratuity": {
              "type": [
                "string",
                "null"
              ]
            },
            "Parking": {
              "type": [
                "string",
                "null"
              ]
            },
            "Fare": {
              "type": [
                "string",
                "null"
              ]
            },
            "PaymentType": {
              "type": [
                "string",
                "null"
              ]
            },
            "ServiceType": {
              "type": [
                "string",
                "null"
              ]
            },
            "Airline": {
              "type": [
                "string",
                "null"
              ]
            },
            "FlightNumber": {
              "type": [
                "string",
                "null"
              ]
            },
            "FlightTOD": {
              "type": [
                "string",
                "null"
              ],
              "format": "date-time"
            },
            "FlightCity": {
              "type": [
                "string",
                "null"
              ]
            },
            "Name": {
              "type": [
                "string",
                "null"
              ]
            },
            "Telephone": {
              "type": [
                "string",
                "null"
              ]
            },
            "Telephone2": {
              "type": [
                "string",
                "null"
              ]
            },
            "EmailAddr": {
              "type": [
                "string",
                "null"
              ]
            },
            "PUDDirections": {
              "type": [
                "string",
                "null"
              ]
            },
            "SpecialInstr": {
              "type": [
                "string",
                "null"
              ]
            },
            "ChargeTo": {
              "type": [
                "string",
                "null"
              ]
            },
            "ConfirmedWith": {
              "type": [
                "string",
                "null"
              ]
            },
            "ProfileIDLocal": {
              "type": [
                "string",
                "null"
              ]
            },
            "ProfileIDParent": {
              "type": [
                "string",
                "null"
              ]
            },
            "CarSeat": {
              "type": [
                "string",
                "null"
              ]
            },
            "Kennel": {
              "type": [
                "string",
                "null"
              ]
            },
            "BagCount": {
              "type": [
                "string",
                "null"
              ]
            },
            "Operation": {
              "type": [
                "string",
                "null"
              ]
            },
            "SourceName": {
              "type": [
                "string",
                "null"
              ]
            },
            "dVehicle": {
              "type": [
                "string",
                "null"
              ]
            },
            "dDriver": {
              "type": [
                "string",
                "null"
              ]
            },
            "JobType": {
              "type": [
                "string",
                "null"
              ]
            },
            "ServiceArea": {
              "type": [
                "string",
                "null"
              ]
            },
            "AltPassengers4": {
              "type": [
                "string",
                "null"
              ]
            },
            "AltPassengers5": {
              "type": [
                "string",
                "null"
              ]
            },
            "PAX": {
              "type": [
                "string",
                "null"
              ]
            }
          }
        }
