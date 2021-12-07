# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayTwo


testData = [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]


def test_PartOne():
    providedAnswer = 150
    assert DayTwo.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 900
    assert DayTwo.PartTwo(testData) == providedAnswer
