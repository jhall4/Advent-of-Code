# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayX

testData = None


def test_PartOne():
    providedAnswer = 0
    assert DayX.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 0
    assert DayX.PartTwo(testData) == providedAnswer
