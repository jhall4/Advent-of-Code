import copy
import numpy
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def IsLowestPoint(data, i, j):
    xleft, xabove, xright, xbelow = 99, 99, 99, 99
    if j-1 >= 0:
        xleft = data[i][j-1]
    if i-1 >= 0:
        xabove = data[i-1][j]
    if j+1 < len(data[i]):
        xright = data[i][j+1]
    if i+1 < len(data):
        xbelow = data[i+1][j]
    val = data[i][j]
    return val < xleft and val < xabove and val < xright and val < xbelow


def GetBasinSize(data, i, j, turned=False):
    data[i][j] = 9
    basinSize = 1
    if j-1 >= 0 and data[i][j-1] < 9:
        basinSize += GetBasinSize(data, i, j-1)
    if i-1 >= 0 and data[i-1][j] < 9:
        basinSize += GetBasinSize(data, i-1, j)
    if j+1 < len(data[i]) and data[i][j+1] < 9:
        basinSize += GetBasinSize(data, i, j+1)
    if i+1 < len(data) and data[i+1][j] < 9:
        basinSize += GetBasinSize(data, i+1, j)

    return basinSize


def part_one(data):
    lowestPoints = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if IsLowestPoint(data, i, j):
                lowestPoints.append(data[i][j])

    total = numpy.sum(lowestPoints)
    total += len(lowestPoints)

    return total


def part_two(data):
    basinSizes = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if IsLowestPoint(data, i, j):
                mutabledata = copy.deepcopy(data)
                basinSizes.append(GetBasinSize(mutabledata, i, j))

    basinSizes.sort(reverse=True)
    total = 1
    for i in range(3):
        total = total * basinSizes[i]
    return total


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_2d_array("aoc_2021/data/daynine.csv")

    part_one_result = part_one(data)
    print("Day Nine - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Nine - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
