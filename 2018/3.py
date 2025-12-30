def printfabric(fabricdef):
    for row in fabricdef:
        line = ''
        for column in row:
            line += str(column)
        print(line)

class Design:
    def __init__(self, designstr):
        #8 @ 431,568: 16x23
        id = int(designstr.split('@')[0][1:-1])
        self.id = int(designstr.split('@')[0][1:-1])
        dimensions = designstr.split('@')[1][1:]
        self.left = int(dimensions.split(':')[0].split(',')[0])
        self.top = int(dimensions.split(':')[0].split(',')[1])
        self.width = int(dimensions.split(':')[1].split('x')[0])
        self.height = int(dimensions.split(':')[1].split('x')[1])

fabric = [[0] * 1000 for i in range(1000)]
with open('input3.txt') as f:
    for line in f:
        design = Design(line)
        #print('#{} @ {},{}: {}x{}'.format(design.id, design.left, design.top, design.width, design.height))
        #print('#{} @ {}-{}x{}-{}'.format(design.id, design.left, design.left + design.width, design.top, design.top + design.height))
        for x in range(design.left, design.left + design.width):
            for y in range(design.top, design.top + design.height):
                #print('#{} marking {}x{}'.format(design.id,x,y))
                fabric[x][y] = fabric[x][y] + 1
                #printfabric(fabric)
f.closed

printfabric(fabric)
colisions = 0
for row in fabric:
    for column in row:
        if column > 1:
            colisions += 1

print(colisions)

