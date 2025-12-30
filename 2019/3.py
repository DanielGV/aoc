import sys

def taxicabdist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

wiredefs = []
with open('inputday3.txt') as f:
    for line in f:
        wiredefs.append(line)
f.closed

wire0 = set([])
wire1 = set([])

pos = [0,0]
for turn in wiredefs[0].split(","):
    direction = turn[0]
    length = int(turn[1:])
    if (direction=='U'):
        wire0 |= set((x, pos[1]) for x in range(pos[0], pos[0] + length))
        pos[0] = pos[0] + length
    elif (direction=='R'):
        wire0 |= set((pos[0], y) for y in range(pos[1], pos[1] + length))
        pos[1] = pos[1] + length
    elif (direction=='L'):
        wire0 |= set((pos[0], y) for y in range(pos[1]-length, pos[1]))
        pos[1] = pos[1] - length
    elif (direction=='D'):
        wire0 |= set((x, pos[1]) for x in range(pos[0]-length, pos[0]))
        pos[0] = pos[0] - length

pos = [0,0]
for turn in wiredefs[1].split(","):
    direction = turn[0]
    length = int(turn[1:])
    if (direction=='U'):
        wire1 |= set((x, pos[1]) for x in range(pos[0], pos[0] + length))
        pos[0] = pos[0] + length
    elif (direction=='R'):
        wire1 |= set((pos[0], y) for y in range(pos[1], pos[1] + length))
        pos[1] = pos[1] + length
    elif (direction=='L'):
        wire1 |= set((pos[0], y) for y in range(pos[1]-length, pos[1]))
        pos[1] = pos[1] - length
    elif (direction=='D'):
        wire1 |= set((x, pos[1]) for x in range(pos[0]-length, pos[0]))
        pos[0] = pos[0] - length

crossings = wire0.intersection(wire1)

closestdist = sys.maxsize
closestcross = (0,0)
for cross in crossings:
    if taxicabdist(cross, (0,0)) < closestdist:
        closestdist = taxicabdist(cross, (0,0))
        closestcross = cross

print(closestcross, closestdist)