from aoc_2021.code import DayEighteen
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = None


def test_ExplodeNumbers1():
    test_data = [[[[[9, 8], 1], 2], 3], 4]
    expectedNumber = [[[[0, 9], 2], 3], 4]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(test_data)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers2():
    test_data = [7, [6, [5, [4, [3, 2]]]]]
    expectedNumber = [7, [6, [5, [7, 0]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(test_data)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers3():
    test_data = [[6, [5, [4, [3, 2]]]], 1]
    expectedNumber = [[6, [5, [7, 0]]], 3]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(test_data)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers4():
    test_data = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
    expectedNumber = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(test_data)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers5():
    test_data = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
    expectedNumber = [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(test_data)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers6():
    test_data = [[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]],
                 [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
    expectedNumber = [[[[4, 0], [5, 4]], [[0, [7, 6]], [9, 5]]], [
        7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(test_data)
    assert explodedNumber == expectedNumber


def test_SplitNumbers():
    test_data = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    expectedNumber = [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    splitNumber, _ = DayEighteen.SplitNumbers(test_data)
    assert splitNumber == expectedNumber


def test_AddNumbers1():
    test_dataA = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
    test_dataB = [1, 1]
    # expectedNumber = [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    expectedNumber = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    addedNumber = DayEighteen.AddNumbers(test_dataA, test_dataB)
    assert addedNumber == expectedNumber


def test_AddNumbers2():
    test_dataA = [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]]
    test_dataB = [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]
    expectedResult = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]],
                      [[8, [7, 7]], [[7, 9], [5, 0]]]]
    addedNumber = DayEighteen.AddNumbers(test_dataA, test_dataB)
    assert addedNumber == expectedResult


def test_GetMagnitude1():
    test_data = [[1, 2], [[3, 4], 5]]
    expectedResult = 143
    assert DayEighteen.GetMagnitude(test_data) == expectedResult


def test_GetMagnitude2():
    test_data = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    expectedResult = 1384
    assert DayEighteen.GetMagnitude(test_data) == expectedResult


def test_GetMagnitude3():
    test_data = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]],
                 [[[0, 7], [6, 6]], [8, 7]]]
    expectedResult = 3488
    assert DayEighteen.GetMagnitude(test_data) == expectedResult


def test_part_oneSmall():
    test_data = [
        [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
        [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]
    ]
    expectedResult = DayEighteen.GetMagnitude(
        [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]])
    assert DayEighteen.part_one(test_data) == expectedResult


def test_part_oneBig():
    test_data = [
        [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
        [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
        [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
        [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
        [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
        [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
        [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
        [[9, 3], [[9, 9], [6, [4, 9]]]],
        [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
        [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]]
    ]
    provided_answer = 4140
    assert DayEighteen.part_one(test_data) == provided_answer


def test_part_two():
    test_data = [
        [[[0, [5, 8]], [[1, 7], [9, 6]]], [[4, [1, 2]], [[1, 4], 2]]],
        [[[5, [2, 8]], 4], [5, [[9, 9], 0]]],
        [6, [[[6, 2], [5, 6]], [[7, 6], [4, 7]]]],
        [[[6, [0, 7]], [0, 9]], [4, [9, [9, 0]]]],
        [[[7, [6, 4]], [3, [1, 3]]], [[[5, 5], 1], 9]],
        [[6, [[7, 3], [3, 2]]], [[[3, 8], [5, 7]], 4]],
        [[[[5, 4], [7, 7]], 8], [[8, 3], 8]],
        [[9, 3], [[9, 9], [6, [4, 9]]]],
        [[2, [[7, 7], 7]], [[5, 8], [[9, 3], [0, 2]]]],
        [[[[5, 2], 5], [8, [3, 7]]], [[5, [7, 5]], [4, 4]]]
    ]
    provided_answer = 3993
    assert DayEighteen.part_two(test_data) == provided_answer
