# make tests think they're running in code module
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent / "Code"
sys.path[0] = str(codeModulePath)

import DayEight
from Utils import DataImporter


testData = [
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


def test_PartOne():
    providedAnswer = 26
    assert DayEight.PartOne(testData) == providedAnswer


def test_PartTwo():
    providedAnswer = 61229
    assert DayEight.PartTwo(testData) == providedAnswer
