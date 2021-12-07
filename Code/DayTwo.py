from Utils import DataImporter


def PartOne(data):
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


def PartTwo(data):
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
    data = DataImporter.GetCsvRowsAsArray("daytwo.csv")

    partOneResult = PartOne(data)
    print("Day Two - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Two - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
