from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def part_one(data):
    numIncreased = 0
    valA = -1
    valB = -1

    for line in data:
        valB = int(line)
        if valA >= 0 and valB > valA:
            numIncreased += 1

        valA = valB

    return numIncreased


def part_two(data):
    numIncreased = 0
    valA = -1
    valB = -1
    valC = -1

    windowA = -1
    windowB = -1

    for line in data:
        valC = int(line)
        if valA >= 0 and valB >= 0 and valC >= 0:
            windowB = valA + valB + valC

        if windowA >= 0 and windowB > windowA:
            numIncreased += 1

        valA = valB
        valB = valC

        windowA = windowB

    return numIncreased


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_rows_as_array("aoc_2021/data/dayone.csv")

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
