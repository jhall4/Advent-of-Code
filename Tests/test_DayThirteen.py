# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayThirteen


testPoints1  = [
    [6,10],
    [0,14],
    [9,10],
    [0,3],
    [10,4],
    [4,11],
    [6,0],
    [6,12],
    [4,1],
    [0,13],
    [10,12],
    [3,4],
    [3,0],
    [8,4],
    [1,10],
    [2,14],
    [8,10],
    [9,0]
]

testPoints2 = [
    [0,0],
    [6,0],
    [1,1],
    [8,1],
    [6,3],
    [3,4],
    [9,4],
    [4,5],
    [5,5]
]

testFolds1 = [
    ['y',7],
    ['x',5]
]

testFolds2 = [
    ['x',5],
    ['y',7]
]


def test1_PartOne():
    providedAnswer = 17
    assert DayThirteen.PartOne(testPoints1, testFolds1) == providedAnswer

def test2_PartOne():
    providedAnswer = 7
    assert DayThirteen.PartOne(testPoints2, testFolds2) == providedAnswer


def test_PartTwo():
    providedAnswer = 0
    assert DayThirteen.PartTwo(testPoints1, testFolds1) == providedAnswer
