import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

# A, X = Rock
# B, Y = Paper
# C, Z = Scissors
#
# 1pt - throw Rock
# 2pt - throw Paper
# 3pt - throw Scissors
#
# 0pt - loss
# 3pt - draw
# 6pt - win
#
# X = lose
# Y = draw
# Z = win


oppThrowIdx = 0
yourThrowIdx = 2


def ConvertThrow(throwChar):
    if throwChar == 'A' or throwChar == 'X': #Rock
        return 'R'
    if throwChar == 'B' or throwChar == 'Y': #Paper
        return 'P'
    if throwChar == 'C' or throwChar == 'Z': #Scissors
        return 'S'


def ConvertInstruction(oppThrowChar, yourThrowChar):
    if yourThrowChar == 'X': #Lose
        if oppThrowChar == 'R':
            return 'S'
        if oppThrowChar == 'P':
            return 'R'
        if oppThrowChar == 'S':
            return 'P'
    if yourThrowChar == 'Y': #Tie
        return oppThrowChar
    if yourThrowChar == 'Z': #Win    
        if oppThrowChar == 'R':
            return 'P'
        if oppThrowChar == 'P':
            return 'S'
        if oppThrowChar == 'S':
            return 'R'


def GetPointsForYourThrow(throwChar):
    if throwChar == 'R': #Rock
        return 1
    if throwChar == 'P': #Paper
        return 2
    if throwChar == 'S': #Scissors
        return 3


def GetPointsForResult(oppThrow, yourThrow):
    if oppThrow == yourThrow:
        return 3

    if oppThrow == 'R': #Rock
        if yourThrow == 'P': #Paper
            return 6
        if yourThrow == 'S': #Scissors
            return 0
    if oppThrow == 'P': #Paper
        if yourThrow == 'R': #Rock
            return 0
        if yourThrow == 'S': #Scissors
            return 6
    if oppThrow == 'S': #Scissors
        if yourThrow == 'R': #Rock
            return 6
        if yourThrow == 'P': #Scissors
            return 0      
    

def PartOne(data):
    totalPoints = 0
    for throw in data:
        oppThrow = throw[oppThrowIdx]
        yourThrow = throw[yourThrowIdx]
        oppThrow = ConvertThrow(oppThrow)
        yourThrow = ConvertThrow(yourThrow)
        totalPoints += GetPointsForYourThrow(yourThrow)
        totalPoints += GetPointsForResult(oppThrow, yourThrow)
    return totalPoints


def PartTwo(data):
    totalPoints = 0
    for throw in data:
        oppThrow = throw[oppThrowIdx]
        yourThrow = throw[yourThrowIdx]
        oppThrow = ConvertThrow(oppThrow)
        yourThrow = ConvertInstruction(oppThrow, yourThrow)
        totalPoints += GetPointsForYourThrow(yourThrow)
        totalPoints += GetPointsForResult(oppThrow, yourThrow)
    return totalPoints


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvRowsAsArray("aoc2022/Data/day2.txt")

    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
