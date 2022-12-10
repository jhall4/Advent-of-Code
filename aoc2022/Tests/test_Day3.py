import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day3


def test_GetPriority_a():
    assert 1 == Day3.GetPriority('a')

def test_GetPriority_A():
    assert 27 == Day3.GetPriority('A')


def test_PartOne():
    testData = DataImporter.GetCsvRowsAsArray("aoc2022/TestData/day3.txt")
    providedAnswer = 157
    assert Day3.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = DataImporter.GetCsvRowsAsArray("aoc2022/TestData/day3.txt")
    providedAnswer = 70
    assert Day3.PartTwo(testData) == providedAnswer
