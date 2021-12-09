from Utils import DataImporter
import numpy
import copy


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


def GetBasinSize(data, i, j, turned = False):
    data[i][j] = 9
    basinSize = 1
    if j-1 >= 0 and data[i][j-1] < 9:
        basinSize += GetBasinSize(data,i,j-1)
    if i-1 >= 0 and data[i-1][j] < 9:
        basinSize += GetBasinSize(data,i-1,j)
    if j+1 < len(data[i]) and data[i][j+1] < 9:
        basinSize += GetBasinSize(data,i,j+1)
    if i+1 < len(data) and data[i+1][j] < 9:
        basinSize += GetBasinSize(data,i+1,j)

    return basinSize

def PartOne(data):
    lowestPoints = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if IsLowestPoint(data, i, j):
                lowestPoints.append(data[i][j])

    total = numpy.sum(lowestPoints)
    total += len(lowestPoints)
    
    return total


def PartTwo(data):
    basinSizes = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if IsLowestPoint(data, i, j):
                mutableData = copy.deepcopy(data)
                basinSizes.append(GetBasinSize(mutableData,i,j))
    
    basinSizes.sort(reverse=True)
    total = 1
    for i in range(3):
        total = total * basinSizes[i]
    return total


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAs2dArray("daynine.csv")

    partOneResult = PartOne(data)
    print("Day Nine - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Nine - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
