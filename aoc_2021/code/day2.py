from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def part_one(data):
    hPosition = 0
    depth = 0

    for line in data:
        instructionValue = int(line[1])

        if line[0] == 'forward':
            hPosition += instructionValue
        elif line[0] == 'down':
            depth += instructionValue
        elif line[0] == 'up':
            depth -= instructionValue

    product = hPosition * depth
    return product


def part_two(data):
    hPosition = 0
    depth = 0
    aim = 0

    for line in data:
        instructionValue = int(line[1])

        if line[0] == 'forward':
            hPosition += instructionValue
            depth += aim * instructionValue
        elif line[0] == 'down':
            aim += instructionValue
        elif line[0] == 'up':
            aim -= instructionValue

    product = hPosition * depth
    return product


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_rows_as_multidimensional_array(
        "aoc_2021/data/daytwo.csv", " ")

    part_one_result = part_one(data)
    print("Day Two - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Two - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
