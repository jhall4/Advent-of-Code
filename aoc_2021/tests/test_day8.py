from utils import data_importer
from aoc_2021.code import DayEight
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


test_data = [
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


def test_part_one():
    provided_answer = 26
    assert DayEight.part_one(test_data) == provided_answer


def test_part_two():
    provided_answer = 61229
    assert DayEight.part_two(test_data) == provided_answer
