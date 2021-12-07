
import csv
import numpy
import pathlib
from os import path
from os.path import exists

def GetPathOnDisk(fileName):
    path = pathlib.Path(__file__).parent.parent.parent / "Data" / fileName
    return path

def GetNumbersFromString(string):
    if not isinstance(string, str):
        return []

    numbers = [int(i) for i in string.split() if i.isdigit()]
    return numbers

def GetCsvRowsAsArray(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []
    
    with open(path) as file:
        contents = file.read()

    return list(contents.split("\n"))

def GetCsvAsArray(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []
    
    with open(path) as file:
        array = numpy.loadtxt(file, delimiter=",", dtype=int)

    return array.flatten().tolist()

def GetCsvAs3dArray(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []
        
    with open(path , newline='') as file:
        contents = file.read()

    topLevel = contents.split("\n\n")
    for i in range(len(topLevel)):
        midLevel = topLevel[i].split("\n")
        topLevel[i] = midLevel
        for j in range(len(midLevel)):
            lowLevel = midLevel[j].split()
            topLevel[i][j] = lowLevel
            for k in range(len(lowLevel)):
                value = lowLevel[k]
                topLevel[i][j][k] = int(value)

    return topLevel

def GetAsStartEndPointArray(fileName):
    path= GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()
    
    lines = contents.split("\n")
    for i in range(len(lines)):
        line = lines[i].split(" -> ")
        lines[i] = line
        for j in range(len(line)):
            point = line[j].split(',')
            lines[i][j] = point
            for k in range(len(point)):
                value = point[k]
                lines[i][j][k] = int(value)

    return lines