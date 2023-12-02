import copy
from collections import defaultdict
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


start = 'start'
end = 'end'


def dataToCaveDictionary(data):
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


def part_one(data):
    cave = dataToCaveDictionary(data)
    routes = Traverse(cave, 'start', [], [])
    return len(routes)


def part_two(data):
    cave = dataToCaveDictionary(data)
    routes = Traverse(cave, 'start', [], [], True)
    return len(routes)


test_data1 = [
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
    data = data_importer.get_rows_as_array("aoc_2021/data/daytwelve.csv")

    part_one_result = part_one(data)
    print("Day Twelve - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Twelve - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
