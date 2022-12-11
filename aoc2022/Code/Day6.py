import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

def FindMarkerPosition(data, markerLen):
    for i in range(len(data)):
        end = min(i+markerLen, len(data))
        buffer = set(data[i:end])
        if len(buffer) == markerLen:
            return end
    return 0


def PartOne(data):
    return FindMarkerPosition(data, 4)


def PartTwo(data):
    return FindMarkerPosition(data, 14)


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetFileAsString("aoc2022/Data/day6.txt")

    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
