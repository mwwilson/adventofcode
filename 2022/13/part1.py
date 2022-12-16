import os

cur_path = os.path.dirname(__file__)
f = open(cur_path + "/input.txt", "r")
filestring = f.readlines()

def createList(line):
    toReturn = []
    idx = 1
    while idx < len(line):
        # print(f'line: {line}, idx: {idx}')
        if line[idx] == ',':
            idx = idx + 1
            continue
        elif line[idx] == '[': # opening of a sublist, need to find idx of the end
            openBraces = 1
            for subIdx in range(idx + 1, len(line)):
                # print(f'idx: {idx}, subIdx: {subIdx}, openBraces: {openBraces}, upcomingChar: {line[subIdx]}')
                if line[subIdx] == '[':
                    openBraces = openBraces + 1
                elif line[subIdx] == ']':
                    openBraces = openBraces - 1
                if openBraces == 0:
                    endIdx = subIdx + 1
                    break
            toReturn.append(createList(line[idx:endIdx]))
            idx = idx + (endIdx - idx)
            continue
        elif line[idx] == ']':
            return toReturn
        else:
            toReturn.append(int(line[idx]))
            idx = idx + 1

pairs = []
for idx in range(0, len(filestring), 3):
    pairs.append((createList(filestring[idx].strip()), createList(filestring[idx + 1].strip())))

def compareElements(left, right, skipLengthCheck=False):
    print(f'left: {left}, right: {right}')
    if isinstance(left, int):
        if isinstance(right, int):
            if left <= right:
                return True
            else:
                return False
        else:
            if len(right) == 0:
                return False
            return compareElements([left], right[0], True)
    else:
        if isinstance(right, int):
            if len(left) == 0:
                return True
            #return left[0] <= right
            return compareElements(left[0], [right], True)
    if len(left) > len(right):
        return False
    
    allSubItemsValid = True
    for idx in range(len(left)):
        if compareElements(left[idx], right[idx]) == False:
            allSubItemsValid = False
            break
    return allSubItemsValid

def getValidIndexes(items):
    indexes = []
    for idx in range(len(items)):
        left = items[idx][0]
        right = items[idx][1]
        if compareElements(left, right):
            indexes.append(idx + 1)
    return indexes

print(pairs)
multiplier = 0
for x in getValidIndexes(pairs):
    multiplier = multiplier + x

print(multiplier)