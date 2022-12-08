import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from aoc2021.Code import DayEighteen


testData = None


def test_ExplodeNumbers1():
    testData = [[[[[9, 8], 1], 2], 3], 4]
    expectedNumber = [[[[0, 9], 2], 3], 4]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(testData)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers2():
    testData = [7, [6, [5, [4, [3, 2]]]]]
    expectedNumber = [7, [6, [5, [7, 0]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(testData)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers3():
    testData = [[6, [5, [4, [3, 2]]]], 1]
    expectedNumber = [[6, [5, [7, 0]]], 3]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(testData)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers4():
    testData = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
    expectedNumber = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(testData)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers5():
    testData = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
    expectedNumber = [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(testData)
    assert explodedNumber == expectedNumber


def test_ExplodeNumbers6():
    testData = [[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]],
                [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
    expectedNumber = [[[[4, 0], [5, 4]], [[0, [7, 6]], [9, 5]]], [
        7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
    explodedNumber, _, _ = DayEighteen.ExplodeNumbers(testData)
    assert explodedNumber == expectedNumber


def test_SplitNumbers():
    testData = [[[[0, 7], 4], [15, [0, 13]]], [1, 1]]
    expectedNumber = [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
    splitNumber, _ = DayEighteen.SplitNumbers(testData)
    assert splitNumber == expectedNumber


def test_AddNumbers1():
    testDataA = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
    testDataB = [1, 1]
    #expectedNumber = [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    expectedNumber = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    addedNumber = DayEighteen.AddNumbers(testDataA, testDataB)
    assert addedNumber == expectedNumber


def test_AddNumbers2():
    testDataA = [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]]
    testDataB = [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]
    expectedResult = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]],
                      [[8, [7, 7]], [[7, 9], [5, 0]]]]
    addedNumber = DayEighteen.AddNumbers(testDataA, testDataB)
    assert addedNumber == expectedResult


def test_GetMagnitude1():
    testData = [[1, 2], [[3, 4], 5]]
    expectedResult = 143
    assert DayEighteen.GetMagnitude(testData) == expectedResult


def test_GetMagnitude2():
    testData = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
    expectedResult = 1384
    assert DayEighteen.GetMagnitude(testData) == expectedResult


def test_GetMagnitude3():
    testData = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]],
                [[[0, 7], [6, 6]], [8, 7]]]
    expectedResult = 3488
    assert DayEighteen.GetMagnitude(testData) == expectedResult


def test_PartOneSmall():
    testData = [
        [[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
        [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]
    ]
    expectedResult = DayEighteen.GetMagnitude(
        [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]])
    assert DayEighteen.PartOne(testData) == expectedResult


def test_PartOneBig():
    testData = [
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
    providedAnswer = 4140
    assert DayEighteen.PartOne(testData) == providedAnswer


def test_PartTwo():
    testData = [
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
    providedAnswer = 3993
    assert DayEighteen.PartTwo(testData) == providedAnswer
