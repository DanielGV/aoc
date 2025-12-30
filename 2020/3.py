
def tree(tile):
    return tile == '#'

def gettile(line, column):
    return line[column % len(line)]

treemap = []
with open('input3.txt') as f:
    for line in f:
        treemap.append(line.strip())
f.closed

row = 0
column = 0
slope = 3

colisions = 0
while row < len(treemap):
    line = treemap[row]
    tile = gettile(line, column)
    if (tree(tile)):
        colisions += 1
    print(row, column, tree(tile))
    row += 1
    column += slope

print(colisions)
        
    

