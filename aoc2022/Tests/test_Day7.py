import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day7


def test_PartOne():
    testData = DataImporter.GetCsvRowsAsArray("aoc2022/TestData/day7.txt")
    providedAnswer = 95437
    assert Day7.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = DataImporter.GetCsvRowsAsArray("aoc2022/TestData/day7.txt")
    providedAnswer = 24933642
    assert Day7.PartTwo(testData) == providedAnswer
