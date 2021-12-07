# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DaySeven

testData = [16,1,2,0,4,2,7,1,2,14]


def test_PartOne():
    providedAnswer = 37
    assert DaySeven.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 168
    assert DaySeven.PartTwo(testData) == providedAnswer
