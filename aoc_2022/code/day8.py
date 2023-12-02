import sys
import pathlib

import numpy

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def is_tree_visible(forest, tree_i, tree_j):
    height = len(forest)
    width = len(forest[0])
    tree = forest[tree_i][tree_j]
    # horizontal
    j = 0
    while j < width:
        if j == tree_j:
            return True
        if tree > forest[tree_i][j]:
            j += 1
            continue
        if j < tree_j:
            j = tree_j+1
        elif j > tree_j:
            break
    if j >= width:
        return True
    # vertical
    i = 0
    while i < height:
        if i == tree_i:
            return True
        if tree > forest[i][tree_j]:
            i += 1
            continue
        if i < tree_i:
            i = min(tree_i+1, height-1)
        elif i > tree_i:
            break
    if i >= height:
        return True
    return False


def get_scenic_score(forest, tree_i, tree_j):
    left, right, up, down = 0, 0, 0, 0
    height = len(forest)
    width = len(forest[0])
    tree = forest[tree_i][tree_j]
    # left
    for i in range(tree_i-1, -1, -1):
        left += 1
        if tree <= forest[i][tree_j]:
            break
    # right
    for i in range(tree_i+1, width):
        right += 1
        if tree <= forest[i][tree_j]:
            break
    # up
    for j in range(tree_j-1, -1, -1):
        up += 1
        if tree <= forest[tree_i][j]:
            break
    # down
    for j in range(tree_j+1, height):
        down += 1
        if tree <= forest[tree_i][j]:
            break
    return left * right * up * down


def part_one(data):
    height = len(data)
    width = len(data[0])
    visible_trees = numpy.zeros((width, height), dtype=int)
    for i in range(height):
        for j in range(width):
            if is_tree_visible(data, i, j):
                visible_trees[i][j] = 1

    return numpy.sum(visible_trees)


def part_two(data):
    height = len(data)
    width = len(data[0])
    scenic_scores = numpy.zeros((width, height), dtype=int)
    for i in range(height):
        for j in range(width):
            scenic_scores[i][j] = get_scenic_score(data, i, j)

    return numpy.amax(scenic_scores)


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_2d_array("aoc_2022/data/day8.txt")

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
