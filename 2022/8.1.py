forest = []
with open('input8.txt') as f:
    for line in f:
        forest.append([int(char) for char in line.strip()])

scenics = [[0] * len(forest[0]) for i in range(len(forest))]

print(forest)
print(scenics)

rows = len(forest)
cols = len(forest[0])

def scenic_calc(x, y):
    tree = forest[x][y]
    # print(x,y,tree)
    left = 0
    for i in reversed(range(y)):
        # print('left', x,i,forest[x][i])
        left += 1
        if forest[x][i] >= tree:
            break
    right = 0
    for i in range(y+1, cols):
        # print('right', x,i,forest[x][i])
        right += 1
        if forest[x][i] >= tree:
            break
    top = 0
    for i in reversed(range(x)):
        # print('top', i,y,forest[i][y])
        top += 1
        if forest[i][y] >= tree:
            break
    down = 0
    for i in range(x+1, rows):
        # print('down', i,y,forest[i][y])
        down += 1
        if forest[i][y] >= tree:
            break
    scenic = left * right * top * down
    # print(top, left,right, down, scenic)
    return scenic

# check all inner trees
for x in range(1, rows-1):
    for y in range(1, cols-1):
        tree = forest[x][y]
        scenics[x][y] = scenic_calc(x,y)

print(scenics)

best_score = max(max(score for score in row) for row in scenics)
print(best_score)