from aoc_2021.code import DaySeven
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part_one():
    provided_answer = 37
    assert DaySeven.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 168
    assert DaySeven.part_two(test_data) == provided_answer
