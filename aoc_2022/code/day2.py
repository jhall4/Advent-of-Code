import sys
import pathlib

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


# A, X = Rock
# B, Y = Paper
# C, Z = Scissors
#
# 1pt - throw Rock
# 2pt - throw Paper
# 3pt - throw Scissors
#
# 0pt - loss
# 3pt - draw
# 6pt - win
#
# X = lose
# Y = draw
# Z = win


OPP_THROW_IDX = 0
YOUR_THROW_IDX = 2


def convert_throw(throw_char):
    if throw_char == 'A' or throw_char == 'X':  # Rock
        return 'R'
    if throw_char == 'B' or throw_char == 'Y':  # Paper
        return 'P'
    if throw_char == 'C' or throw_char == 'Z':  # Scissors
        return 'S'


def convert_instruction(opp_throw_char, your_throw_char):
    if your_throw_char == 'X':  # Lose
        if opp_throw_char == 'R':
            return 'S'
        if opp_throw_char == 'P':
            return 'R'
        if opp_throw_char == 'S':
            return 'P'
    if your_throw_char == 'Y':  # Tie
        return opp_throw_char
    if your_throw_char == 'Z':  # Win
        if opp_throw_char == 'R':
            return 'P'
        if opp_throw_char == 'P':
            return 'S'
        if opp_throw_char == 'S':
            return 'R'


def get_points_for_your_throw(throw_char):
    if throw_char == 'R':  # Rock
        return 1
    if throw_char == 'P':  # Paper
        return 2
    if throw_char == 'S':  # Scissors
        return 3


def get_points_for_result(opp_throw, your_throw):
    if opp_throw == your_throw:
        return 3

    if opp_throw == 'R':  # Rock
        if your_throw == 'P':  # Paper
            return 6
        if your_throw == 'S':  # Scissors
            return 0
    if opp_throw == 'P':  # Paper
        if your_throw == 'R':  # Rock
            return 0
        if your_throw == 'S':  # Scissors
            return 6
    if opp_throw == 'S':  # Scissors
        if your_throw == 'R':  # Rock
            return 6
        if your_throw == 'P':  # Scissors
            return 0


def part_one(data):
    total_points = 0
    for throw in data:
        opp_throw = throw[OPP_THROW_IDX]
        your_throw = throw[YOUR_THROW_IDX]
        opp_throw = convert_throw(opp_throw)
        your_throw = convert_throw(your_throw)
        total_points += get_points_for_your_throw(your_throw)
        total_points += get_points_for_result(opp_throw, your_throw)
    return total_points


def part_two(data):
    total_points = 0
    for throw in data:
        opp_throw = throw[OPP_THROW_IDX]
        your_throw = throw[YOUR_THROW_IDX]
        opp_throw = convert_throw(opp_throw)
        your_throw = convert_instruction(opp_throw, your_throw)
        total_points += get_points_for_your_throw(your_throw)
        total_points += get_points_for_result(opp_throw, your_throw)
    return total_points


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_rows_as_array("aoc_2022/data/day2.txt")

    part_one_result = part_one(data)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
