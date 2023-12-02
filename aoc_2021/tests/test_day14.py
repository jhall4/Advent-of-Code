from aoc_2021.code import DayFourteen
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


testString = 'NNCB'
testDict = {
    'CH': 'B',
    'HH': 'N',
    'CB': 'H',
    'NH': 'C',
    'HB': 'C',
    'HC': 'B',
    'HN': 'C',
    'NN': 'C',
    'BH': 'H',
    'NC': 'B',
    'NB': 'B',
    'BN': 'B',
    'BB': 'N',
    'BC': 'B',
    'CC': 'N',
    'CN': 'C'
}


def test_part_one():
    provided_answer = 1588
    assert DayFourteen.part_one(testString, testDict) == provided_answer


def test_part_two():
    provided_answer = 2188189693529
    assert DayFourteen.part_two(testString, testDict) == provided_answer
