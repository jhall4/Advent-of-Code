from Utils import DataImporter
import sys


def PartOne(data):
    return 0


def PartTwo(data):
    return 0


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvRowsAsArray("dayX.csv")

    partOneResult = PartOne(data)
    print("Day X - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day X - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
