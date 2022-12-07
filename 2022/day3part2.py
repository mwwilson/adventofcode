f = open("day3input.txt", "r")
filestring = f.readlines()

letters = []

for index in range(2, len(filestring), 3):
    for char in filestring[index]:
        if filestring[index - 1].count(char) > 0 and filestring[index - 2].count(char) > 0:
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