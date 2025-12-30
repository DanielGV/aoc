serial = 3999
#testserial = 42

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
square = range(3)
maxPow = 0
maxSquare = [0,0]
for x in coords:
    for y in coords:
        squarePow = 0
        for dx in square:
            for dy in square:
                squarePow += powerLevel([x+dx,y+dy])
        if (squarePow > maxPow):
            maxPow = squarePow
            maxSquare = [x, y]

print(maxSquare)
print(maxPow)