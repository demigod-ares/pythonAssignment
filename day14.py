from enum import Enum

class TiltDirection(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class Tile(Enum):
    Empty = "."
    CubeRock = "#"
    RoundRock = "O"


def tilt_platform(platform_state, direction=TiltDirection.North): # North only
    if direction != TiltDirection.North:
        NotImplementedError("Only TiltDirection.North is supported for now")
    # split the platform state into rows
    platform_state = [list(row) for row in platform_state.split("\n")]
    for i, row in enumerate(platform_state):
        for j, tile in enumerate(row):
            if tile == Tile.RoundRock.value:
                # move this rock upwards in column
                row_idx, col_idx = i, j
                while (
                    row_idx - 1 >= 0
                    and platform_state[row_idx - 1][col_idx] == Tile.Empty.value
                ):
                    platform_state[row_idx][col_idx] = Tile.Empty.value
                    platform_state[row_idx - 1][col_idx] = Tile.RoundRock.value
                    row_idx -= 1

    return platform_state


def calculate_load_on_north_beam(tilted_platform_state):
    total_load = 0
    load_factor = len(tilted_platform_state)
    for row in tilted_platform_state:
        total_load += load_factor * row.count(Tile.RoundRock.value)
        load_factor -= 1

    return total_load


def solution():
    with open("input.txt") as f:
        platform_state = f.read()

    tilted_platform_state = tilt_platform(platform_state, TiltDirection.North)
    print(f"{tilted_platform_state}")
    total_load = calculate_load_on_north_beam(tilted_platform_state)
    print(f"Total load on the north beam is {total_load}")

    tilted_platform_state = tilt_platform(platform_state, TiltDirection.North)

solution()