from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def part_one(data):
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


def part_two(data):
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
    data = data_importer.get_rows_as_array("aoc_2021/data/daythree.csv")

    part_one_result = part_one(data)
    print("Day Three - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Three - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
