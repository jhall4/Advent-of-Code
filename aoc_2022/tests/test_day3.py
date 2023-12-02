import sys
import pathlib

from aoc_2022.code import day3
from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_get_priority_lowercase_a():
    assert 1 == day3.get_priority('a')


def test_get_priority_uppercase_a():
    assert 27 == day3.get_priority('A')


def test_part_one():
    test_data = data_importer.get_rows_as_array("aoc_2022/test_data/day3.txt")
    provided_answer = 157
    assert day3.part_one(test_data) == provided_answer


def test_part_two():
    test_data = data_importer.get_rows_as_array("aoc_2022/test_data/day3.txt")
    provided_answer = 70
    assert day3.part_two(test_data) == provided_answer
