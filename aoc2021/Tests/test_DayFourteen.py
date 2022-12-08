import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from aoc2021.Code import DayFourteen


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


def test_PartOne():
    providedAnswer = 1588
    assert DayFourteen.PartOne(testString, testDict) == providedAnswer


def test_PartTwo():
    providedAnswer = 2188189693529
    assert DayFourteen.PartTwo(testString, testDict) == providedAnswer
