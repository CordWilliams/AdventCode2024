import numpy as np

def read_input(file):
    with open(file, "r") as f:
        input_text = f.read()
    return np.array([list(line) for line in input_text.splitlines()])

def is_guard_in_lab(lab, guard_location):
    rows, cols = lab.shape
    return 0 <= guard_location[0] < rows and 0 <= guard_location[1] < cols

def count_distinct_pos_until_guard_leaves(lab_grid, guard_location):
    visited = set()
    direction = "^"

    moves = {
        "^": (-1, 0),
        "v": (1, 0),
        ">": (0, 1),
        "<": (0, -1),
    }

    while is_guard_in_lab(lab_grid, guard_location):
        row, col = guard_location
        visited.add((row, col))

        dr, dc = moves[direction]
        next_row, next_col = row + dr, col + dc
        max_row, max_col = lab_grid.shape
        if next_row< 0 or next_row >= max_row or next_col < 0 or next_col >= max_col:
            break

        if lab_grid[next_row, next_col] == "#":
            direction = {
                "^": ">",
                ">": "v",
                "v": "<",
                "<": "^",
            }[direction]
        else:
            lab_grid[row, col] = "."
            lab_grid[next_row, next_col] = direction
            guard_location = (next_row, next_col)

    return len(visited)

example_input_file = "einput.txt"
input_file = "input.txt"
lab = read_input(example_input_file)

coordinates = np.where(lab == "^")
location = (int(coordinates[0][0]), int(coordinates[1][0]))

distinct_positions = count_distinct_pos_until_guard_leaves(lab_grid=lab, guard_location=location)
print("Distinct positions visited:", distinct_positions)
