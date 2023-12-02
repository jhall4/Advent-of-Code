from aoc_2021.code import DayTen
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = [
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


def test_part_one():
    provided_answer = 26397
    assert DayTen.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 288957
    assert DayTen.part_two(test_data) == provided_answer
