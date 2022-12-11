f = open("day8input.txt", "r")
filestring = f.readlines()

treeArray = []
def constructTreeArray():
    for line in filestring:
        treeRow = []
        for char in line.strip():
            treeRow.append(int(char))
        treeArray.append(treeRow)

constructTreeArray()
width = len(treeArray)
height = len(treeArray[0])

numVisible = 0
def checkVisible(treeX, treeY):
    visibleLeft = True
    visibleRight = True
    visibleTop = True
    visibleBottom = True
    for coord in range(0, treeX):
        if treeArray[coord][treeY] >= treeArray[treeX][treeY]: # check from the left
            visibleLeft = False
            break
    for coord in reversed(range(treeX + 1, width)):
        if treeArray[coord][treeY] >= treeArray[treeX][treeY]: # check from the right
            visibleRight = False
            break
    for coord in range(0, treeY):
        if treeArray[treeX][coord] >= treeArray[treeX][treeY]: # check from the top
            visibleTop = False
            break
    for coord in reversed(range(treeY + 1, height)):
        if treeArray[treeX][coord] >= treeArray[treeX][treeY]: # check from the bottom
            visibleBottom = False
            break
    return visibleLeft or visibleRight or visibleTop or visibleBottom
    
visibleTrees = 0
for x in range(width):
    for y in range(height):
        if checkVisible(x, y):
            visibleTrees = visibleTrees + 1

print(visibleTrees)
