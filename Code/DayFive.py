import numpy
from Utils import DataImporter


def FindNumDangerousPoints(data, includeDiagonals):
    #determine grid size
    maxZeroth = 0
    maxOneth = 0
    for line in data:
        for point in line:
            maxZeroth = max(maxZeroth, point[0])
            maxOneth = max(maxOneth, point[1])

    #plot to grid
    grid = numpy.zeros([maxZeroth+1, maxOneth+1], dtype=int)
    for line in data:
        #take away 1 from all to account for array indexing
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        if x1 == x2: #horizontal
            yy1 = min(y1, y2)
            yy2 = max(y1, y2)
            for j in range(yy1, yy2+1):
                grid[j, x1] += 1 
        elif y1 == y2: #vertical
            xx1 = min(x1, x2)
            xx2 = max(x1, x2)
            for j in range(xx1, xx2+1):
                grid[y1, j] += 1 
        elif includeDiagonals: #diagonal - only 45s
            xSlope = 1 if x1 - x2 < 0 else -1
            ySlope = 1 if y1 - y2 < 0 else -1

            while(x1 != x2+xSlope and y1 != y2+ySlope):
                grid[y1, x1] += 1
                x1 += xSlope
                y1 += ySlope
    #count cells w/ >=2
    dangerPointCount = 0
    for row in grid:
        for point in row:
            if point >= 2:
                dangerPointCount += 1
    
    return dangerPointCount


def PartOne(data): 
    return FindNumDangerousPoints(data, includeDiagonals=False)


def PartTwo(data):
    return FindNumDangerousPoints(data, includeDiagonals=True)

def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAsStartEndPointArray("dayfive.csv")

    partOneResult = PartOne(data)
    print("Day Five - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Five - Part Two")
    print("Result: {}".format(partTwoResult))

if __name__ == "__main__":
    main()