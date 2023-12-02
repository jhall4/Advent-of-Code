import sys
import pathlib

from aoc_2022.code import day2
from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_part_one():
    test_data = data_importer.get_rows_as_array("aoc_2022/test_data/day2.txt")
    provided_answer = 15
    assert day2.part_one(test_data) == provided_answer


def test_part_two():
    test_data = data_importer.get_rows_as_array("aoc_2022/test_data/day2.txt")
    provided_answer = 12
    assert day2.part_two(test_data) == provided_answer
