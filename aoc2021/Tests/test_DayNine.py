import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from aoc2021.Code import DayNine

testData = [
    [2,1,9,9,9,4,3,2,1,0],
    [3,9,8,7,8,9,4,9,2,1],
    [9,8,5,6,7,8,9,8,9,2],
    [8,7,6,7,8,9,6,7,8,9],
    [9,8,9,9,9,6,5,6,7,8]
]


def test_PartOne():
    providedAnswer = 15
    assert DayNine.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 1134
    assert DayNine.PartTwo(testData) == providedAnswer
