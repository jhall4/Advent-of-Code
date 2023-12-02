import sys
import pathlib

from aoc_2022.code import day1
from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_part_one():
    test_data = data_importer.get_new_line_delimited_file_as_2d_int_array(
        "aoc_2022/test_data/day1.txt")
    provided_answer = 24000
    assert day1.part_one(test_data) == provided_answer


def test_part_two():
    test_data = data_importer.get_new_line_delimited_file_as_2d_int_array(
        "aoc_2022/test_data/day1.txt")
    provided_answer = 45000
    assert day1.part_two(test_data) == provided_answer
