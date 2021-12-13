# make tests think they're running in code module
import DayTwelve
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)


testData1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

testData2 = [
    'dc-end',
    'HN-start',
    'start-kj',
    'dc-start',
    'dc-HN',
    'LN-dc',
    'HN-end',
    'kj-sa',
    'kj-HN',
    'kj-dc',
]

testData3 = [
    'fs-end',
    'he-DX',
    'fs-he',
    'start-DX',
    'pj-DX',
    'end-zg',
    'zg-sl',
    'zg-pj',
    'pj-he',
    'RW-he',
    'fs-DX',
    'pj-RW',
    'zg-RW',
    'start-pj',
    'he-WI',
    'zg-he',
    'pj-fs',
    'start-RW'
]


def test1_PartOne():
    providedAnswer = 10
    assert DayTwelve.PartOne(testData1) == providedAnswer


def test2_PartOne():
    providedAnswer = 19
    assert DayTwelve.PartOne(testData2) == providedAnswer


def test3_PartOne():
    providedAnswer = 226
    assert DayTwelve.PartOne(testData3) == providedAnswer


def test1_PartTwo():
    providedAnswer = 36
    assert DayTwelve.PartTwo(testData1) == providedAnswer


def test2_PartTwo():
    providedAnswer = 103
    assert DayTwelve.PartTwo(testData2) == providedAnswer


def test3_PartTwo():
    providedAnswer = 3509
    assert DayTwelve.PartTwo(testData3) == providedAnswer
