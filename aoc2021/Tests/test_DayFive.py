import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from aoc2021.Code import DayFive


testData = [
        [[0, 9], [5, 9]],
        [[8, 0], [0, 8]],
        [[9, 4], [3, 4]],
        [[2, 2], [2, 1]],
        [[7, 0], [7, 4]],
        [[6, 4], [2, 0]],
        [[0, 9], [2, 9]],
        [[3, 4], [1, 4]],
        [[0, 0], [8, 8]],
        [[5, 5], [8, 2]]
    ]

def test_PartOne():
    providedAnswer = 5
    assert DayFive.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 12
    assert DayFive.PartTwo(testData) == providedAnswer
