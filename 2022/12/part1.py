import os

cur_path = os.path.dirname(__file__)
f = open(cur_path + "/input.txt", "r")
filestring = f.readlines()

filestring = [x.strip() for x in filestring]
steps = []
coordinates = (-1,-1)
endCoords = (-1, -1)
for x in range(len(filestring)):
    stepRow = []
    for y in range(len(filestring[x])):
        if filestring[x][y] == "S":
            coordinates = (x,y)
            stepRow.append(0)
        else:
            stepRow.append(999)
        if filestring[x][y] == 'E':
            endCoords = (x,y)

    steps.append(stepRow)


def getNeighbors(x, y, map):
    neighbors = []
    if x != 0:
        neighbors.append((x - 1, y))
    if x != len(map) - 1:
        neighbors.append((x + 1, y))
    if y != 0:
        neighbors.append((x, y - 1))
    if y != len(map[0]) - 1:
        neighbors.append((x, y + 1))
    return neighbors

def isTraversible(fromCoord, toCoord):
    fromLetter = filestring[fromCoord[0]][fromCoord[1]]
    toLetter = filestring[toCoord[0]][toCoord[1]]
    if fromLetter == 'S':
        fromLetter = 'a'
    if toLetter == 'S':
        toLetter = 'a'
    if fromLetter == 'E':
        fromLetter = 'z'
    if toLetter == 'E':
        toLetter = 'z'
    if ord(toLetter) - ord(fromLetter) <= 1:
        return True
    return False

def distanceFromGoal(x, y, map):
    neighbors = getNeighbors(x, y, map)
    for coordPair in neighbors:
        if isTraversible((x,y), coordPair) and map[coordPair[0]][coordPair[1]] > map[x][y] + 1:
            map[coordPair[0]][coordPair[1]] = map[x][y] + 1
            distanceFromGoal(coordPair[0], coordPair[1], map)

distanceFromGoal(coordinates[0], coordinates[1], steps)
print(steps)
print(steps[endCoords[0]][endCoords[1]])