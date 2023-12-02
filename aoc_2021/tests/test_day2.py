from aoc_2021.code import day2
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = [['forward', 5], ['down', 5], ['forward', 8],
             ['up', 3], ['down', 8], ['forward', 2]]


def test_part_one():
    provided_answer = 150
    assert day2.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 900
    assert day2.part_two(test_data) == provided_answer
