import sys
import pathlib

from aoc_2022.code import day4
from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_part_one():
    test_data = data_importer.get_as_multidimensional_array(
        "aoc_2022/test_data/day4.txt", '\n', ',', '-')
    provided_answer = 2
    assert day4.part_one(test_data) == provided_answer


def test_part_two():
    test_data = data_importer.get_as_multidimensional_array(
        "aoc_2022/test_data/day4.txt", '\n', ',', '-')
    provided_answer = 4
    assert day4.part_two(test_data) == provided_answer
