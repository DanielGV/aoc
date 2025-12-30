from itertools import permutations 

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def adjacent_occupied(layout, x, y):
    adjacents_busy = 0
    for direction in directions:
        pos = [x,y]
        for i in range(len(layout)):
            pos = pos[0] + direction[0], pos[1] + direction[1]
            if (0 > pos[0] or 0 > pos[1] or len(layout) <= pos[0] or len(layout[0]) <= pos[1]):
                break
            seat_pointer = layout[pos[0]][pos[1]]            
            if(occupied(seat_pointer)):
                adjacents_busy += 1
                break
            elif(empty(seat_pointer)):
                break
    return adjacents_busy

def updated(layout, x, y):
    seat = layout[x][y]
    if (empty(seat) and adjacent_occupied(layout, x, y) == 0):
        return '#'
    elif (occupied(seat) and adjacent_occupied(layout, x, y) >= 5):
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

def occupied_seats(layout):
    return sum([sum(map(occupied, line)) for line in new_layout])

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
    print('\n'.join(new_layout))
    if (new_layout == layout):
        print(occupied_seats(new_layout))
        exit()
    layout = new_layout.copy()
