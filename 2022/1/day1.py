import sys

f = open("day1input.txt", "r")
filestring = f.read()

maxElf = sum(sorted([sum([int(z) for z in y]) for y in [x.split("\n") for x in filestring.split("\n\n")]], reverse=True)[0:int(sys.argv[1])])

print(maxElf)