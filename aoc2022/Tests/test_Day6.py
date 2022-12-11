import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day6


def test_PartOne():
    testData = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    providedAnswer = 7
    assert Day6.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    providedAnswer = 19
    assert Day6.PartTwo(testData) == providedAnswer
