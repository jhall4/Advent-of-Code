from Utils import DataImporter



def PartOne(data):
    numIncreased = 0
    valA = -1
    valB = -1

    for line in data:
        valB = int(line)
        if valA >= 0 and valB > valA:
            numIncreased += 1

        valA = valB

    return numIncreased


def PartTwo(data):
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
    data = DataImporter.GetCsvRowsAsArray("dayone.csv")

    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
