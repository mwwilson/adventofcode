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

knots = [(0,0)]*11
tailLocations = set()
tailLocations.add(knots[0])

for line in filestring:
    print(line)
    parts = line.split()
    direction = parts[0]
    step = int(parts[1])

    for x in range(step):
        knots[0] = adjustRopePos(direction, knots[0], True)
        
        if abs(knots[0][0] - knots[1][0]) > 1 or abs(knots[0][1] - knots[1][1]) > 1:
            secondPos = adjustRopePos(direction, knots[0], False)
            for knotIdx in reversed(range(2, len(knots))):
                knots[knotIdx] = knots[knotIdx - 1]
            knots[1] = secondPos

        # for knotIdx in range(1, len(knots)):
        #     if abs(knots[knotIdx - 1][0] - knots[knotIdx][0]) > 1 or abs(knots[knotIdx - 1][1] - knots[knotIdx][1]) > 1:
        #         knots[knotIdx] = adjustRopePos(direction, knots[knotIdx - 1], False)
        print(knots)
        tailLocations.add(knots[-1])

print(tailLocations)
print(len(tailLocations))