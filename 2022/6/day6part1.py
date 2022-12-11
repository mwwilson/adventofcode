f = open("day6input.txt", "r")
filestring = f.readlines()[0]

for index in range(4, len(filestring)):
    duplicate = False
    marker = filestring[index-4:index]
    for char in marker:
        if marker.count(char) > 1:
            duplicate = True
    if duplicate == False:
        print(index)
        break
