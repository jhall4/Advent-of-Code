from aoc_2021.code import DaySeventeen
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = {
    'top_left': {'x': 20, 'y': -5},
    'bottom_right': {'x': 30, 'y': -10}
}


def test_part_one():
    provided_answer = 45
    assert DaySeventeen.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 112
    assert DaySeventeen.part_two(test_data) == provided_answer
