from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def HexToBin(hex_stringing):
    binary_stringing = ""
    for char in hex_stringing:
        binNum = bin(int(char, 16))
        binary_stringing += str(binNum)[2:].zfill(4)
    return binary_stringing


def PopFromString(string, numToPop):
    popped = string[:numToPop]
    string = string[numToPop:]
    return popped, string


def BinStringToInt(binString):
    return int(binString, 2)


def GetNextPacket(binString):
    version, binString = PopFromString(binString, 3)
    version = BinStringToInt(version)
    id, binString = PopFromString(binString, 3)
    id = BinStringToInt(id)
    value = ""
    subPackets = []
    if id == 4:  # literal value
        checkBit = '1'
        while checkBit == '1':
            checkBit, binString = PopFromString(binString, 1)
            temp, binString = PopFromString(binString, 4)
            value += temp
        value = BinStringToInt(value)
    else:  # operator
        lengthTypeId, binString = PopFromString(binString, 1)
        if lengthTypeId == '0':
            totalBitLengthOfSubPackets, binString = PopFromString(
                binString, 15)
            totalBitLengthOfSubPackets = BinStringToInt(
                totalBitLengthOfSubPackets)
            subPacketsStr, binString = PopFromString(
                binString, totalBitLengthOfSubPackets)
            while len(subPacketsStr) > 0:
                (tVer, tId, tValue, tSubPackets,
                 subPacketsStr) = GetNextPacket(subPacketsStr)
                subPackets.append((tVer, tId, tValue, tSubPackets))
        if lengthTypeId == '1':
            numberOfSubPackets, binString = PopFromString(binString, 11)
            numberOfSubPackets = BinStringToInt(numberOfSubPackets)
            for i in range(numberOfSubPackets):
                (tVer, tId, tValue, tSubPackets,
                 binString) = GetNextPacket(binString)
                subPackets.append((tVer, tId, tValue, tSubPackets))

    return version, id, value, subPackets, binString


def TotalVersionsInSubPackets(curTotal, packets):
    for packet in packets:
        (tVer, _, _, subPackets) = packet
        curTotal += tVer
        curTotal += TotalVersionsInSubPackets(0, subPackets)
    return curTotal


def EvaluatePackets(id, value, subPackets):
    if id == 4:  # value
        return value

    subValues = []
    for packet in subPackets:
        (_, tId, tValue, tSubPackets) = packet
        subValues.append(EvaluatePackets(tId, tValue, tSubPackets))

    if id == 0:  # sum
        total = 0
        for val in subValues:
            total += val
        return total
    elif id == 1:  # product
        total = 1
        for val in subValues:
            total *= val
        return total
    elif id == 2:  # min
        minVal = 9999999999999
        for val in subValues:
            minVal = min(minVal, val)
        return minVal
    elif id == 3:  # max
        maxVal = 0
        for val in subValues:
            maxVal = max(maxVal, val)
        return maxVal
    # greater than - These packets always have exactly two sub-packets.
    elif id == 5:
        retVal = 1 if subValues[0] > subValues[1] else 0
        return retVal
    # less than - These packets always have exactly two sub-packets.
    elif id == 6:
        retVal = 1 if subValues[0] < subValues[1] else 0
        return retVal
    # equality - These packets always have exactly two sub-packets.
    elif id == 7:
        retVal = 1 if subValues[0] == subValues[1] else 0
        return retVal


def part_one(data):
    bindata = HexToBin(data)
    (version, _, _, subPackets, _) = GetNextPacket(bindata)

    verTotal = TotalVersionsInSubPackets(version, subPackets)
    return verTotal


def part_two(data):
    bindata = HexToBin(data)
    (_, id, value, subPackets, _) = GetNextPacket(bindata)

    evaluation = EvaluatePackets(id, value, subPackets)
    return evaluation


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_string("aoc_2021/data/daysixteen.csv")

    part_one_result = part_one(data)
    print("Day Sixteen - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Sixteen - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
