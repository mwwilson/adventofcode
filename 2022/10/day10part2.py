f = open("day10input.txt", "r")
filestring = f.readlines()

cycleCount = {"addx": 2, "noop": 1}
currentCycle = 1
registerValue = 1
signalSum = 0
row = []

while len(filestring) > 0:
    instruction = filestring.pop(0).split()
    op = instruction[0]

    requiredCycles = cycleCount[op]
    for cycle in range(requiredCycles):
        if abs((currentCycle % 40) - registerValue - 1) <= 1:
            row.append('#')
        else:
            row.append(".")
        
        currentCycle = currentCycle + 1
        if op == "addx" and cycle == 1:
            operand = -1 if instruction[1][0] == '-' else 1
            registerValue = registerValue + (operand * int(instruction[1].strip('-')))
        if (currentCycle - 20) % 40 == 0:
            signalSum = signalSum + registerValue * currentCycle

line = []
for x in range(currentCycle - 1):
    line.append(row[x])
    if (x + 1) % 40 == 0:
        print(''.join(line))
        line = []