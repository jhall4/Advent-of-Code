import csv
from typing import List
import numpy
import math
import pathlib
import string
from os import path
from os.path import exists
import json


def GetPathOnDisk(fileName):
    basicPath = pathlib.Path(__file__)
    #path = pathlib.Path(__file__).parent.parent.parent / "Data" / fileName
    path = basicPath.parent.parent / fileName
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

def GetCsvRowsAsMultiDimensionalArray(fileName, delim):
    fileArray = GetCsvRowsAsArray(fileName)

    for i in range(len(fileArray)):
        splitLine = fileArray[i].split(delim)
        fileArray[i] = splitLine
    
    return fileArray


def GetAsMultiDimensionalArray(fileName, delim1, delim2, delim3):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path, newline='') as file:
        contents = file.read()

    topLevel = contents.split(delim1)
    for i in range(len(topLevel)):
        midLevel = topLevel[i].split(delim2)
        topLevel[i] = midLevel
        for j in range(len(midLevel)):
            lowLevel = midLevel[j].split(delim3)
            topLevel[i][j] = lowLevel
            #for k in range(len(lowLevel)):
            #    value = lowLevel[k]
            #    topLevel[i][j][k] = value

    return topLevel


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

    with open(path, newline='') as file:
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
    path = GetPathOnDisk(fileName)
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


def GetAsString(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()
    return contents


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


def GetStringBetween(string, left='', right=''):
    if not isinstance(string, str) or not isinstance(left, str) or not isinstance(right, str):
        return ""
    if left not in string and right not in string:
        return ""
    leftSearch = 0
    if left != '' and left in string:
        leftSearch = string.index(left)+len(left)
    rightSearch = len(string)
    if right != '' and right in string:
        rightSearch = string.index(right)
    return string[leftSearch:rightSearch]


topLeft = 'topLeft'
bottomRight = 'bottomRight'


def GetAsRect(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()

    findX = 'x='
    findY = 'y='
    xStr = GetStringBetween(contents, findX, ',')
    yStr = GetStringBetween(contents, findY)
    xs = xStr.split('..')
    ys = yStr.split('..')

    rect = {}
    rect[topLeft] = {'x': int(xs[0]), 'y': int(ys[1])}
    rect[bottomRight] = {'x': int(xs[1]), 'y': int(ys[0])}

    return rect


def GetAsList(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()

    lines = contents.split('\n')
    list = []
    for line in lines:
        list.append(json.loads(line))
    return list


def GetAs3dPointBeaconArray(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()

    lines = contents.split('\n')
    scanners = []
    currentScanner = None
    for line in lines:
        if 'scanner' in line:
            if currentScanner:
                scanners.append(currentScanner)
            currentScanner = []
            continue
        if not line.strip():
            continue
        coords = line.split(',')
        currentScanner.append({'x': int(coords[0]), 'y': int(coords[1]), 'z': int(coords[2])})
    scanners.append(currentScanner)
    return scanners


def GetNewLineDelimitedFileAs2dIntArray(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()
    lines = contents.split('\n')

    topLevelArray = []
    secondLevelArray = []
    for line in lines:
        if line != '':
            secondLevelArray.append(int(line))
        else:
            topLevelArray.append(secondLevelArray)
            secondLevelArray = []
        
    if len(secondLevelArray)>0:
        topLevelArray.append(secondLevelArray)
    return topLevelArray


def GetAsStacksAndMoves(fileName):
    path = GetPathOnDisk(fileName)
    if(not exists(path)):
        return []

    with open(path) as file:
        contents = file.read()
    lines = contents.split('\n')

    stacks = []
    instructions = []

    for line in lines:
        if "[" in line:
            for i in range(math.ceil(len(line)/4)):
                start = i*4
                end = min(start+4, len(line))
                crate = line[start:end].strip()
                if len(crate) > 0:
                    while len(stacks) < i+1:
                        stacks.append([])
                    stacks[i].append(crate[1])
        elif "move" in line:
            instruction = [int(i) for i in line.split() if i.isdigit()]
            instructions.append(instruction)


    for i in range(len(stacks)):
        stacks[i].reverse()
    return stacks, instructions
                
            
        
