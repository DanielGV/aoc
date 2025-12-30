
def tree(tile):
    return tile == '#'

def gettile(line, column):
    return line[column % len(line)]

treemap = []
with open('input3.txt') as f:
    for line in f:
        treemap.append(line.strip())
f.closed

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

slopescolisions = 1
for slope in slopes:
    row = 0
    column = 0
    colisions = 0
    while row < len(treemap):
        line = treemap[row]
        tile = gettile(line, column)
        if (tree(tile)):
            colisions += 1
        print(row, column, tree(tile))
        column += slope[0]
        row += slope[1]
    print(colisions)
    slopescolisions *= colisions

print(slopescolisions)

        
    

