import sys
import pathlib

from aoc_2022.code import day6

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_part_one():
    test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    provided_answer = 7
    assert day6.part_one(test_data) == provided_answer


def test_part_two():
    test_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    provided_answer = 19
    assert day6.part_two(test_data) == provided_answer
