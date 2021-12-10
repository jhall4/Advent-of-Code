# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayTen

testData = [
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


def test_PartOne():
    providedAnswer = 26397
    assert DayTen.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 288957
    assert DayTen.PartTwo(testData) == providedAnswer
