import copy
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


flashPoint = 9
flashed = -9999


def IncrementAndFlash(octoGrid):
    for i, octoRow in enumerate(octoGrid):
        for j, octopus in enumerate(octoRow):
            octoGrid[i][j] += 1

    hasFlashed = True
    while hasFlashed:
        flashingOctos = []
        for i, octoRow in enumerate(octoGrid):
            for j, octopus in enumerate(octoRow):
                if octopus > flashPoint:
                    flashingOctos.append([i, j])

        for octopus in flashingOctos:
            v = octopus[0]
            h = octopus[1]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= i+v < len(octoGrid) and 0 <= j+h < len(octoGrid[0]):
                        octoGrid[i+v][j+h] += 1
            octoGrid[octopus[0]][octopus[1]] = flashed
        hasFlashed = len(flashingOctos) > 0


def part_one(data, runDepth):
    octoGrid = copy.deepcopy(data)
    numFlashes = 0

    for _ in range(runDepth):
        IncrementAndFlash(octoGrid)

        for i, octoRow in enumerate(octoGrid):
            for j, octopus in enumerate(octoRow):
                if octopus < 0:
                    numFlashes += 1
                    octoGrid[i][j] = 0

    return numFlashes


def part_two(data):
    octoGrid = copy.deepcopy(data)
    flashedSimultaneously = False
    step = 0

    while not flashedSimultaneously:
        step += 1
        IncrementAndFlash(octoGrid)

        flashedSimultaneously = True
        for i, octoRow in enumerate(octoGrid):
            for j, octopus in enumerate(octoRow):
                flashed = octopus < 0
                flashedSimultaneously = flashedSimultaneously and flashed
                if flashed:
                    octoGrid[i][j] = 0

    return step


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_2d_array("aoc_2021/data/dayeleven.csv")

    part_one_result = part_one(data, 100)
    print("Day Eleven - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Eleven - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
