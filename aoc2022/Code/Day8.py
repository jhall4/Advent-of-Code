import numpy
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter


def IsTreeVisible(forest, treeI, treeJ):
    height = len(forest)
    width = len(forest[0])
    tree = forest[treeI][treeJ]
    #horizontal
    j = 0
    while j < width:
        if j == treeJ:
            return True
        if tree > forest[treeI][j]:
            j+=1
            continue
        if j < treeJ:
            j = treeJ+1
        elif j > treeJ:
            break
    if j >= width:
        return True
    #vertical
    i = 0
    while i < height:
        if i == treeI:
            return True
        if tree > forest[i][treeJ]:
            i+=1
            continue
        if i < treeI:
            i = min(treeI+1, height-1)
        elif i > treeI:
            break
    if i >= height:
        return True
    return False


def GetScenicScore(forest, treeI, treeJ):
    left, right, up, down = 0, 0, 0, 0
    height = len(forest)
    width = len(forest[0])
    tree = forest[treeI][treeJ]
    #left
    for i in range(treeI-1, -1, -1):
        left += 1
        if tree <= forest[i][treeJ]:
            break
    #right 
    for i in range(treeI+1, width):
        right += 1
        if tree <= forest[i][treeJ]:
            break
    #up
    for j in range(treeJ-1, -1, -1):
        up += 1
        if tree <= forest[treeI][j]:
            break
    #down 
    for j in range(treeJ+1, height):
        down += 1
        if tree <= forest[treeI][j]:
            break
    return left * right * up * down


def PartOne(data):
    height = len(data)
    width = len(data[0])
    visibleTrees = numpy.zeros((width, height), dtype=int)
    for i in range(height):
        for j in range(width):
            if IsTreeVisible(data, i, j):
                visibleTrees[i][j] = 1
  
    return numpy.sum(visibleTrees)


def PartTwo(data):
    height = len(data)
    width = len(data[0])
    scenicScores = numpy.zeros((width, height), dtype=int)
    for i in range(height):
        for j in range(width):
            scenicScores[i][j] = GetScenicScore(data, i, j)
  
    return numpy.amax(scenicScores)


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAs2dArray("aoc2022/Data/day8.txt")

    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
