import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

from collections import defaultdict
import copy

start = 'start'
end = 'end'


def DataToCaveDictionary(data):
    cave = defaultdict(list)
    for line in data:
        connection = line.split('-')
        room1 = connection[0]
        room2 = connection[1]
        cave[room1].append(room2)
        cave[room2].append(room1)
    return cave


def Traverse(cave, curRoom, curRoute, finishedRoutes, canVisitSmallRoomTwice=False):
    myCave = copy.deepcopy(cave)
    curRoute.append(curRoom)
    if curRoom == 'end':
        finishedRoutes.append(curRoute)
    else:
        possibleNextRooms = myCave[curRoom]
        for nextRoom in possibleNextRooms:
            newRoute = copy.deepcopy(curRoute)
            if nextRoom.islower() and nextRoom in curRoute:
                if canVisitSmallRoomTwice:
                    if nextRoom == 'start':
                        continue
                    Traverse(myCave, nextRoom, newRoute, finishedRoutes, False)
                continue
            Traverse(myCave, nextRoom, newRoute,
                     finishedRoutes, canVisitSmallRoomTwice)
    return finishedRoutes


def PartOne(data):
    cave = DataToCaveDictionary(data)
    routes = Traverse(cave, 'start', [], [])
    return len(routes)


def PartTwo(data):
    cave = DataToCaveDictionary(data)
    routes = Traverse(cave, 'start', [], [], True)
    return len(routes)


testData1 = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvRowsAsArray("aoc2021/Data/daytwelve.csv")

    partOneResult = PartOne(data)
    print("Day Twelve - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Twelve - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
