import copy
from Utils import DataImporter


val = "val"
stamped = "stamped"

def Convert3dArrayToBingoBoards(array):
    boards = copy.deepcopy(array)
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, value in enumerate(row):
                boards[i][j][k] = {val:value, stamped:False}
    
    return boards


def IsBingoBoard(board):
    bHeight = len(board)
    if bHeight == 0:
        return False
    bWidth = len(board[0])
    if bWidth == 0:
        return False

    if  len(board[0][0]) == 1:
        return False

    if bWidth != bHeight:
        return False
    
    return True

def CheckBingo(board):
    if not IsBingoBoard(board):
        return False

    bSize = len(board)

    hBingo = False
    vBingo = False
    for i in range(bSize):
        if hBingo or vBingo:
            break

        hBingo = True
        vBingo = True
        for j in range(bSize):
            hVal = board[i][j]
            vVal = board[j][i]
            hBingo = hBingo and hVal[stamped]
            vBingo = vBingo and vVal[stamped]
    
    return hBingo or vBingo

def GetUnstampedTotal(board):
    if not IsBingoBoard(board):
        return 0
    
    unStampedTotal = 0
    for row in board:
        for value in row:
            if value[stamped] == False:
                unStampedTotal += value[val]

    return unStampedTotal


def PartOne(calls, boards):
    bingoBoards = Convert3dArrayToBingoBoards(boards)
    if not bingoBoards:
        return 0

    for call in calls:
        #mark the boards
        for i, board in enumerate(bingoBoards):
            for j, row in enumerate(board):
                for k, value in enumerate(row):
                    if value[val] == call:
                        bingoBoards[i][j][k][stamped] = True
                        if CheckBingo(bingoBoards[i]) == True:
                            unstampedTotal = GetUnstampedTotal(board)
                            return unstampedTotal * call

    return 0

def PartTwo(calls, boards):
    bingoBoards = Convert3dArrayToBingoBoards(boards)
    if not bingoBoards:
        return 0

    lastBoardToBingo = None
    lastCallToBingo = None
    bingoidxs = []
    
    for call in calls:
        #mark the boards
        for i, board in enumerate(bingoBoards):
            if i in bingoidxs:
                continue
            for j, row in enumerate(board):
                for k, value in enumerate(row):
                    if value[val] == call:
                        bingoBoards[i][j][k][stamped] = True
                        if CheckBingo(bingoBoards[i]) == True:
                            lastBoardToBingo = copy.deepcopy(board)
                            lastCallToBingo = copy.deepcopy(call)
                            bingoidxs.append(i)
                       
    unstampedTotal = GetUnstampedTotal(lastBoardToBingo)
    return unstampedTotal * lastCallToBingo


    

def main():
    """ Main program """
    # Code goes over here.
    calls = DataImporter.GetCsvAsArray("dayfour_calls.csv")
    boards = DataImporter.GetCsvAs3dArray("dayfour_boards.csv")

    partOneResult = PartOne(calls, boards)
    print("Day Four - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(calls, boards)
    print("Day Four - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()