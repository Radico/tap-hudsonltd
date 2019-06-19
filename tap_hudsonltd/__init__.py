from tap_kit import main_method
from .executor import HudsonltdExecutor
from .client import BaseClient
from .profile import ProfileStream
from .reservation import ReservationStream


REQUIRED_CONFIG_KEYS = [
]

STREAMS = [
	ProfileStream,
	ReservationStream,
]

def main():
	main_method(
		REQUIRED_CONFIG_KEYS,
		HudsonltdExecutor,
		BaseClient,
		STREAMS
	)

if __name__ == '__main__':
	main()
