import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter

import decimal
import sys
import math
from decimal import *
from collections import defaultdict

'''
generate hash for all beacons with their 2 closest beacons (they formed a triangle with unique size) 
*count of unique hash is the answer for part1

with beacon hashes of scanner-0, match beacon hashes from other scanners. 1 matched hash from each scanner is enough.

get xyz translations from the matched beacon and its triangular peers, and its scanner xyz is known.

with the xyz translations found, import all beacons from known scanners to extend scanner-0 coverage

repeat 1-4 until all scanners found
'''

def GetRotations(scanner):
    return [scanner]


def GetActualDistance(beacon1, beacon2):
    xDist = beacon1['x'] - beacon2['x']
    yDist = beacon1['y'] - beacon2['y']
    zDist = beacon1['z'] - beacon2['z']
    total = (xDist**2)+(yDist**2)+(zDist**2)
    return math.sqrt(total)


def GetDistancesOfBeacons(scanners):
    distances = defaultdict(list)
    for i, scanner in enumerate(scanners):
        for j, beaconA in enumerate(scanner):
            beaconADistances = []
            for k, beaconB in enumerate(scanner):
                if j == k:
                    continue
                beaconADistances.append(GetActualDistance(beaconA, beaconB))
            beaconADistances.sort()
            distances[sum(beaconADistances[:2])].append((i,j))
    return distances


def GetDistancesOfBeacons(scanners):
    distances = []
    for scanner in scanners:
        scannerDists = []
        for j, beaconA in enumerate(scanner):
            beaconADistances = []
            for k, beaconB in enumerate(scanner):
                if j == k:
                    continue
                beaconADistances.append(GetActualDistance(beaconA, beaconB))
            beaconADistances.sort()
            distances[sum(beaconADistances[:2])].append((k,j))
    return distances



def PartOne(data):
    distances = GetDistancesOfBeacons(data)
    return len(distances)


def PartTwo(data):
    distances = GetDistancesOfBeacons(data)
    positionedScanners = [0]

    return 0


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetAs3dPointBeaconArray("aoc2021/Data/daynineteen.csv")

    partOneResult = PartOne(data)
    print("Day Nineteen - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Nineteen - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
