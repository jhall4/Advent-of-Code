import sys
import pathlib

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


TOP_LEFT = data_importer.TOP_LEFT
BOTTOM_RIGHT = data_importer.BOTTOM_RIGHT
X = 'x'
Y = 'y'


def is_in_rect(point, rect):
    if point[X] >= rect[TOP_LEFT][X] and point[X] <= rect[BOTTOM_RIGHT][X] and \
       point[Y] <= rect[TOP_LEFT][Y] and point[Y] >= rect[BOTTOM_RIGHT][Y]:
        return True
    return False


def is_past_rect(point, rect):
    if point[X] > rect[BOTTOM_RIGHT][X] or point[Y] < rect[BOTTOM_RIGHT][Y]:
        return True
    return False


def launch_probe(v_x, v_y, position, rect, peak=0):
    position[X] += v_x
    position[Y] += v_y
    peak = max(peak, position[Y])
    if is_in_rect(position, rect):
        return peak, True
    if is_past_rect(position, rect):
        return 0, False
    if v_x > 0:
        v_x -= 1
    if v_x < 0:
        v_x += 1
    v_y -= 1

    return launch_probe(v_x, v_y, position, rect, peak)


def part_one(data):
    x_limit = int(data[BOTTOM_RIGHT][X] / 2)
    y_limit = int(abs(data[BOTTOM_RIGHT][Y]))
    peak = 0
    for v_x in range(x_limit):
        for v_y in range(y_limit):
            position = {X: 0, Y: 0}
            highest, _ = launch_probe(v_x, v_y, position, data)
            peak = max(peak, highest)
    return peak


def part_two(data):
    x_limit = data[BOTTOM_RIGHT][X] + 1
    y_limit_low = data[BOTTOM_RIGHT][Y] - 1
    y_limit_high = abs(data[BOTTOM_RIGHT][Y]) + 1
    total_in_zone = 0
    for v_x in range(x_limit):
        for v_y in range(y_limit_low, y_limit_high):
            position = {X: 0, Y: 0}
            _, landed = launch_probe(v_x, v_y, position, data)
            if landed:
                total_in_zone += 1
    return total_in_zone


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_rect("aoc_2021/data/dayseventeen.csv")

    part_one_result = part_one(data)
    print("Day Seventeen - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Seventeen - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
