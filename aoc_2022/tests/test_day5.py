import sys
import pathlib

from aoc_2022.code import day5
from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_part_one():
    test_stacks, test_instructions = data_importer.get_as_stacks_and_moves(
        "aoc_2022/test_data/day5.txt")
    provided_answer = "CMZ"
    assert day5.part_one(test_stacks, test_instructions) == provided_answer


def test_part_two():
    test_stacks, test_instructions = data_importer.get_as_stacks_and_moves(
        "aoc_2022/test_data/day5.txt")
    provided_answer = "MCD"
    assert day5.part_two(test_stacks, test_instructions) == provided_answer
