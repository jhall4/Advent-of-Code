from Utils import DataImporter
import sys


def PartOne(data):
    numDigits = len(data[0])
    bitCounts = [0] * numDigits
    for line in data:
        digits = list(line)
        for i in range(numDigits):
            if digits[i] == '1':
                bitCounts[i] += 1
            if digits[i] == '0':
                bitCounts[i] -= 1

    gammaString = '0b'
    epsilonString = '0b'
    for bitCount in bitCounts:
        if bitCount >= 0:  # 1 is more common
            gammaString += "1"
            epsilonString += "0"
        elif bitCount < 0:  # 0 is more common
            gammaString += "0"
            epsilonString += "1"

    gammaRate = int(gammaString, 2)
    epsilonRate = int(epsilonString, 2)
    powerConsumption = gammaRate * epsilonRate
    return powerConsumption


def PartTwo(data):
    oxyGenRating = FindNumberByBitCriteria(data, True)
    co2ScrubRating = FindNumberByBitCriteria(data, False)

    oxyGenRatingInt = int(oxyGenRating, 2)
    co2ScrubRatingInt = int(co2ScrubRating, 2)
    lifeSupportRating = oxyGenRatingInt * co2ScrubRatingInt

    return lifeSupportRating


def FindNumberByBitCriteria(data, mostCommon, digitIdx=0):
    oneCount = 0
    zeroCount = 0
    onesBitValues = []
    zerosBitValues = []

    for line in data:
        digits = list(line)
        if digits[digitIdx] == '1':
            oneCount += 1
            onesBitValues.append(line)
        if digits[digitIdx] == '0':
            zeroCount += 1
            zerosBitValues.append(line)

    dataToKeep = []
    if oneCount >= zeroCount:
        if mostCommon:
            dataToKeep = onesBitValues
        else:
            dataToKeep = zerosBitValues
    else:
        if mostCommon:
            dataToKeep = zerosBitValues
        else:
            dataToKeep = onesBitValues

    if len(dataToKeep) == 1:
        return dataToKeep[0]
    else:
        return FindNumberByBitCriteria(dataToKeep, mostCommon, digitIdx+1)


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvRowsAsArray("daythree.csv")

    partOneResult = PartOne(data)
    print("Day Three - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Three - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
