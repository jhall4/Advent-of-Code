from Utils import DataImporter
import math
import copy


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


def PartOne(data):
    total = data[0]
    for i in range(1, len(data)):
        total = AddNumbers(total, data[i])
    return GetMagnitude(total)


def PartTwo(data):
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
    data = DataImporter.GetAsList("dayeighteen.csv")

    partOneResult = PartOne(data)
    print("Day Eighteen - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Eighteen - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
