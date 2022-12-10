import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter


items = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def GetPriority(itemChar):
    priority = 0
    for item in items:
        priority += 1
        if itemChar == item:
            break
    return priority


def PartOne(data):
    priorityTotal = 0
    for ruckSack in data:
        sackLen = len(ruckSack)
        sackMid = int(sackLen/2)
        firstHalf = set(ruckSack[0:sackMid])
        secondHalf = set(ruckSack[sackMid:sackLen])
        sharedItem = list(firstHalf & secondHalf)
        priorityTotal += GetPriority(sharedItem[0])
    return priorityTotal


def PartTwo(data):
    priorityTotal = 0
    for i in range(0, len(data), 3):
        elf1 = set(data[i])
        elf2 = set(data[i+1])
        elf3 = set(data[i+2])
        sharedItem = list(elf1 & elf2 & elf3)
        priorityTotal += GetPriority(sharedItem[0])
    return priorityTotal


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvRowsAsArray("aoc2022/Data/day3.txt")

    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
