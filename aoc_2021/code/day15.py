import copy
import heapq
import numpy
from collections import defaultdict
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def GetPart2data(grid):
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


def part_one(data):
    score = FindShortestPath(data)
    return score


def part_two(data):
    bigdata = GetPart2data(data)
    score = FindShortestPath(bigdata)
    return score


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_2d_array("aoc_2021/data/dayfifteen.csv")

    part_one_result = part_one(data)
    print("Day Fifteen - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Fifteen - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
