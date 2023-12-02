# import csv
# from typing import List
import math
import pathlib
from os.path import exists
import json
import numpy


def get_path_on_disk(file_name):
    basic_path = pathlib.Path(__file__)
    # path = pathlib.Path(__file__).parent.parent.parent / "data" / file_name
    path = basic_path.parent.parent / file_name
    return path


def get_numbers_from_string(string):
    if not isinstance(string, str):
        return []

    numbers = [int(i) for i in string.split() if i.isdigit()]
    return numbers


def get_file_as_string(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return ""
    with open(path, encoding="utf-8") as file:
        contents = file.read()
    return contents


def get_rows_as_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    return list(contents.split("\n"))


def get_rows_as_multidimensional_array(file_name, delim):
    file_array = get_rows_as_array(file_name)

    for entry in file_array:
        split_line = entry.split(delim)
        entry = split_line

 #   for i in range(len(file_array)):
 #       split_line = file_array[i].split(delim)
 #       file_array[i] = split_line

    return file_array


def get_as_multidimensional_array(file_name, delim1, delim2, delim3):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, newline="", encoding="utf-8") as file:
        contents = file.read()

    top_level = contents.split(delim1)
    for i in range(len(top_level)):
        mid_level = top_level[i].split(delim2)
        top_level[i] = mid_level
        for j in range(len(mid_level)):
            low_level = mid_level[j].split(delim3)
            top_level[i][j] = low_level
            # for k in range(len(low_level)):
            #    value = low_level[k]
            #    top_level[i][j][k] = value

    return top_level


def get_as_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        array = numpy.loadtxt(file, delimiter=",", dtype=int)

    return array.flatten().tolist()


def get_as_3d_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, newline="", encoding="utf-8") as file:
        contents = file.read()

    top_level = contents.split("\n\n")
    for i in range(len(top_level)):
        mid_level = top_level[i].split("\n")
        top_level[i] = mid_level
        for j in range(len(mid_level)):
            low_level = mid_level[j].split()
            top_level[i][j] = low_level
            for k in range(len(low_level)):
                value = low_level[k]
                top_level[i][j][k] = int(value)

    return top_level


def get_as_start_end_point_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    lines = contents.split("\n")
    for i in range(len(lines)):
        line = lines[i].split(" -> ")
        lines[i] = line
        for j in range(len(line)):
            point = line[j].split(",")
            lines[i][j] = point
            for k in range(len(point)):
                value = point[k]
                lines[i][j][k] = int(value)

    return lines


SIGNAL_VALUES = "signalValues"
OUTPUT_VALUE = "outputValue"


def get_as_display_segment_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    segments = []
    lines = contents.split("\n")
    for line in lines:
        split_line = line.split(" | ")
        segment = {}
        segment[SIGNAL_VALUES] = split_line[0].split(" ")
        segment[OUTPUT_VALUE] = split_line[1].split(" ")
        segments.append(segment)

    return segments


def get_as_2d_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    lines = contents.split("\n")
    for i in range(len(lines)):
        lines[i] = list(map(int, list(lines[i])))

    return lines


def get_as_points_and_folds(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    sections = contents.split("\n\n")
    points = sections[0].split("\n")
    folds = sections[1].split("\n")

    for i, point in enumerate(points):
        points[i] = numpy.fromstring(point, dtype=int, sep=",").tolist()

    unneeded_info = "fold along "
    for i, fold in enumerate(folds):
        fold = fold.replace(unneeded_info, "")
        fold = fold.split("=")
        fold[1] = int(fold[1])
        folds[i] = fold

    return points, folds


def get_as_string(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()
    return contents


def get_as_string_and_dict(file_name):
    string = ""
    dictionary = {}
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()
    sections = contents.split("\n\n")

    string = sections[0]
    entries = sections[1].split("\n")

    for entry in entries:
        (key, val) = entry.split(" -> ")
        dictionary[key] = val

    return string, dictionary


def get_string_between(string, left="", right=""):
    if (
        not isinstance(string, str)
        or not isinstance(left, str)
        or not isinstance(right, str)
    ):
        return ""
    if left not in string and right not in string:
        return ""
    left_search = 0
    if left != "" and left in string:
        left_search = string.index(left) + len(left)
    right_search = len(string)
    if right != "" and right in string:
        right_search = string.index(right)
    return string[left_search:right_search]


TOP_LEFT = "top_left"
BOTTOM_RIGHT = "bottom_right"


def get_as_rect(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    find_x = "x="
    find_y = "y="
    x_string = get_string_between(contents, find_x, ",")
    y_string = get_string_between(contents, find_y)
    xs = x_string.split("..")
    ys = y_string.split("..")

    rect = {}
    rect[TOP_LEFT] = {"x": int(xs[0]), "y": int(ys[1])}
    rect[BOTTOM_RIGHT] = {"x": int(xs[1]), "y": int(ys[0])}

    return rect


def get_as_list(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    lines = contents.split("\n")
    file_list = []
    for line in lines:
        file_list.append(json.loads(line))
    return file_list


def get_as_3d_point_beacon_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()

    lines = contents.split("\n")
    scanners = []
    current_scanner = None
    for line in lines:
        if "scanner" in line:
            if current_scanner:
                scanners.append(current_scanner)
            current_scanner = []
            continue
        if not line.strip():
            continue
        coords = line.split(",")
        current_scanner.append(
            {"x": int(coords[0]), "y": int(coords[1]), "z": int(coords[2])}
        )
    scanners.append(current_scanner)
    return scanners


def get_new_line_delimited_file_as_2d_int_array(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()
    lines = contents.split("\n")

    top_level_array = []
    second_level_array = []
    for line in lines:
        if line != "":
            second_level_array.append(int(line))
        else:
            top_level_array.append(second_level_array)
            second_level_array = []

    if len(second_level_array) > 0:
        top_level_array.append(second_level_array)
    return top_level_array


def get_as_stacks_and_moves(file_name):
    path = get_path_on_disk(file_name)
    if not exists(path):
        return []

    with open(path, encoding="utf-8") as file:
        contents = file.read()
    lines = contents.split("\n")

    stacks = []
    instructions = []

    for line in lines:
        if "[" in line:
            for i in range(math.ceil(len(line) / 4)):
                start = i * 4
                end = min(start + 4, len(line))
                crate = line[start:end].strip()
                if len(crate) > 0:
                    while len(stacks) < i + 1:
                        stacks.append([])
                    stacks[i].append(crate[1])
        elif "move" in line:
            instruction = [int(i) for i in line.split() if i.isdigit()]
            instructions.append(instruction)

    for stack in stacks:
        stack.reverse()
    return stacks, instructions
