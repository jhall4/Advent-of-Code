import sys
import pathlib
import math
from collections import defaultdict

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


'''
generate hash for all beacons with their 2 closest beacons (they formed a triangle with unique size) 
*count of unique hash is the answer for part1

with beacon hashes of scanner-0, match beacon hashes from other scanners. 1 matched hash from each scanner is enough.

get xyz translations from the matched beacon and its triangular peers, and its scanner xyz is known.

with the xyz translations found, import all beacons from known scanners to extend scanner-0 coverage

repeat 1-4 until all scanners found
'''


def get_rotations(scanner):
    return [scanner]


def get_actual_distance(beacon1, beacon2):
    x_dist = beacon1['x'] - beacon2['x']
    y_dist = beacon1['y'] - beacon2['y']
    z_dist = beacon1['z'] - beacon2['z']
    total = (x_dist**2)+(y_dist**2)+(z_dist**2)
    return math.sqrt(total)


def get_distances_of_beacons(scanners):
    distances = defaultdict(list)
    for i, scanner in enumerate(scanners):
        for j, beacon_a in enumerate(scanner):
            beacon_a_distances = []
            for k, beacon_b in enumerate(scanner):
                if j == k:
                    continue
                beacon_a_distances.append(
                    get_actual_distance(beacon_a, beacon_b))
            beacon_a_distances.sort()
            distances[sum(beacon_a_distances[:2])].append((i, j))
    return distances


def part_one(data):
    distances = get_distances_of_beacons(data)
    return len(distances)


def part_two(data):
    # distances = get_distances_of_beacons(data)
    # positionedScanners = [0]
    return data


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_3d_point_beacon_array(
        "aoc_2021/data/daynineteen.csv")

    part_one_result = part_one(data)
    print("Day Nineteen - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Nineteen - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
