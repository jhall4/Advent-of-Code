#import sys
#import pathlib
#codeModulePath = pathlib.Path(__file__)
#sys.path[0] = str(codeModulePath)

#import Utils.DataImporter as DataImporter
import DataImporter


##### GetNumbersFromString #####


def test_GetNumbersFromString_IsNotString_EmptyArrayReturned():
    string = 55.5
    numbers = DataImporter.GetNumbersFromString(string)
    assert(numbers == [])


def test_GetNumbersFromString_OneDigitNumber_CorrectNumberReturned():
    num = 4
    string = "test number {} test number".format(num)
    numbers = DataImporter.GetNumbersFromString(string)
    assert(numbers[0] == num)


def test_GetNumbersFromString_TwoDigitNumber_CorrectNumberReturned():
    num = 14
    string = "test number {} test number".format(num)
    numbers = DataImporter.GetNumbersFromString(string)
    assert(numbers[0] == num)


def test_GetNumbersFromString_MultipleNumbers_CorrectNumbersReturned():
    num1 = 4
    num2 = 14
    expectedNumbers = [num1, num2]
    string = "test number {} test number {} test number ".format(num1, num2)
    numbers = DataImporter.GetNumbersFromString(string)
    assert(numbers == expectedNumbers)

##### GetCsvRowsAsArray #####


def test_GetCsvRowsAsArray_FileDoesNotExist_EmptyArrayReturned():
    fileName = "madeUpFile.fake"
    array = DataImporter.GetCsvRowsAsArray(fileName)
    assert (array == [])


def test_GetCsvRowsAsArray_FileExistsAndHasData_ValidArrayReturned():
    fileName = "aoc2021/TestData/tenrowcount.csv"
    array = DataImporter.GetCsvRowsAsArray(fileName)
    assert (len(array) > 0)


def test_GetCsvRowsAsArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    fileName = "aoc2021/TestData/tenrowcount.csv"
    array = DataImporter.GetCsvRowsAsArray(fileName)
    assert (array == expectedArray)


def test_GetCsvRowsAsArray_DayTenFile_CorrectArrayReturned():
    expectedArray = [
        r"[({(<(())[]>[[{[]{<()<>>",
        r"[(()[<>])]({[<{<<[]>>(",
        r"{([(<{}[<>[]}>{[]{[(<()>",
        r"(((({<>}<{<{<>}{[]{[]{}",
        r"[[<[([]))<([[{}[[()]]]",
        r"[{[{({}]{}}([{[{{{}}([]",
        r"{<[[]]>}<{[{[{[]{()[[[]",
        r"[<(<(<(<{}))><([]([]()",
        r"<{([([[(<>()){}]>(<<{{",
        r"<{([{{}}[<[[[<>{}]]]>[]]"
    ]
    fileName = "aoc2021/TestData/dayten.csv"
    array = DataImporter.GetCsvRowsAsArray(fileName)
    assert (array == expectedArray)


def test_GetCsvRowsAsArray_DatTwelveFile_CorrectArrayReturned():
    expectedArray = [
        'start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end',
    ]
    fileName = "aoc2021/TestData/daytwelve.csv"
    array = DataImporter.GetCsvRowsAsArray(fileName)
    assert (array == expectedArray)


##### GetCsvAsArray #####


def test_GetCsvAsArray_FileDoesNotExist_EmptyArrayReturned():
    fileName = "madeUpFile.fake"
    array = DataImporter.GetCsvAsArray(fileName)
    assert (array == [])


def test_GetCsvAsArray_FileExistsAndHasData_ValidArrayReturned():
    fileName = "aoc2021/TestData/dayfour_calls.csv"
    array = DataImporter.GetCsvAsArray(fileName)
    assert (len(array) > 0)


def test_GetCsvAsArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                     10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    fileName = "aoc2021/TestData/dayfour_calls.csv"
    array = DataImporter.GetCsvAsArray(fileName)
    assert (array == expectedArray)


##### GetCsvAs3dArray #####


def test_GetCsvAs3dArray_FileDoesNotExist_EmptyArrayReturned():
    fileName = "madeUpFile.fake"
    array = DataImporter.GetCsvAs3dArray(fileName)
    assert (array == [])


def test_GetCsvAs3dArray_FileExistsAndHasData_ValidArrayReturned():
    fileName = "aoc2021/TestData/dayfour_boards.csv"
    array = DataImporter.GetCsvAs3dArray(fileName)
    assert (len(array) > 0)


