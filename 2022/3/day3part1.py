f = open("day3input.txt", "r")
filestring = f.readlines()

letters = []

for line in filestring:
    part1 = line[0:int(len(line) / 2)]
    part2 = line[int(len(line) / 2):]
    for char in part1:
        if part2.count(char) >= 1:
            letters.append(char)
            break

sum = 0
for char in letters:
    value = ord(char)
    if value <= 90 and value >= 65:
        sum = sum + (value - 38)
    if value <= 122 and value >= 97:
        sum = sum + (value - 96)

print(sum)