import numpy
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


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
        # move squared + move / 2
        binomialCoefficient = int(((move * move) + move) / 2)
        total += binomialCoefficient
    return total


def part_one(data):
    return FindSmallestMoveTotal(data, numpy.sum)


def part_two(data):
    return FindSmallestMoveTotal(data, BinomialCoefficientSum)


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_array("aoc_2021/data/dayseven.csv")

    part_one_result = part_one(data)
    print("Day Seven - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Seven - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