def test_GetCsvAs3dArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6]
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7]
        ]
    ]

    fileName = "aoc2021/TestData/dayfour_boards.csv"
    array = DataImporter.GetCsvAs3dArray(fileName)
    assert (array == expectedArray)


##### GetAsStartEndPointArray #####


def test_GetAsStartEndPointArray_FileDoesNotExist_EmptyArrayReturned():
    fileName = "madeUpFile.fake"
    array = DataImporter.GetAsStartEndPointArray(fileName)
    assert (array == [])


def test_GetAsStartEndPointArray_FileExistsAndHasData_ValidArrayReturned():
    fileName = "aoc2021/TestData/dayfive.csv"
    array = DataImporter.GetAsStartEndPointArray(fileName)
    assert (len(array) > 0)


def test_GetAsStartEndPointArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = [
        [[0, 9], [5, 9]],
        [[8, 0], [0, 8]],
        [[9, 4], [3, 4]],
        [[2, 2], [2, 1]],
        [[7, 0], [7, 4]],
        [[6, 4], [2, 0]],
        [[0, 9], [2, 9]],
        [[3, 4], [1, 4]],
        [[0, 0], [8, 8]],
        [[5, 5], [8, 2]]
    ]
    fileName = "aoc2021/TestData/dayfive.csv"
    array = DataImporter.GetAsStartEndPointArray(fileName)
    assert (array == expectedArray)


def test_GetAsDisplaySegmentArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = [
        {DataImporter.signalValues: ["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd",
                                     "fecdb", "fabcd", "edb"], DataImporter.outputValue: ["fdgacbe", "cefdb", "cefbgd", "gcbe"]},
        {DataImporter.signalValues: ["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd",
                                     "abcde", "gfcbed", "gfec"], DataImporter.outputValue: ["fcgedb", "cgb", "dgebacf", "gc"]},
        {DataImporter.signalValues: ["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad",
                                     "gfac", "gcb", "cdgabef"], DataImporter.outputValue: ["cg", "cg", "fdcagb", "cbg"]},
        {DataImporter.signalValues: ["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc",
                                     "ecdab", "fgdeca", "fcdbega"], DataImporter.outputValue: ["efabcd", "cedba", "gadfec", "cb"]},
        {DataImporter.signalValues: ["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea",
                                     "fcaegb", "dgceab", "fcbdga"], DataImporter.outputValue: ["gecf", "egdcabf", "bgf", "bfgea"]},
        {DataImporter.signalValues: ["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec",
                                     "bfadeg", "bafgc", "acf"], DataImporter.outputValue: ["gebdcfa", "ecba", "ca", "fadegcb"]},
        {DataImporter.signalValues: ["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc",
                                     "dacgb", "gdcebf", "gf"], DataImporter.outputValue: ["cefg", "dcbef", "fcge", "gbcadfe"]},
        {DataImporter.signalValues: ["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf",
                                     "ced", "adcbefg", "gebcd"], DataImporter.outputValue: ["ed", "bcgafe", "cdgba", "cbgef"]},
        {DataImporter.signalValues: ["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg",
                                     "fgcdab", "egfdb", "bfceg"], DataImporter.outputValue: ["gbdfcae", "bgc", "cg", "cgb"]},
        {DataImporter.signalValues: ["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef",
                                     "cafbge", "fdbac", "fegbdc"], DataImporter.outputValue: ["fgae", "cfgab", "fg", "bagce"]}

    ]
    fileName = "aoc2021/TestData/dayeight.csv"
    array = DataImporter.GetAsDisplaySegmentArray(fileName)
    assert (array == expectedArray)


def test_GetAs2dArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = testData = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
    ]
    fileName = "aoc2021/TestData/daynine.csv"
    array = DataImporter.GetAs2dArray(fileName)
    assert (array == expectedArray)


def test_GetAs2dArray_DayElevenFile_CorrectArrayReturned():
    expectedArray = [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]
    ]
    fileName = "aoc2021/TestData/dayeleven.csv"
    array = DataImporter.GetAs2dArray(fileName)
    assert (array == expectedArray)


