from itertools import combinations 

def adjacent(layout, x, y):
    fromx, tox, fromy, toy = max(x-1,0),min(x+1, len(layout))+1,max(y-1,0),min(y+1, len(layout[x]))+1
    return ''.join([line[fromy:toy] for line in layout[fromx:tox]])

def updated(layout, x, y):
    seat = layout[x][y]
    if (empty(seat) and not any(map(occupied, adjacent(layout, x, y)))):
        return '#'
    elif (occupied(seat) and sum(map(occupied, adjacent(layout, x, y))) > 4):
        return 'L'
    else:
        return seat

def seat(seat):
    return empty(seat) or occupied(seat)

def empty(seat):
    return seat == 'L'

def occupied(seat):
    return seat == '#'

def floor(seat):
    return seat == '.'

layout = []
with open('input11.txt') as f:
    for line in f:
        layout.append(line.strip())
f.closed

print('\n'.join(layout))
while True:
    new_layout = layout.copy()
    for x in range(len(layout)):
        new_line = list(layout[x])
        for y in range(len(layout[x])):
            new_line[y] = updated(layout, x, y)
        new_layout[x] = ''.join(new_line)
    if (new_layout == layout):
        print(sum([sum(map(occupied, line)) for line in new_layout]))
        exit()
    layout = new_layout.copy()
