import numpy as np
import re

def read_input():
    with open("input.txt", "r") as file:
        input_text = file.read()

    return np.array([list(line) for line in input_text.splitlines()])

def count_word_occurrences(grid):
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

xmas_word_puzzle = read_input()
print(count_word_occurrences(grid=xmas_word_puzzle))
