import sys
import pathlib

from aoc_2022.code import day7
from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_part_one():
    test_data = data_importer.get_rows_as_array("aoc_2022/test_data/day7.txt")
    provided_answer = 95437
    assert day7.part_one(test_data) == provided_answer


def test_part_two():
    test_data = data_importer.get_rows_as_array("aoc_2022/test_data/day7.txt")
    provided_answer = 24933642
    assert day7.part_two(test_data) == provided_answer
