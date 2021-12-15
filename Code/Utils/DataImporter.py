
import csv
from typing import List
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

signalValues = "signalValues"
outputValue = "outputValue"

def GetAsDisplaySegmentArray(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()

    segments = []
    lines = contents.split("\n")
    for i in range(len(lines)):
        line = lines[i].split(" | ")
        segment = {}
        segment[signalValues] = line[0].split(" ")
        segment[outputValue] = line[1].split(" ")
        segments.append(segment)

    return segments
    
    
def GetAs2dArray(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()

    lines = contents.split("\n")
    for i in range(len(lines)):
        lines[i] = list(map(int, list(lines[i])))
    
    return lines


def GetAsPointsAndFolds(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()

    sections = contents.split("\n\n")
    points = sections[0].split("\n")
    folds = sections[1].split("\n")

    for i, point in enumerate(points):
        points[i] = numpy.fromstring(point, dtype=int, sep=',').tolist()

    unneededInfo = 'fold along '
    for i, fold in enumerate(folds):
        fold = fold.replace(unneededInfo, '')
        fold = fold.split("=")
        fold[1] = int(fold[1])
        folds[i] = fold

    return points, folds


def GetAsStringAndDict(fileName):
    string = ""
    dict = {}
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()
    sections = contents.split('\n\n')

    string = sections[0]
    entries = sections[1].split('\n')

    for entry in entries:
        (key, val) = entry.split(' -> ')
        dict[key] = val
    
    return string, dict
