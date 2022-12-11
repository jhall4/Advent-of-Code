import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from aoc2022.Code import Day5


def test_PartOne():
    testStacks, testInstrustions = DataImporter.GetAsStacksAndMoves("aoc2022/TestData/day5.txt")
    providedAnswer = "CMZ"
    assert Day5.PartOne(testStacks, testInstrustions) == providedAnswer


def test_PartTwo():
    testStacks, testInstrustions = DataImporter.GetAsStacksAndMoves("aoc2022/TestData/day5.txt")
    providedAnswer = "MCD"
    assert Day5.PartTwo(testStacks, testInstrustions) == providedAnswer
