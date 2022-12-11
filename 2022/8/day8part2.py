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
def scenicScore(treeX, treeY):
    leftScore = 0
    rightScore = 0
    topScore = 0
    bottomScore = 0
    for coord in reversed(range(0, treeX)):
        leftScore = leftScore + 1
        if treeArray[coord][treeY] >= treeArray[treeX][treeY]: # check from the left
            break
    for coord in range(treeX + 1, width):
        rightScore = rightScore + 1
        if treeArray[coord][treeY] >= treeArray[treeX][treeY]: # check from the right
            break
    for coord in reversed(range(0, treeY)):
        topScore = topScore + 1
        if treeArray[treeX][coord] >= treeArray[treeX][treeY]: # check from the top
            break
    for coord in range(treeY + 1, height):
        bottomScore = bottomScore + 1
        if treeArray[treeX][coord] >= treeArray[treeX][treeY]: # check from the bottom
            break
    return leftScore * rightScore * topScore * bottomScore
    
bestScenic = 0
for x in range(width):
    for y in range(height):
        current = scenicScore(x, y)
        if current > bestScenic:
            bestScenic = current

print(bestScenic)
