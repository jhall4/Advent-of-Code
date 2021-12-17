from Utils import DataImporter
import sys


def HexToBin(hexString):
    binaryString = ""
    for char in hexString:
        binNum = bin(int(char, 16))
        binaryString += str(binNum)[2:].zfill(4)
    return binaryString


def PopFromString(string, numToPop):
    popped = string[:numToPop]
    string = string[numToPop:]
    return popped, string


def BinStringToInt(binString):
    return int(binString,2)


def GetNextPacket(binString):
    version, binString = PopFromString(binString, 3)
    version = BinStringToInt(version)
    id, binString = PopFromString(binString, 3)
    id = BinStringToInt(id)
    value = ""
    subPackets = []
    if id == 4: # literal value
        checkBit = '1'
        while checkBit == '1':
            checkBit, binString = PopFromString(binString, 1)
            temp, binString = PopFromString(binString, 4)
            value += temp
        value = BinStringToInt(value)
    else: # operator
        lengthTypeId, binString = PopFromString(binString, 1)
        if lengthTypeId == '0': 
            totalBitLengthOfSubPackets, binString = PopFromString(binString, 15)
            totalBitLengthOfSubPackets = BinStringToInt(totalBitLengthOfSubPackets)
            subPacketsStr, binString = PopFromString(binString, totalBitLengthOfSubPackets)
            while len(subPacketsStr) > 0:
                (tVer, tId, tValue, tSubPackets, subPacketsStr) = GetNextPacket(subPacketsStr)
                subPackets.append((tVer, tId, tValue, tSubPackets))
        if lengthTypeId == '1': 
            numberOfSubPackets, binString = PopFromString(binString, 11)
            numberOfSubPackets = BinStringToInt(numberOfSubPackets)
            for i in range(numberOfSubPackets):
                (tVer, tId, tValue, tSubPackets, binString) = GetNextPacket(binString)
                subPackets.append((tVer, tId, tValue, tSubPackets))

        
    return version, id, value, subPackets, binString


def TotalVersionsInSubPackets(curTotal, packets):
    for packet in packets:
        (tVer, _, _, subPackets) = packet
        curTotal += tVer
        curTotal += TotalVersionsInSubPackets(0, subPackets)
    return curTotal


def EvaluatePackets(id, value, subPackets):
    if id == 4: #value
        return value

    subValues = []
    for packet in subPackets:
        (_, tId, tValue, tSubPackets) = packet
        subValues.append(EvaluatePackets(tId, tValue, tSubPackets))

    if id == 0: #sum
        total = 0
        for val in subValues:
            total += val
        return total
    elif id == 1: #product
        total = 1
        for val in subValues:
            total *= val
        return total
    elif id == 2: #min
        minVal = 9999999999999
        for val in subValues:
            minVal = min(minVal, val)
        return minVal
    elif id == 3: #max
        maxVal = 0
        for val in subValues:
            maxVal = max(maxVal, val)
        return maxVal
    elif id == 5: #greater than - These packets always have exactly two sub-packets.
        retVal = 1 if subValues[0] > subValues[1] else 0
        return retVal
    elif id == 6: #less than - These packets always have exactly two sub-packets.
        retVal = 1 if subValues[0] < subValues[1] else 0
        return retVal
    elif id == 7: #equality - These packets always have exactly two sub-packets.
        retVal = 1 if subValues[0] == subValues[1] else 0
        return retVal


def PartOne(data):
    binData = HexToBin(data)
    (version, _, _, subPackets, _) = GetNextPacket(binData)

    verTotal = TotalVersionsInSubPackets(version, subPackets)
    return verTotal


def PartTwo(data):
    binData = HexToBin(data)
    (_, id, value, subPackets, _) = GetNextPacket(binData)

    evaluation = EvaluatePackets(id, value, subPackets)
    return evaluation


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAsString("daysixteen.csv")

    partOneResult = PartOne(data)
    print("Day Sixteen - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Sixteen - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
