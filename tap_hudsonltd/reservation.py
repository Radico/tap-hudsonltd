from tap_kit.streams import Stream
import singer


class ReservationStream(Stream):

    stream = 'reservation'

    meta_fields = dict(

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
