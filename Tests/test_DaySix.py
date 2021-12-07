# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DaySix

testData = [3,4,3,1,2]


def test_PartOne():
    providedAnswer = 5934
    assert DaySix.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 26984457539
    assert DaySix.PartTwo(testData) == providedAnswer
