import sys

def taxicabdist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

wiredefs = []
with open('inputday3.txt') as f:
    for line in f:
        wiredefs.append(line)
f.closed

wire0 = list([])
wire1 = list([])

pos = [0,0]
for turn in wiredefs[0].split(","):
    direction = turn[0]
    length = int(turn[1:])
    if (direction=='U'):
        wire0.extend(list((x, pos[1]) for x in range(pos[0], pos[0] + length)))
        pos[0] = pos[0] + length
    elif (direction=='R'):
        wire0.extend(list((pos[0], y) for y in range(pos[1], pos[1] + length)))
        pos[1] = pos[1] + length
    elif (direction=='L'):
        wire0.extend(list((pos[0], y) for y in range(pos[1]-length, pos[1])))
        pos[1] = pos[1] - length
    elif (direction=='D'):
        wire0.extend(list((x, pos[1]) for x in range(pos[0]-length, pos[0])))
        pos[0] = pos[0] - length


pos = [0,0]
for turn in wiredefs[1].split(","):
    direction = turn[0]
    length = int(turn[1:])
    if (direction=='U'):
        wire1.extend(list((x, pos[1]) for x in range(pos[0], pos[0] + length)))
        pos[0] = pos[0] + length
    elif (direction=='R'):
        wire1.extend(list((pos[0], y) for y in range(pos[1], pos[1] + length)))
        pos[1] = pos[1] + length
    elif (direction=='L'):
        wire1.extend(list((pos[0], y) for y in range(pos[1]-length, pos[1])))
        pos[1] = pos[1] - length
    elif (direction=='D'):
        wire1.extend(list((x, pos[1]) for x in range(pos[0]-length, pos[0])))
        pos[0] = pos[0] - length

intersections = set(wire0).intersection(set(wire1))

closestdist = sys.maxsize
closestcross = (0,0)
for cross in intersections:
    if taxicabdist(cross, (0,0)) < closestdist:
        closestdist = taxicabdist(cross, (0,0))
        closestcross = cross

print(closestcross, closestdist)

def steps_taken(path, point):
    return path.index(point)

shortestdist = sys.maxsize
shortestcross = (0,0)
for cross in intersections:
    print(cross, steps_taken(wire0, cross), steps_taken(wire1, cross))
    walk = steps_taken(wire0, cross) + steps_taken(wire1, cross)
    if walk < shortestdist:
        shortestdist = walk
        shortestcross = cross

print(shortestcross, shortestdist)