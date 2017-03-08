# Conway's Game Of Life sim in Python3

### How to run ?

Run `python3 main.py` in the terminal to start the simulation.

### Directory structure

    Game Of Life
    ├── game_config.json
    ├── game_of_life
    │   ├── __init__.py
    │   └── board.py
    ├── game_params
    │   ├── __init__.py
    │   └── game_params.py
    ├── main.py
    ├── readme.md
    └── test.py


`game_config.json` - Contains various tunable parameters for the simulation

`board.py` - `Board` class, heart of the simulation

`game_params` - Helper module to board, helps parse `game_config.json`

`main.py` - Runs the simulation with default parameter read from the `game_config.json` 

`test.py` - Unittests for `Board` class

### Dependencies
- `numpy`

### Author
Sayan Goswami (@Sayan98)