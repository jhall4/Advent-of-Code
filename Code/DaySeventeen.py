from Utils import DataImporter
import sys

tl = DataImporter.topLeft
br = DataImporter.bottomRight
x = 'x'
y = 'y'


def IsInRect(point, rect):
    if point[x] >= rect[tl][x] and point[x] <= rect[br][x] and \
       point[y] <= rect[tl][y] and point[y] >= rect[br][y]:
        return True
    return False


def IsPastRect(point, rect):
    if point[x] > rect[br][x] or point[y] < rect[br][y]:
        return True
    return False


def LaunchProbe(vX, vY, position, rect, peak=0):
    position[x] += vX
    position[y] += vY
    peak = max(peak, position[y])
    if IsInRect(position, rect):
        return peak, True
    if IsPastRect(position, rect):
        return 0, False
    if vX > 0:
        vX -= 1
    if vX < 0:
        vX += 1
    vY -= 1

    return LaunchProbe(vX, vY, position, rect, peak)


def PartOne(data):
    xLimit = int(data[br][x] / 2)
    yLimit = int(abs(data[br][y]))
    peak = 0
    for vX in range(xLimit):
        for vY in range(yLimit):
            position = {x: 0, y: 0}
            highest, _ = LaunchProbe(vX, vY, position, data)
            peak = max(peak, highest)
    return peak


def PartTwo(data):
    xLimit = data[br][x] + 1
    yLimitLow = data[br][y] - 1
    yLimitHigh = abs(data[br][y]) + 1
    totalInZone = 0
    for vX in range(xLimit):
        for vY in range(yLimitLow, yLimitHigh):
            position = {x: 0, y: 0}
            _, landed = LaunchProbe(vX, vY, position, data)
            if landed:
                totalInZone += 1
    return totalInZone


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAsRect("dayseventeen.csv")

    partOneResult = PartOne(data)
    print("Day Seventeen - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Seventeen - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
