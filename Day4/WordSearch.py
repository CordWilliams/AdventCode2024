import numpy as np
import re

def read_input():
    with open("input.txt", "r") as file:
        input_text = file.read()

    return np.array([list(line) for line in input_text.splitlines()])

def count_xmas(grid):
    pattern = re.compile("XMAS")
    rev_pattern = re.compile("SAMX")
    count = 0

    #TODO: count the number of XMAS up/down and left/right
    words = grid
    for _ in range(2):
        for line in words:
            count += len(pattern.findall("".join(line)))
            count += len(rev_pattern.findall("".join(line)))

        words = words.transpose()

    #TODO: count the number of XMAS diagonally (left -> right)
    rows, cols = grid.shape
    for i in range(rows):
        line = grid.diagonal(offset=i)
        count += len(pattern.findall("".join(line)))
        count += len(rev_pattern.findall("".join(line)))
    for i in range(1, rows):
        line = grid.diagonal(offset=-i)
        count += len(pattern.findall("".join(line)))
        count += len(rev_pattern.findall("".join(line)))

    # TODO: count the number of XMAS diagonally (right -> left)
    grid = np.fliplr(grid)
    rows, cols = grid.shape
    for i in range(rows):
        line = grid.diagonal(offset=i)
        count += len(pattern.findall("".join(line)))
        count += len(rev_pattern.findall("".join(line)))
    for i in range(1, rows):
        line = grid.diagonal(offset=-i)
        count += len(pattern.findall("".join(line)))
        count += len(rev_pattern.findall("".join(line)))

    return count

def count_x_mas(grid):
    rows, cols = grid.shape
    count = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):

            top_left = grid[i - 1, j - 1]
            bottom_right = grid[i + 1, j + 1]
            top_right = grid[i - 1, j + 1]
            bottom_left = grid[i + 1, j - 1]
            center = grid[i, j]

            if center == "A":
                if (top_left == "M" and bottom_right == "S" and top_right == "S" and bottom_left == "M"):
                    count += 1
                elif (top_left == "S" and bottom_right == "M" and top_right == "S" and bottom_left == "M"):
                    count += 1
                elif (top_left == "S" and bottom_right == "M" and top_right == "M" and bottom_left == "S"):
                    count += 1
                elif (top_left == "M" and bottom_right == "S" and top_right == "M" and bottom_left == "S"):
                    count += 1
    return count

xmas_word_puzzle = read_input()
print(count_xmas(grid=xmas_word_puzzle))
print(count_x_mas(grid=xmas_word_puzzle))
