f = open("day9input.txt", "r")
filestring = f.readlines()

def adjustRopePos(char, headPos, isHeadMovement):
    offset = 1 if isHeadMovement else -1

    if char == 'R':
        return (headPos[0] + offset, headPos[1])
    if char == 'L':
        return (headPos[0] - offset, headPos[1])
    if char == 'U':
        return (headPos[0], headPos[1] - offset)
    if char == 'D':
        return (headPos[0], headPos[1] + offset)

headPos = (0,0)
tailPos = (0,0)
tailLocations = set()
tailLocations.add(tailPos)

for line in filestring:
    parts = line.split()
    direction = parts[0]
    step = int(parts[1])

    for x in range(step):
        headPos = adjustRopePos(direction, headPos, True)
        if abs(headPos[0] - tailPos[0]) > 1 or abs(headPos[1] - tailPos[1]) > 1:
            tailPos = adjustRopePos(direction, headPos, False)
        tailLocations.add(tailPos)

print(len(tailLocations))