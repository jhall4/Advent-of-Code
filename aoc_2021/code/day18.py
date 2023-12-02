import copy
import math
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def CombineNumbers(a, b):
    c = []
    c.append(copy.deepcopy(a))
    c.append(copy.deepcopy(b))
    return c


def ExplodeNumbers(number, depth=0, exploded=False):
    if depth == 4 and not exploded:  # explode
        return 0, True, [number[0], number[1]]

    updates = [0, 0]
    for i in range(len(number)):
        if type(number[i]) is list:
            number[i], exploded, updates = ExplodeNumbers(
                number[i], depth+1, exploded)
            inv = (i+1) % 2
            if not exploded:
                continue
            if type(number[inv]) is int:
                number[inv] += updates[inv]
                updates[inv] = 0
            else:
                temp = number[inv]
                while type(temp) != int:
                    if updates[i] == updates[inv] == 0:
                        break
                    if type(temp[i]) == int:
                        temp[i] += updates[inv]
                        updates[inv] = 0
                        break
                    else:
                        temp = temp[i]
            break
    return number, exploded, updates


def SplitNumbers(number, split=False):
    if type(number) is int:
        if number >= 10 and not split:  # split
            half = number / 2
            return [math.floor(half), math.ceil(half)], True
    else:
        for i in range(len(number)):
            number[i], split = SplitNumbers(number[i], split)
    return number, split


def AddNumbers(a, b):
    c = CombineNumbers(a, b)
    reduced = True
    while reduced:
        reduced = False
        c, reduced, _ = ExplodeNumbers(c)
        if reduced:
            continue
        c, reduced = SplitNumbers(c)
    return c


def GetMagnitude(number):
    if type(number) is int:
        return number
    return GetMagnitude(number[0]) * 3 + GetMagnitude(number[1]) * 2


def part_one(data):
    total = data[0]
    for i in range(1, len(data)):
        total = AddNumbers(total, data[i])
    return GetMagnitude(total)


def part_two(data):
    maxMagnitude = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            addedNumber = AddNumbers(data[i], data[j])
            magnitude = GetMagnitude(addedNumber)
            maxMagnitude = max(maxMagnitude, magnitude)
    return maxMagnitude


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_list("aoc_2021/data/dayeighteen.csv")

    part_one_result = part_one(data)
    print("Day Eighteen - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Eighteen - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
