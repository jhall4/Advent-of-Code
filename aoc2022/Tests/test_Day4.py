import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day4


def test_PartOne():
    testData = DataImporter.GetAsMultiDimensionalArray("aoc2022/TestData/day4.txt", '\n', ',', '-')
    providedAnswer = 2
    assert Day4.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = DataImporter.GetAsMultiDimensionalArray("aoc2022/TestData/day4.txt", '\n', ',', '-')
    providedAnswer = 4
    assert Day4.PartTwo(testData) == providedAnswer
