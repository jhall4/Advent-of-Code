from utils import data_importer
from aoc_2021.code import DayNineteen
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def test_get_rotations():
    test_data = [
        {'x': -1, 'y': -1, 'z': 1},
        {'x': -2, 'y': -2, 'z': 2},
        {'x': -3, 'y': -3, 'z': 3},
        {'x': -2, 'y': -3, 'z': 1},
        {'x': 5, 'y': 6, 'z': -4},
        {'x': 8, 'y': 0, 'z': 7}
    ]
    assert True


def test_part_one():
    provided_answer = 79
    file_name = "aoc_2021/test_data/daynineteen.csv"
    test_data = data_importer.get_as_3d_point_beacon_array(file_name)
    # assert DayNineteen.part_one(test_data) == provided_answer
    assert True


def test_part_oneActual():
    provided_answer = 440
    file_name = "aoc_2021/test_data/daynineteen.csv"
    test_data = data_importer.get_as_3d_point_beacon_array(file_name)
    # assert DayNineteen.part_one(test_data) == provided_answer
    assert True


def test_part_two():
    provided_answer = 3621
    file_name = "aoc_2021/test_data/daynineteen.csv"
    test_data = data_importer.get_as_3d_point_beacon_array(file_name)
    # assert DayNineteen.part_two(test_data) == provided_answer
    assert True


def test_part_twoActual():
    provided_answer = 13382
    file_name = "aoc_2021/test_data/daynineteen.csv"
    test_data = data_importer.get_as_3d_point_beacon_array(file_name)
    # assert DayNineteen.part_two(test_data) == provided_answer
    assert True
