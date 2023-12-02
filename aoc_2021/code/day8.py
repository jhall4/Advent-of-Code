import numpy
from utils import data_importer
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)


#              0       1*     2        3        4*      5         6       7*       8*        9
numbers = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
           "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]


def GetSegmentSizeProperties(numbers):
    segLengths = []
    for number in numbers:
        segLengths.append(len(number))
    digitsWithLength = numpy.zeros(8, dtype=int)
    for length in segLengths:
        digitsWithLength[length] += 1

    return segLengths, digitsWithLength


def part_one(data):
    _, digitsWithLengh = GetSegmentSizeProperties(numbers)
    numUniqueDigits = 0
    for segment in data:
        for output in segment[data_importer.OUTPUT_VALUE]:
            if digitsWithLengh[len(output)] == 1:
                numUniqueDigits += 1

    return numUniqueDigits


def part_two(data):
    segLenths, digitsWithLengh = GetSegmentSizeProperties(numbers)
    total = 0
    for segment in data:
        # order strings
        for i, signal in enumerate(segment[data_importer.SIGNAL_VALUES]):
            segment[data_importer.SIGNAL_VALUES][i] = "".join(sorted(signal))
        for i, output in enumerate(segment[data_importer.OUTPUT_VALUE]):
            segment[data_importer.OUTPUT_VALUE][i] = "".join(sorted(output))

        scrambledNumbers = [''] * 10
        segmentLetters = [''] * 7  # T UL UR M LL LR B
        signals = segment[data_importer.SIGNAL_VALUES]
        signals.sort(key=len)
        letterCounts = {}
        # easy digits & letter counts
        for signal in signals:
            for letter in list(signal):
                if letter in letterCounts:
                    letterCounts[letter] += 1
                else:
                    letterCounts[letter] = 1
            signalLength = len(signal)
            if digitsWithLengh[signalLength] == 1:
                idx = segLenths.index(signalLength)
                scrambledNumbers[idx] = signal

        # top segment is in 7 but not 1
        for letter in list(scrambledNumbers[7]):
            if letter in scrambledNumbers[1]:
                continue
            segmentLetters[0] = letter
        # UL, UR, M, LR are in 4 (without 1) with counts of 6, 8, 7, 9 respectively
        for letter in list(scrambledNumbers[4]):
            if letterCounts[letter] == 8:
                segmentLetters[2] = letter
            elif letterCounts[letter] == 9:
                segmentLetters[5] = letter
            elif letterCounts[letter] == 6:
                segmentLetters[1] = letter
            elif letterCounts[letter] == 7:
                segmentLetters[3] = letter
        # occurance of remaining unknown segments LL: 4, B: 7
        for letter in letterCounts:
            if letter in segmentLetters:
                continue
            if letterCounts[letter] == 4:
                segmentLetters[4] = letter
            elif letterCounts[letter] == 7:
                segmentLetters[6] = letter

        # solve remaining numbers - 0,6,9,2,3,5
        for signal in signals:
            if signal in scrambledNumbers:
                continue
            if len(signal) == 6:  # 0,6,9
                if segmentLetters[2] in signal and segmentLetters[4] in signal:  # 0
                    scrambledNumbers[0] = signal
                elif segmentLetters[3] in signal and segmentLetters[4] in signal:  # 6
                    scrambledNumbers[6] = signal
                elif segmentLetters[3] in signal and segmentLetters[2] in signal:  # 9
                    scrambledNumbers[9] = signal
            elif len(signal) == 5:  # 2,3,5
                if segmentLetters[2] in signal and segmentLetters[4] in signal:  # 2
                    scrambledNumbers[2] = signal
                elif segmentLetters[2] in signal and segmentLetters[5] in signal:  # 3
                    scrambledNumbers[3] = signal
                elif segmentLetters[1] in signal and segmentLetters[5] in signal:  # 5
                    scrambledNumbers[5] = signal

        # get the numbers in the output
        outputNums = []
        for outputStr in segment[data_importer.OUTPUT_VALUE]:
            outputNums.append(scrambledNumbers.index(outputStr))

        total += int("".join(map(str, outputNums)))

    return total


def main():
    """ Main program """
    # Code goes over here.
    data = data_importer.get_as_display_segment_array(
        "aoc_2021/data/dayeight.csv")

    part_one_result = part_one(data)
    print("Day Eight - Part One")
    print(f"Result: {part_one_result}")

    part_two_result = part_two(data)
    print("Day Eight - Part Two")
    print(f"Result: {part_two_result}")


if __name__ == "__main__":
    main()
