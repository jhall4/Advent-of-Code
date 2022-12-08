import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from aoc2021.Code import DayOne

import pytest

testData = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_PartOne():
    providedAnswer = 7
    assert DayOne.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 5
    assert DayOne.PartTwo(testData) == providedAnswer
