import copy
from collections import defaultdict
from typing import DefaultDict
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def InsertIntoPair(pair, val):
    return pair[:1] + val + pair[1:]


def GetPolymerPairsList(polymer):
    polyPairs = []
    polyChars = list(polymer)
    for i in range(len(polyChars)):
        if i+1 < len(polyChars):
            polyPairs.append(polyChars[i] + polyChars[i+1])
    return polyPairs


def GetPolymerPairsDict(polymer):
    polyPairs = defaultdict(int)
    polyChars = list(polymer)
    for i in range(len(polyChars)):
        if i+1 < len(polyChars):
            polyPairs[polyChars[i] + polyChars[i+1]] += 1
    return polyPairs


def ApplyInsertions(polymer, insertions, depth):
    polyPairs = GetPolymerPairsList(polymer)
    if depth == 0:
        return polymer
    for i, pair in enumerate(polyPairs):
        if pair in insertions:
            newPolymer = InsertIntoPair(pair, insertions[pair])
            polyPairs[i] = ApplyInsertions(newPolymer, insertions, depth-1)

    finishedPolymer = polyPairs[0][0]
    for pair in polyPairs:
        finishedPolymer += pair[1:]

    return finishedPolymer


def SimulateInsertions(polymer, insertions, depth):
    polyPairsDict = GetPolymerPairsDict(polymer)
    letterCounts = defaultdict(int)
    for letter in polymer:
        letterCounts[letter] += 1
    while depth > 0:
        depth -= 1
        currentPolyPairs = copy.deepcopy(polyPairsDict)
        newPolyPairs = defaultdict(int)
        for pair in currentPolyPairs:
            if currentPolyPairs[pair] > 0 and pair in insertions:
                currentAmount = currentPolyPairs[pair]
                polyPairsDict[pair] = 0
                insertion = insertions[pair]
                letterCounts[insertion] += currentAmount
                newPolymer = InsertIntoPair(pair, insertion)
                newPairs = GetPolymerPairsList(newPolymer)
                for newPair in newPairs:
                    newPolyPairs[newPair] += currentAmount
        for pair in newPolyPairs:
            polyPairsDict[pair] += newPolyPairs[pair]
    return letterCounts


def ScorePolymer(polymer):
    letterCount = defaultdict(int)
    for letter in polymer:
        letterCount[letter] += 1
    return ScoreCount(letterCount)


def ScoreCount(count):
    mostCommonCount = 0
    leastCommonCount = 999999999999999999999
    for count in count.values():
        mostCommonCount = max(mostCommonCount, count)
        leastCommonCount = min(leastCommonCount, count)

    return mostCommonCount - leastCommonCount


def part_one(polymer, insertions):
    numSteps = 10
    # finishedPolymer = ApplyInsertions(polymer, insertions, numSteps)
    # return ScorePolymer(finishedPolymer)
    simulatedPolymerCount = SimulateInsertions(polymer, insertions, numSteps)
    return ScoreCount(simulatedPolymerCount)


def part_two(polymer, insertions):
    numSteps = 40
    simulatedPolymerCount = SimulateInsertions(polymer, insertions, numSteps)
    return ScoreCount(simulatedPolymerCount)


def main():
    """ Main program """
    # Code goes over here.
    polymer, insertions = data_importer.get_as_string_and_dict(
        "aoc_2021/data/dayfourteen.csv")

    part_one_result = part_one(polymer, insertions)
    print("Day Fourteen - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(polymer, insertions)
    print("Day Fourteen - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
