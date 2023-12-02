import sys
import pathlib

from aoc_2021.code import day1

codeModulePath = pathlib.Path(__file__).parent.parent.parent

sys.path[0] = str(codeModulePath)


test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_one():
    provided_answer = 7
    assert day1.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 5
    assert day1.part_two(test_data) == provided_answer
