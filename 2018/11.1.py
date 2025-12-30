serial = 3999
# serial = 42

def rackID(cell):
    return cell[0] + 10

def powerLevel(cell):
    power = rackID(cell)
    power = power * cell[1]
    power = power + serial
    power = power * rackID(cell)
    power = (power // 100) % 10
    power = power - 5
    return power

coords = range(1, 301)
grid = [[0] * 301 for i in range(301)]
gridp = [[0] * 301 for i in range(301)]
for x in coords:
    for y in coords:
        grid[x][y] = powerLevel([x, y])
        gridp[x][y] = powerLevel([x, y])


print(grid)

#square = range(3)
maxPow = 0
maxSquare = [0,0]
for s in range(2, 301):
    square = range(s)
    for x in range(301-s):
        for y in range(301-s):
            #print([x, y, s + 1])
            squarePow = gridp[x][y]
            for dx in square:
                squarePow += grid[x+dx][y+s-1]
            for dy in square:
                squarePow += grid[x+s-1][y+dy]
            squarePow -= grid[x+s-1][y+s-1]
            gridp[x][y] = squarePow
            if (squarePow > maxPow):
                maxPow = squarePow
                maxSquare = [x, y, s]
    print(s)
    print(maxSquare)
    print(maxPow)

print(maxSquare)
print(maxPow)
print([224, 222, 27])