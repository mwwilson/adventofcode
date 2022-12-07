f = open("day5input.txt", "r")
filestring = f.readlines()

crates = []

def fillCrates():
    for line in filestring:
        if len(crates) == 0:
            for i in range(int((len(line)) / 4)):
                crates.append([])
        chars = line.strip()
        if len(chars) == 0 or chars[0] != '[':
            break
        for charIndex in range(len(line)):
            if line[charIndex].isalpha():
                rowNum = int((charIndex - 1) / 4)
                crates[rowNum].insert(0, line[charIndex])

def moveBoxes():
    for line in filestring:
        pieces = line.split()
        if len(pieces) == 0 or pieces[0] != 'move':
            continue
        
        numCrates = int(pieces[1])
        fromRow = int(pieces[3])
        toRow = int(pieces[5])
        for op in range(numCrates):
            transition = crates[fromRow - 1].pop()
            crates[toRow - 1].append(transition)

fillCrates()
moveBoxes()
print([x[-1] for x in crates])