import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day1


def test_PartOne():
    testData = DataImporter.GetNewLineDelimitedFileAs2dIntArray("aoc2022/TestData/day1.txt")
    providedAnswer = 24000
    assert Day1.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = DataImporter.GetNewLineDelimitedFileAs2dIntArray("aoc2022/TestData/day1.txt")
    providedAnswer = 45000
    assert Day1.PartTwo(testData) == providedAnswer
