import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

import numpy

def FindSmallestMoveTotal(data, totalMethod):
    total = numpy.sum(data)
    avg = round(total / len(data))
    moves = []
    for crab in data:
        moves.append(abs(crab-avg))

    smallestTotal = totalMethod(moves)

    searchRange = round(numpy.amax(data)/2)
    for i in range(searchRange):
        smallerMoves = []
        biggerMoves = []
        for crab in data:
            smallerMoves.append(abs(crab-avg-i))
            biggerMoves.append(abs(crab-avg+i))

        smallerTotal = totalMethod(smallerMoves)
        biggerTotal = totalMethod(biggerMoves)
        
        smallestTotal = min(smallestTotal, smallerTotal)
        smallestTotal = min(biggerTotal, smallestTotal)

    return smallestTotal

def BinomialCoefficientSum(moves):
    total = 0
    for move in moves:
        #move squared + move / 2
        binomialCoefficient = int(((move * move) + move) / 2)
        total += binomialCoefficient
    return total


def PartOne(data):
    return FindSmallestMoveTotal(data, numpy.sum)

def PartTwo(data):
    return FindSmallestMoveTotal(data, BinomialCoefficientSum)


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvAsArray("aoc2021/Data/dayseven.csv")

    partOneResult = PartOne(data)
    print("Day Seven - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Seven - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
