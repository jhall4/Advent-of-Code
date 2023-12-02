from aoc_2021.code import DayThree
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = ['00100', '11110', '10110', '10111', '10101', '01111',
             '00111', '11100', '10000', '11001', '00010', '01010']


def test_part_one():
    provided_answer = 198
    assert DayThree.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 230
    assert DayThree.part_two(test_data) == provided_answer
