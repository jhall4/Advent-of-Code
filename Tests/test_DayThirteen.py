# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayThirteen


testPoints  = [
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

testFolds = [
    ['y',7],
    ['x',5]
]


def test_PartOne():
    providedAnswer = 17
    assert DayThirteen.PartOne(testPoints, testFolds) == providedAnswer
