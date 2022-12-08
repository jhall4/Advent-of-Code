import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter


def GetIllegalCharScore(illegalChars):
    score = 0
    for char in illegalChars:
        if char == ')':
            score += 3
        elif char == ']':
            score += 57
        elif char == '}':
            score += 1197
        elif char == '>':
            score += 25137
    return score

def GetCompletedCharScore(completedCharsLines):
    scores = []
    for line in completedCharsLines:
        score = 0
        for char in line:
            score = score * 5
            if char == ')':
                score += 1
            elif char == ']':
                score += 2
            elif char == '}':
                score += 3
            elif char == '>':
                score += 4
        scores.append(score)
    scores.sort()
    middleIdx = int((len(scores) - 1)/2)
    return scores[middleIdx]
                

def BracketsMatch(open, close):
    if (open == '(' and close == ')') or (open == '[' and close == ']') \
    or (open == '{' and close == '}') or (open == '<' and close == '>'):
        return True
    return False

def GetClosingBracket(openingBracket):
    if openingBracket == '(':
        return ')'
    elif openingBracket == '[':
        return ']'
    elif openingBracket == '{':
        return '}'
    elif openingBracket == '<':
        return '>'



def PartOne(data):
    illegalChars = []
    for line in data:
        chars = list(line)
        chunks = []
        for char in chars:
            if char == '(' or char == '[' or char == '{' or char == '<':
                chunks.append(char)
            else:
                chunkOpening = chunks.pop()
                if BracketsMatch(chunkOpening, char):
                    continue
                illegalChars.append(char)
                break

    return GetIllegalCharScore(illegalChars)


def PartTwo(data):
    completedChars = []
    for line in data:
        chars = list(line)
        chunks = []
        for char in chars:
            if char == '(' or char == '[' or char == '{' or char == '<':
                chunks.append(char)
            else:
                chunkOpening = chunks.pop()
                if BracketsMatch(chunkOpening, char):
                    continue
                chunks = []
                break

        if len(chunks) > 0:
            completedLineChars = []
            for remainingChunk in chunks:
                completedLineChars.insert(0,GetClosingBracket(remainingChunk))
            completedChars.append(completedLineChars)
        
    return GetCompletedCharScore(completedChars)


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvRowsAsArray("aoc2021/Data/dayten.csv")

    partOneResult = PartOne(data)
    print("Day Ten - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day Ten - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
