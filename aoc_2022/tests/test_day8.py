import sys
import pathlib

from aoc_2022.code import day8
from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_part_one():
    test_data = data_importer.get_as_2d_array("aoc_2022/test_data/day8.txt")
    provided_answer = 21
    assert day8.part_one(test_data) == provided_answer


def test_part_two():
    test_data = data_importer.get_as_2d_array("aoc_2022/test_data/day8.txt")
    provided_answer = 8
    assert day8.part_two(test_data) == provided_answer
