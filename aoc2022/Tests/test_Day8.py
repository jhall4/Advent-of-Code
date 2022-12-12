import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day8


def test_PartOne():
    testData = DataImporter.GetAs2dArray("aoc2022/TestData/day8.txt")
    providedAnswer = 21
    assert Day8.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = DataImporter.GetAs2dArray("aoc2022/TestData/day8.txt")
    providedAnswer = 8
    assert Day8.PartTwo(testData) == providedAnswer
