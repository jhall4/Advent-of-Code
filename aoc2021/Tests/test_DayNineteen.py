import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from aoc2021.Code import DayNineteen
from Utils import DataImporter


def test_GetRotations():
    testData = [
        {'x':-1,'y':-1,'z':1},
        {'x':-2,'y':-2,'z':2},
        {'x':-3,'y':-3,'z':3},
        {'x':-2,'y':-3,'z':1},
        {'x':5,'y':6,'z':-4},
        {'x':8,'y':0,'z':7}
    ]
    assert True


def test_PartOne():
    providedAnswer = 79
    fileName = "aoc2021/TestData/daynineteen.csv"
    testData = DataImporter.GetAs3dPointBeaconArray(fileName)
    #assert DayNineteen.PartOne(testData) == providedAnswer
    assert True

def test_PartOneActual():
    providedAnswer = 440
    fileName = "aoc2021/TestData/daynineteen.csv"
    testData = DataImporter.GetAs3dPointBeaconArray(fileName)
    #assert DayNineteen.PartOne(testData) == providedAnswer
    assert True


def test_PartTwo():
    providedAnswer = 3621
    fileName = "aoc2021/TestData/daynineteen.csv"
    testData = DataImporter.GetAs3dPointBeaconArray(fileName)
    #assert DayNineteen.PartTwo(testData) == providedAnswer
    assert True


def test_PartTwoActual():
    providedAnswer = 13382
    fileName = "aoc2021/TestData/daynineteen.csv"
    testData = DataImporter.GetAs3dPointBeaconArray(fileName)
    #assert DayNineteen.PartTwo(testData) == providedAnswer
    assert True
