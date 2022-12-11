from collections import namedtuple
import sys
import pathlib
codeModulePath = pathlib.Path(__file__).parent.parent.parent
sys.path[0] = str(codeModulePath)

from Utils import DataImporter


dir = "dir"
file = "file"
File = namedtuple('File', 'type name size')
Dir = namedtuple('Dir', 'type name children')


def BuildFileSystem(data):
    rootDir = Dir(dir, "/", [])
    navList = [rootDir]
    for line in data:
        contents = line.split(' ')
        if contents[0] == '$':
            command = contents[1]
            if command == "cd":
                destination = contents[2]
                if destination == '/':
                    navList = [rootDir]
                elif destination == "..":
                    navList = navList[:-1]
                else:
                    for child in navList[-1].children:
                        if child.type == dir and child.name == destination:
                            navList.append(child)
                            break
            continue
        elif contents[0] == dir:
            navList[-1].children.append(Dir(dir, contents[1], []))
            continue
        else:
            navList[-1].children.append(File(file, contents[1], int(contents[0])))
            continue
    return rootDir


def GetDirSizes(node, sizesList):
    dirSize = 0
    for child in node.children:
        if child.type == file:
            dirSize += child.size
        else: #child.type == dir:
            childSize, sizesList = GetDirSizes(child, sizesList)
            dirSize += childSize
    sizesList.append(dirSize)
    return dirSize, sizesList
    
        
def PartOne(data):
    rootNode = BuildFileSystem(data)
    dirSizesList = []
    _, dirSizesList = GetDirSizes(rootNode, dirSizesList)
    
    sizeTotal = 0
    for dirSize in dirSizesList:
        if dirSize <= 100001:
            sizeTotal += dirSize
    return sizeTotal


def PartTwo(data):
    rootNode = BuildFileSystem(data)
    dirSizesList = []
    rootDirSize, dirSizesList = GetDirSizes(rootNode, dirSizesList)

    diskSize = 70000000
    spaceNeeded = 30000000
    minSpaceNeeded = spaceNeeded - (diskSize - rootDirSize)

    dirSizesList.sort()
    for size in dirSizesList:
        if size >= minSpaceNeeded:
            return size
    return 0


def main():
    """ Main program """
    # Code goes over here.
    data = DataImporter.GetCsvRowsAsArray("aoc2022/Data/day7.txt")

    partOneResult = PartOne(data)
    print("Day One - Part One")
    print("Result: {}".format(partOneResult))

    partTwoResult = PartTwo(data)
    print("Day One - Part Two")
    print("Result: {}".format(partTwoResult))


if __name__ == "__main__":
    main()
