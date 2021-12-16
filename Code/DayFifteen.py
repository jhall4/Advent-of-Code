from Utils import DataImporter
from collections import defaultdict
import numpy
import heapq
import copy


def GetPart2Data(grid):
    repeatNum = 5
    gridSize = len(grid)
    bigGrid = numpy.zeros(
        [gridSize*repeatNum, gridSize*repeatNum], dtype=int).tolist()

    for i in range(gridSize):
        for j in range(gridSize):
            for x in range(repeatNum):
                for y in range(repeatNum):
                    newNum = grid[i][j]+x+y
                    newNum = newNum-9 if newNum > 9 else newNum
                    bigGrid[i+(gridSize*x)][j+(gridSize*y)] = newNum
    return bigGrid


def FindShortestPath(grid):
    gridSize = len(grid)
    visitationCosts = numpy.full(
        [gridSize, gridSize], 999999999999999999).tolist()
    changed = True
    while changed:
        changed = False
        for i in range(gridSize):
            for j in range(gridSize):
                costFromAbove = costFromBelow = costFromLeft = costFromRight = 99999999999
                if i == 0 and j == 0:
                    visitationCosts[i][j] = 0
                    continue
                if i-1 >= 0:
                    costFromAbove = visitationCosts[i-1][j]
                if i+1 < gridSize:
                    costFromBelow = visitationCosts[i+1][j]
                if j-1 >= 0:
                    costFromLeft = visitationCosts[i][j-1]
                if j+1 < gridSize:
                    costFromRight = visitationCosts[i][j+1]
                curCost = visitationCosts[i][j]
                minNeightborCost = min(
                    costFromAbove, costFromBelow, costFromLeft, costFromRight)
                potentialCost = grid[i][j] + minNeightborCost
                if curCost == 0 or curCost > potentialCost:
                    changed = True
                    visitationCosts[i][j] = potentialCost
    return visitationCosts[gridSize-1][gridSize-1]


def PartOne(data):
    score = FindShortestPath(data)
    return score


def PartTwo(data):
    bigData = GetPart2Data(data)
    score = FindShortestPath(bigData)
    return score


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAs2dArray("dayfifteen.csv")

    partOneResult = PartOne(data)
    print("Day Fifteen - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Fifteen - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
