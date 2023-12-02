import sys
import pathlib

from utils import data_importer

codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


def get_top_crate_string(stacks):
    crate_string = ""
    for stack in stacks:
        crate_string = crate_string + stack[-1]
    return crate_string


def part_one(stacks, instrustions):
    for instruction in instrustions:
        amt = instruction[0]
        src = instruction[1]-1
        dst = instruction[2]-1

        for _ in range(amt):
            crate = stacks[src].pop()
            stacks[dst].append(crate)
    return get_top_crate_string(stacks)


def part_two(stacks, instrustions):
    for instruction in instrustions:
        amt = instruction[0]
        src = instruction[1]-1
        dst = instruction[2]-1
        src_len = len(stacks[src])

        moved_crates = stacks[src][src_len-amt:src_len]
        stacks[src] = stacks[src][:-amt]
        stacks[dst].extend(moved_crates)
    return get_top_crate_string(stacks)


def main():
    """ Main program """
    # Code goes over here.
    stacks, instrustions = data_importer.get_as_stacks_and_moves(
        "aoc_2022/data/day5.txt")

    part_one_result = part_one(stacks, instrustions)
    print("Day One - Part One")
    print(f"Result: {part_one_result}")

    stacks, instrustions = data_importer.get_as_stacks_and_moves(
        "aoc_2022/data/day5.txt")
    part_two_result = part_two(stacks, instrustions)
    print("Day One - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
