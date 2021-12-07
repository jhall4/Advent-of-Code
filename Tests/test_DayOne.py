# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayOne

testData = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_PartOne():
    providedAnswer = 7
    assert DayOne.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 5
    assert DayOne.PartTwo(testData) == providedAnswer
