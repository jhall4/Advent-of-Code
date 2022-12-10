import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day2


def test_PartOne():
    testData = DataImporter.GetCsvRowsAsArray("aoc2022/TestData/day2.txt")
    providedAnswer = 15
    assert Day2.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = DataImporter.GetCsvRowsAsArray("aoc2022/TestData/day2.txt")
    providedAnswer = 12
    assert Day2.PartTwo(testData) == providedAnswer