def test_GetAs2dArray_DayFifteenFile_CorrectArrayReturned():
    expectedArray = [
        [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
        [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
        [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
        [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
        [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
        [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
        [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
        [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
        [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
        [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
    ]
    fileName = "aoc2021/TestData/dayfifteen.csv"
    array = DataImporter.GetAs2dArray(fileName)
    assert (array == expectedArray)

    ##### GetAsPointsAndFolds #####


def test_GetAsPointsAndFolds_DayThirteenFile_CorrectArrayReturned():
    expectedPoints = [
        [6, 10],
        [0, 14],
        [9, 10],
        [0, 3],
        [10, 4],
        [4, 11],
        [6, 0],
        [6, 12],
        [4, 1],
        [0, 13],
        [10, 12],
        [3, 4],
        [3, 0],
        [8, 4],
        [1, 10],
        [2, 14],
        [8, 10],
        [9, 0]
    ]
    expectedFolds = [
        ['y', 7],
        ['x', 5]
    ]

    fileName = "aoc2021/TestData/daythirteen.csv"
    points, folds = DataImporter.GetAsPointsAndFolds(fileName)
    assert points == expectedPoints
    assert folds == expectedFolds


##### GetAsStringAndDict #####

def test_GetAsStringAndDict_DayFourteenFile_CorrectValuesReturned():
    expectedString = 'NNCB'
    expectedDict = {
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
    fileName = "aoc2021/TestData/dayfourteen.csv"
    string, dict = DataImporter.GetAsStringAndDict(fileName)
    assert string == expectedString
    assert dict == expectedDict

    ##### GetStringBetween #####


def test_GetStringBetween_IsNotString_EmptyStringReturned():
    string, left, right = 1, 2, 3
    assert DataImporter.GetStringBetween(string, left, right) == ""


def test_GetStringBetween_LeftNotInStringRightIs_StringUpToRightReturned():
    expected = 'hello th'
    left = 'test'
    right = 'ere'
    string = expected + right
    assert DataImporter.GetStringBetween(string, left, right) == expected


def test_GetStringBetween_LeftInStringRightNot_StringLeftToEndReturned():
    expected = 'lo there'
    left = 'hel'
    right = 'test'
    string = left + expected
    assert DataImporter.GetStringBetween(string, left, right) == expected


def test_GetStringBetween_NeitherInString_EmptyStringReturned():
    left = 'test'
    right = 'test'
    string = 'hello there'
    assert DataImporter.GetStringBetween(string, left, right) == ''


##### GetAsRect #####


def test_GetAsRect_DaySeventeenFile():
    expectedRect = {
        'topLeft': {'x': 20, 'y': -5},
        'bottomRight': {'x': 30, 'y': -10}
    }
    fileName = "aoc2021/TestData/dayseventeen.csv"
    rect = DataImporter.GetAsRect(fileName)
    assert rect == expectedRect


##### GetAsList #####

def test_GetAsList_DayEighteenFile():
    expectedList = [
        [1, 2],
        [[1, 2], 3],
        [9, [8, 7]],
        [[1, 9], [8, 5]],
        [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9],
        [[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]],
        [[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [
            [[4, 9], [6, 9]], [[8, 2], [7, 3]]]]
    ]
    fileName = "aoc2021/TestData/dayeighteen.csv"
    list = DataImporter.GetAsList(fileName)
    assert list == expectedList


##### GetAs3dPointBeaconArray #####


def test_GetAs3dPointBeaconArray_DayNineteenSmallFile():
    expectedList = [
        [
            {'x':404,'y':-588,'z':-901},
            {'x':528,'y':-643,'z':409},
            {'x':-838,'y':591,'z':734}
        ],
        [
            {'x':686,'y':422,'z':578},
            {'x':605,'y':423,'z':415},
            {'x':515,'y':917,'z':-361}
        ],
        [
            {'x':649,'y':640,'z':665},
            {'x':682,'y':-795,'z':504},
            {'x':-784,'y':533,'z':-524}
        ]
    ]
    fileName = "aoc2021/TestData/daynineteensmall.csv"
    list = DataImporter.GetAs3dPointBeaconArray(fileName)
    assert list == expectedList


##### GetNewLineDelimitedFileAs2dIntArray #####



def test_GetNewLineDelimitedFileAs2dIntArray_Day1TestFile():
    expectedList = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000]
    ]
    fileName = "aoc2022/TestData/day1.txt"
    list = DataImporter.GetNewLineDelimitedFileAs2dIntArray(fileName)
    assert list == expectedList