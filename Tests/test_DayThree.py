# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayThree


testData = ['00100', '11110', '10110', '10111', '10101', '01111',
            '00111', '11100', '10000', '11001', '00010', '01010']


def test_PartOne():
    providedAnswer = 198
    assert DayThree.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 230
    assert DayThree.PartTwo(testData) == providedAnswer