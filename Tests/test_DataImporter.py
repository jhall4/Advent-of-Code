from Code.Utils import DataImporter


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
    fileName = "TestData/tenrowcount.csv"
    array = DataImporter.GetCsvRowsAsArray(fileName)
    assert (len(array) > 0)


def test_GetCsvRowsAsArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    fileName = "TestData/tenrowcount.csv"
    array = DataImporter.GetCsvRowsAsArray(fileName)
    assert (array == expectedArray)


##### GetCsvAsArray #####


def test_GetCsvAsArray_FileDoesNotExist_EmptyArrayReturned():
    fileName = "madeUpFile.fake"
    array = DataImporter.GetCsvAsArray(fileName)
    assert (array == [])


def test_GetCsvAsArray_FileExistsAndHasData_ValidArrayReturned():
    fileName = "TestData/dayfour_calls.csv"
    array = DataImporter.GetCsvAsArray(fileName)
    assert (len(array) > 0)


def test_GetCsvAsArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    fileName = "TestData/dayfour_calls.csv"
    array = DataImporter.GetCsvAsArray(fileName)
    assert (array == expectedArray)


##### GetCsvAs3dArray #####


def test_GetCsvAs3dArray_FileDoesNotExist_EmptyArrayReturned():
    fileName = "madeUpFile.fake"
    array = DataImporter.GetCsvAs3dArray(fileName)
    assert (array == [])


def test_GetCsvAs3dArray_FileExistsAndHasData_ValidArrayReturned():
    fileName = "TestData/dayfour_boards.csv"
    array = DataImporter.GetCsvAs3dArray(fileName)
    assert (len(array) > 0)


def test_GetCsvAs3dArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = [
        [
            [22,13,17,11, 0],
            [ 8, 2,23, 4,24],
            [21, 9,14,16, 7],
            [ 6,10, 3,18, 5],
            [ 1,12,20,15,19]
        ],
        [
            [3,15, 0, 2,22],
            [ 9,18,13,17, 5],
            [19, 8, 7,25,23],
            [20,11,10,24, 4],
            [14,21,16,12, 6]
        ],
        [
            [14,21,17,24, 4],
            [10,16,15, 9,19],
            [18, 8,23,26,20],
            [22,11,13, 6, 5],
            [ 2, 0,12, 3, 7]
        ]
    ]

    fileName = "TestData/dayfour_boards.csv"
    array = DataImporter.GetCsvAs3dArray(fileName)
    assert (array == expectedArray)


##### GetAsStartEndPointArray #####


def test_GetAsStartEndPointArray_FileDoesNotExist_EmptyArrayReturned():
    fileName = "madeUpFile.fake"
    array = DataImporter.GetAsStartEndPointArray(fileName)
    assert (array == [])


def test_GetAsStartEndPointArray_FileExistsAndHasData_ValidArrayReturned():
    fileName = "TestData/dayfive.csv"
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
    fileName = "TestData/dayfive.csv"
    array = DataImporter.GetAsStartEndPointArray(fileName)
    assert (array == expectedArray)

def test_GetAsDisplaySegmentArray_FileExistsAndHasData_CorrectArrayReturned():
    expectedArray = [
        {DataImporter.signalValues : ["be","cfbegad","cbdgef","fgaecd","cgeb","fdcge","agebfd","fecdb","fabcd","edb"], DataImporter.outputValue : ["fdgacbe","cefdb","cefbgd","gcbe"]},
        {DataImporter.signalValues : ["edbfga","begcd","cbg","gc","gcadebf","fbgde","acbgfd","abcde","gfcbed","gfec"], DataImporter.outputValue : ["fcgedb","cgb","dgebacf","gc"]},
        {DataImporter.signalValues : ["fgaebd","cg","bdaec","gdafb","agbcfd","gdcbef","bgcad","gfac","gcb","cdgabef"], DataImporter.outputValue : ["cg","cg","fdcagb","cbg"]},
        {DataImporter.signalValues : ["fbegcd","cbd","adcefb","dageb","afcb","bc","aefdc","ecdab","fgdeca","fcdbega"], DataImporter.outputValue : ["efabcd","cedba","gadfec","cb"]},
        {DataImporter.signalValues : ["aecbfdg","fbg","gf","bafeg","dbefa","fcge","gcbea","fcaegb","dgceab","fcbdga"], DataImporter.outputValue : ["gecf","egdcabf","bgf","bfgea"]},
        {DataImporter.signalValues : ["fgeab","ca","afcebg","bdacfeg","cfaedg","gcfdb","baec","bfadeg","bafgc","acf"], DataImporter.outputValue : ["gebdcfa","ecba","ca","fadegcb"]},
        {DataImporter.signalValues : ["dbcfg","fgd","bdegcaf","fgec","aegbdf","ecdfab","fbedc","dacgb","gdcebf","gf"], DataImporter.outputValue : ["cefg","dcbef","fcge","gbcadfe"]},
        {DataImporter.signalValues : ["bdfegc","cbegaf","gecbf","dfcage","bdacg","ed","bedf","ced","adcbefg","gebcd"], DataImporter.outputValue : ["ed","bcgafe","cdgba","cbgef"]},
        {DataImporter.signalValues : ["egadfb","cdbfeg","cegd","fecab","cgb","gbdefca","cg","fgcdab","egfdb","bfceg"], DataImporter.outputValue : ["gbdfcae","bgc","cg","cgb"]},
        {DataImporter.signalValues : ["gcafb","gcf","dcaebfg","ecagb","gf","abcdeg","gaef","cafbge","fdbac","fegbdc"], DataImporter.outputValue : ["fgae","cfgab","fg","bagce"]}

    ]
    fileName = "TestData/dayeight.csv"
    array = DataImporter.GetAsDisplaySegmentArray(fileName)
    assert (array == expectedArray)