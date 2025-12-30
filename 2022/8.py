forest = []
with open('input8.txt') as f:
    for line in f:
        forest.append([int(char) for char in line.strip()])

visibles = [[0] * len(forest[0]) for i in range(len(forest))]

print(forest)
print(visibles)

rows = len(forest)
cols = len(forest[0])

# left
for x in range(rows):
    lowest = -1
    for y in range(cols):
        col = forest[x][y]
        if col > lowest:
            visibles[x][y] += 1
            lowest = col
        # print(x,y,visibles)
# right
for x in range(rows):
    lowest = -1
    for y in reversed(range(cols)):
        col = forest[x][y]
        if col > lowest:
            visibles[x][y] += 1
            lowest = col
        # print(x,y,visibles)   
# top
for y in range(cols):
    lowest = -1
    for x in range(rows):
        col = forest[x][y]
        if col > lowest:
            visibles[x][y] += 1
            lowest = col
        # print(x,y,visibles)
# botom
for y in range(cols):
    lowest = -1
    for x in reversed(range(rows)):
        col = forest[x][y]
        if col > lowest:
            visibles[x][y] += 1
            lowest = col
        # print(x,y,visibles)
    
print(visibles)

visible = sum(sum(tree > 0 for tree in row) for row in visibles)
print(visible)