from Utils import DataImporter
import copy
import numpy
import math


def GetPointsAsGrid(points, folds):
    maxX = 0
    maxY = 0
    for fold in folds:
        (axis, foldAt) = fold
        if axis == 'y':
            maxY = max(2*foldAt, maxY)
        elif axis == 'x':
            maxX = max(2*foldAt, maxX)

    grid = numpy.zeros([maxY+1, maxX+1], dtype=int).tolist()

    for point in points:
        x = point[0]
        y = point[1]
        grid[y][x] = 1

    return grid

def FoldGrid(grid, fold):
    foldedGrid = []
    (axis, foldAt) = fold

    gridHeight = len(grid) 
    gridWidth = len(grid[0])
    if axis == 'y': # fold at y horizontally
        newGridHeight = math.ceil(gridHeight/2)
        foldedGrid = numpy.zeros([newGridHeight,gridWidth], dtype=int).tolist()
        for y in range(newGridHeight):
            if y == foldAt:
                continue
            for x in range(gridWidth):
                y2 = (2 * foldAt) - (y)
                foldedGrid[y][x] = grid[y][x] + grid[y2][x] 
    elif axis == 'x': # fold at x vertically
        newGridWidth = math.ceil(gridWidth/2)
        foldedGrid = numpy.zeros([gridHeight,newGridWidth], dtype=int).tolist()
        for y in range(gridHeight):
            for x in range(newGridWidth):
                if x == foldAt:
                    continue
                x2 = (2 * foldAt) - (x)
                foldedGrid[y][x] = grid[y][x] + grid[y][x2] 
    return foldedGrid



def PartOne(points, folds):
    grid = GetPointsAsGrid(points, folds)
    #for fold in folds:
    #    grid = FoldGrid(grid, fold)
    grid = FoldGrid(grid, folds[0])


    numDots = 0
    for row in grid:
        for val in row:
            if val > 0:
                numDots += 1
    return numDots


def PartTwo(points, folds):
    grid = GetPointsAsGrid(points, folds)
    for fold in folds:
        grid = FoldGrid(grid, fold)

    output = '\n'
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if grid[i][j] > 0:
                output += '\u2588'
            elif grid[i][j] == 0:
                output += ' '
        output += '\n'
    
    return output


def main():
    """ Main program """
    # Code goes over here.
    points, folds = DataImporter.GetAsPointsAndFolds("daythirteen.csv")

    partOneResult = PartOne(points, folds)
    print("Day Thirteen - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(points, folds)
    print("Day Thirteen - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
