# import sys
# import pathlib
# codeModulePath = pathlib.Path(__file__)
# sys.path[0] = str(codeModulePath)

# import utils.data_importer as data_importer
import data_importer


##### get_numbers_from_string #####


def test_get_numbers_from_string_is_not_string_empty_array_returned():
    string = 55.5
    numbers = data_importer.get_numbers_from_string(string)
    assert numbers == []


def test_get_numbers_from_string_one_digit_number_correct_number_returned():
    num = 4
    string = f"test number {num} test number"
    numbers = data_importer.get_numbers_from_string(string)
    assert numbers[0] == num


def test_get_numbers_from_string_two_digit_number_correct_number_returned():
    num = 14
    string = f"test number {num} test number"
    numbers = data_importer.get_numbers_from_string(string)
    assert numbers[0] == num


def test_get_numbers_from_string_multiple_numbers_correct_numbers_returned():
    num1 = 4
    num2 = 14
    expected_numbers = [num1, num2]
    string = f"test number {num1} test number {num2} test number "
    numbers = data_importer.get_numbers_from_string(string)
    assert numbers == expected_numbers


##### get_rows_as_array #####


def test_get_rows_as_array_file_does_not_exist_empty_array_returned():
    file_name = "madeUpFile.fake"
    array = data_importer.get_rows_as_array(file_name)
    assert not array


def test_get_rows_as_array_file_exists_and_has_data_valid_array_returned():
    file_name = "aoc_2021/test_data/tenrowcount.csv"
    array = data_importer.get_rows_as_array(file_name)
    assert len(array) > 0


def test_get_rows_as_array_file_exists_and_has_data_correct_array_returned():
    expected_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    file_name = "aoc_2021/test_data/tenrowcount.csv"
    array = data_importer.get_rows_as_array(file_name)
    assert array == expected_array


