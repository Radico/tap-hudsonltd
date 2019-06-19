# tap-hudsonltd
Singer tap for extracting from HudsonLTD API

## Setup

`python3 setup.py install`

## Running the tap

#### Discover mode:

`tap-hudsonltd --config config.json --discover > catalog.json`

#### Sync mode:

`tap-hudsonltd --config config.json -p catalog.json -s state.json`
