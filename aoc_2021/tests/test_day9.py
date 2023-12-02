from aoc_2021.code import DayNine
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = [
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
    [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
    [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
    [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
    [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
]


def test_part_one():
    provided_answer = 15
    assert DayNine.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 1134
    assert DayNine.part_two(test_data) == provided_answer
