f = open("day4input.txt", "r")
filestring = f.readlines()

pairs = 0
for line in filestring:
    elves = line.split(',')
    elf1range = [int(x) for x in elves[0].split('-')]
    elf2range = [int(x) for x in elves[1].split('-')]

    if elf1range[0] >= elf2range[0] and elf1range[1] <= elf2range[1]:
        pairs = pairs + 1
    elif elf1range[0] <= elf2range[0] and elf1range[1] >= elf2range[1]:
        pairs = pairs + 1

print(pairs)