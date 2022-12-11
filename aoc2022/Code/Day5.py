import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

def GetTopCrateString(stacks):
    crateString = ""
    for stack in stacks:
        crateString = crateString + stack[-1]
    return crateString


def PartOne(stacks, instrustions):
    for instruction in instrustions:
        amt = instruction[0]
        src = instruction[1]-1
        dst = instruction[2]-1
        
        for i in range(amt):
            crate = stacks[src].pop()
            stacks[dst].append(crate)
    return GetTopCrateString(stacks)


def PartTwo(stacks, instrustions):
    for instruction in instrustions:
        amt = instruction[0]
        src = instruction[1]-1
        dst = instruction[2]-1
        srcLen = len(stacks[src])

        movedCrates = stacks[src][srcLen-amt:srcLen]
        stacks[src] = stacks[src][ :-amt]
        stacks[dst].extend(movedCrates)
    return GetTopCrateString(stacks)


def main():
    """ Main program """
    # Code goes over here.
    stacks, instrustions = DataImporter.GetAsStacksAndMoves("aoc2022/Data/day5.txt")

    partOneResult = PartOne(stacks, instrustions)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    stacks, instrustions = DataImporter.GetAsStacksAndMoves("aoc2022/Data/day5.txt")
    partTwoResult = PartTwo(stacks, instrustions)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
