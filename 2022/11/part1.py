import os

cur_path = os.path.dirname(__file__)
f = open(cur_path + "/input.txt", "r")
filestring = f.readlines()

class Monkey():
    def __init__(self, name):
        self.name = name
        self.items = []
        self.inspections = 0
        self.operation = ""
        self.operand = ""
        self.testDivisor = 1
        self.trueMonkey = ""
        self.falseMonkey = ""
    
    def __str__(self):
        return(f"Name: {self.name}\n\tItems: {str(self.items)}\n\tOperation: {self.operation}\n\tOperand: {self.operand}\n\t{str(self.testDivisor)}\n\tTrue: {self.trueMonkey}\n\tFalse: {self.falseMonkey}")
    
    def math(self, operation, item1, item2):
        if operation == "*":
            return item1 * item2
        if operation == "+":
            return item1 + item2

    def inspectItem(self, item):
        self.inspections = self.inspections + 1
        if self.operand == "old":
            operand = item
        else:
            operand = int(self.operand)
        return self.math(self.operation, item, operand)

    def monkeyToPass(self, item):
        if item % self.testDivisor == 0:
            return self.trueMonkey
        return self.falseMonkey

monkeys = {}

while len(filestring) > 0:
    line = filestring.pop(0)
    parts = line.split()
    if(len(parts) == 0):
        continue
    if parts[0] == "Monkey":
        monkeyName = parts[1].strip(':')
        constructedMonkey = Monkey(monkeyName)
        constructedMonkey.items = [int(x) for x in filestring.pop(0).strip()[16:].replace(',', '').split()]
        operation = filestring.pop(0).strip()[17:].split()
        constructedMonkey.operation = operation[1]
        constructedMonkey.operand = operation[2]
        constructedMonkey.testDivisor = int(filestring.pop(0).split()[-1])
        constructedMonkey.trueMonkey = filestring.pop(0).split()[-1]
        constructedMonkey.falseMonkey = filestring.pop(0).split()[-1]
        monkeys[monkeyName] = constructedMonkey

monkeyRounds = 20

for round in range(monkeyRounds):
    for monkeyName in monkeys:
        monkey = monkeys[monkeyName]
        while len(monkey.items) > 0:
            currentItem = monkey.items.pop(0)
            worryLevel = int(monkey.inspectItem(currentItem) / 3)
            passMonkey = monkey.monkeyToPass(worryLevel)
            monkeys[passMonkey].items.append(worryLevel)

maxMonkey = 0
max2Monkey = 0

for monkeyName in monkeys:
    monkey = monkeys[monkeyName]
    if monkey.inspections > maxMonkey:
        max2Monkey = maxMonkey
        maxMonkey = monkey.inspections
    elif monkey.inspections > max2Monkey:
        max2Monkey = monkey.inspections

print(maxMonkey * max2Monkey)
