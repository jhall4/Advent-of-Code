from aoc_2021.code import DayTwelve
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

test_data2 = [
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

test_data3 = [
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


def test1_part_one():
    provided_answer = 10
    assert DayTwelve.part_one(test_data1) == provided_answer


def test2_part_one():
    provided_answer = 19
    assert DayTwelve.part_one(test_data2) == provided_answer


def test3_part_one():
    provided_answer = 226
    assert DayTwelve.part_one(test_data3) == provided_answer


def test1_part_two():
    provided_answer = 36
    assert DayTwelve.part_two(test_data1) == provided_answer


def test2_part_two():
    provided_answer = 103
    assert DayTwelve.part_two(test_data2) == provided_answer


def test3_part_two():
    provided_answer = 3509
    assert DayTwelve.part_two(test_data3) == provided_answer