def test_get_rows_as_array_day_ten_file_correct_array_returned():
    expected_array = [
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
    file_name = "aoc_2021/test_data/dayten.csv"
    array = data_importer.get_rows_as_array(file_name)
    assert array == expected_array


def test_get_rows_as_array_day_twelve_file_correct_array_returned():
    expected_array = [
        'start-A',
        'start-b',
        'A-c',
        'A-b',
        'b-d',
        'A-end',
        'b-end',
    ]
    file_name = "aoc_2021/test_data/daytwelve.csv"
    array = data_importer.get_rows_as_array(file_name)
    assert array == expected_array


##### get_as_array #####


def test_get_as_array_file_does_not_exist_empty_array_returned():
    file_name = "madeUpFile.fake"
    array = data_importer.get_as_array(file_name)
    assert array == []


def test_get_as_array_file_exists_and_has_data_valid_array_returned():
    file_name = "aoc_2021/test_data/dayfour_calls.csv"
    array = data_importer.get_as_array(file_name)
    assert len(array) > 0


def test_get_as_array_file_exists_and_has_data_correct_array_returned():
    expected_array = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24,
                      10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    file_name = "aoc_2021/test_data/dayfour_calls.csv"
    array = data_importer.get_as_array(file_name)
    assert array == expected_array


##### get_as_3d_array #####


def test_get_as_3d_array_file_does_not_exist_empty_array_returned():
    file_name = "madeUpFile.fake"
    array = data_importer.get_as_3d_array(file_name)
    assert array == []


def test_get_as_3d_array_file_exists_and_has_data_valid_array_returned():
    file_name = "aoc_2021/test_data/dayfour_boards.csv"
    array = data_importer.get_as_3d_array(file_name)
    assert len(array) > 0


def test_get_as_3d_array_file_exists_and_has_data_correct_array_returned():
    expected_array = [
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

    file_name = "aoc_2021/test_data/dayfour_boards.csv"
    array = data_importer.get_as_3d_array(file_name)
    assert array == expected_array


##### get_as_start_end_point_array #####


def test_get_as_start_end_point_array_file_does_not_exist_empty_array_returned():
    file_name = "madeUpFile.fake"
    array = data_importer.get_as_start_end_point_array(file_name)
    assert array == []


def test_get_as_start_end_point_array_file_exists_and_has_data_valid_array_returned():
    file_name = "aoc_2021/test_data/dayfive.csv"
    array = data_importer.get_as_start_end_point_array(file_name)
    assert len(array) > 0


def test_get_as_start_end_point_array_file_exists_and_has_data_correct_array_returned():
    expected_array = [
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
    file_name = "aoc_2021/test_data/dayfive.csv"
    array = data_importer.get_as_start_end_point_array(file_name)
    assert array == expected_array


def test_get_as_display_segment_array_file_exists_and_has_data_correct_array_returned():
    expected_array = [
        {data_importer.SIGNAL_VALUES: ["be", "cfbegad", "cbdgef", "fgaecd", "cgeb", "fdcge", "agebfd",
                                       "fecdb", "fabcd", "edb"], data_importer.OUTPUT_VALUE: ["fdgacbe", "cefdb", "cefbgd", "gcbe"]},
        {data_importer.SIGNAL_VALUES: ["edbfga", "begcd", "cbg", "gc", "gcadebf", "fbgde", "acbgfd",
                                       "abcde", "gfcbed", "gfec"], data_importer.OUTPUT_VALUE: ["fcgedb", "cgb", "dgebacf", "gc"]},
        {data_importer.SIGNAL_VALUES: ["fgaebd", "cg", "bdaec", "gdafb", "agbcfd", "gdcbef", "bgcad",
                                       "gfac", "gcb", "cdgabef"], data_importer.OUTPUT_VALUE: ["cg", "cg", "fdcagb", "cbg"]},
        {data_importer.SIGNAL_VALUES: ["fbegcd", "cbd", "adcefb", "dageb", "afcb", "bc", "aefdc",
                                       "ecdab", "fgdeca", "fcdbega"], data_importer.OUTPUT_VALUE: ["efabcd", "cedba", "gadfec", "cb"]},
        {data_importer.SIGNAL_VALUES: ["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea",
                                       "fcaegb", "dgceab", "fcbdga"], data_importer.OUTPUT_VALUE: ["gecf", "egdcabf", "bgf", "bfgea"]},
        {data_importer.SIGNAL_VALUES: ["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg", "gcfdb", "baec",
                                       "bfadeg", "bafgc", "acf"], data_importer.OUTPUT_VALUE: ["gebdcfa", "ecba", "ca", "fadegcb"]},
        {data_importer.SIGNAL_VALUES: ["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf", "ecdfab", "fbedc",
                                       "dacgb", "gdcebf", "gf"], data_importer.OUTPUT_VALUE: ["cefg", "dcbef", "fcge", "gbcadfe"]},
        {data_importer.SIGNAL_VALUES: ["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg", "ed", "bedf",
                                       "ced", "adcbefg", "gebcd"], data_importer.OUTPUT_VALUE: ["ed", "bcgafe", "cdgba", "cbgef"]},
        {data_importer.SIGNAL_VALUES: ["egadfb", "cdbfeg", "cegd", "fecab", "cgb", "gbdefca", "cg",
                                       "fgcdab", "egfdb", "bfceg"], data_importer.OUTPUT_VALUE: ["gbdfcae", "bgc", "cg", "cgb"]},
        {data_importer.SIGNAL_VALUES: ["gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef",
                                       "cafbge", "fdbac", "fegbdc"], data_importer.OUTPUT_VALUE: ["fgae", "cfgab", "fg", "bagce"]}
    ]
    file_name = "aoc_2021/test_data/dayeight.csv"
    array = data_importer.get_as_display_segment_array(file_name)
    assert array == expected_array


def test_get_as_2d_array_file_exists_and_has_data_correct_array_returned():
    expected_array = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
    ]
    file_name = "aoc_2021/test_data/daynine.csv"
    array = data_importer.get_as_2d_array(file_name)
    assert array == expected_array


def test_get_as_2d_array_day_eleven_file_correct_array_returned():
    expected_array = [
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
    file_name = "aoc_2021/test_data/dayeleven.csv"
    array = data_importer.get_as_2d_array(file_name)
    assert array == expected_array


def test_get_as_2d_array_day_fifteen_file_correct_array_returned():
    expected_array = [
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
    file_name = "aoc_2021/test_data/dayfifteen.csv"
    array = data_importer.get_as_2d_array(file_name)
    assert array == expected_array


##### get_as_points_and_folds #####


def test_get_as_points_and_folds_day_thirteen_file_correct_array_returned():
    expected_points = [
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
    expected_folds = [
        ['y', 7],
        ['x', 5]
    ]

    file_name = "aoc_2021/test_data/daythirteen.csv"
    points, folds = data_importer.get_as_points_and_folds(file_name)
    assert points == expected_points
    assert folds == expected_folds


##### get_as_string_and_dict #####


def test_get_as_string_and_dict_day_fourteen_file_correct_values_returned():
    expected_string = 'NNCB'
    expected_dict = {
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
    file_name = "aoc_2021/test_data/dayfourteen.csv"
    string, dictionary = data_importer.get_as_string_and_dict(file_name)
    assert string == expected_string
    assert dictionary == expected_dict


##### get_string_between #####


def test_get_string_between_is_not_string_empty_string_returned():
    string, left, right = 1, 2, 3
    assert data_importer.get_string_between(string, left, right) == ""


def test_get_string_between_left_not_in_string_right_is_string_up_to_right_returned():
    expected = 'hello th'
    left = 'test'
    right = 'ere'
    string = expected + right
    assert data_importer.get_string_between(string, left, right) == expected


def test_get_string_between_left_in_string_right_not_string_left_to_end_returned():
    expected = 'lo there'
    left = 'hel'
    right = 'test'
    string = left + expected
    assert data_importer.get_string_between(string, left, right) == expected


def test_get_string_between_neither_in_string_empty_string_returned():
    left = 'test'
    right = 'test'
    string = 'hello there'
    assert data_importer.get_string_between(string, left, right) == ''


##### get_as_rect #####


def test_get_as_rect_day_seventeen_file():
    expected_rect = {
        'top_left': {'x': 20, 'y': -5},
        'bottom_right': {'x': 30, 'y': -10}
    }
    file_name = "aoc_2021/test_data/dayseventeen.csv"
    rect = data_importer.get_as_rect(file_name)
    assert rect == expected_rect


##### get_as_list #####


def test_get_as_list_day_eighteen_file():
    expected_list = [
        [1, 2],
        [[1, 2], 3],
        [9, [8, 7]],
        [[1, 9], [8, 5]],
        [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], 9],
        [[[9, [3, 8]], [[0, 9], 6]], [[[3, 7], [4, 9]], 3]],
        [[[[1, 3], [5, 3]], [[1, 3], [8, 7]]], [
            [[4, 9], [6, 9]], [[8, 2], [7, 3]]]]
    ]
    file_name = "aoc_2021/test_data/dayeighteen.csv"
    result_list = data_importer.get_as_list(file_name)
    assert result_list == expected_list


##### get_as_3d_point_beacon_array #####


def test_get_as_3d_point_beacon_array_day_nineteen_small_file():
    expected_list = [
        [
            {'x': 404, 'y': -588, 'z': -901},
            {'x': 528, 'y': -643, 'z': 409},
            {'x': -838, 'y': 591, 'z': 734}
        ],
        [
            {'x': 686, 'y': 422, 'z': 578},
            {'x': 605, 'y': 423, 'z': 415},
            {'x': 515, 'y': 917, 'z': -361}
        ],
        [
            {'x': 649, 'y': 640, 'z': 665},
            {'x': 682, 'y': -795, 'z': 504},
            {'x': -784, 'y': 533, 'z': -524}
        ]
    ]
    file_name = "aoc_2021/test_data/daynineteensmall.csv"
    result_list = data_importer.get_as_3d_point_beacon_array(file_name)
    assert result_list == expected_list


##### get_new_line_delimited_file_as_2d_int_array #####


def test_get_new_line_delimited_file_as_2d_int_array_day_one_test_file():
    expected_list = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000]
    ]
    file_name = "aoc_2022/test_data/day1.txt"
    result_list = data_importer.get_new_line_delimited_file_as_2d_int_array(
        file_name)
    assert result_list == expected_list


##### get_as_stacks_and_moves #####


def test_get_as_stacks_and_moves_day_five_test_file():
    expected_stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
    expected_instructions = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]
    file_name = "aoc_2022/test_data/day5.txt"
    stacks, instrustions = data_importer.get_as_stacks_and_moves(file_name)
    assert expected_stacks == stacks and expected_instructions == instrustions
