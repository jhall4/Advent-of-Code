# make tests think they're running in code module
import DaySeventeen
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)


testData = {
    'topLeft': {'x': 20, 'y': -5},
    'bottomRight': {'x': 30, 'y': -10}
}


def test_PartOne():
    providedAnswer = 45
    assert DaySeventeen.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 112
    assert DaySeventeen.PartTwo(testData) == providedAnswer
