from aoc_2021.code import DaySix
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = [3, 4, 3, 1, 2]


def test_part_one():
    provided_answer = 5934
    assert DaySix.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 26984457539
    assert DaySix.part_two(test_data) == provided_answer
