scans = []
with open('input14.txt') as f:
    for line in f:
        scans.append(line.strip())

print(scans)

def unwrap(a, b):
    if a[0] == b[0]:
        return [(a[0], y) for y in range(min(a[1],b[1]), max(a[1],b[1]+1))]
    elif a[1] == b[1]:
        return [(x, a[1]) for x in range(min(a[0],b[0]), max(a[0],b[0]+1))]
    print(f'Not straigh line between {a} and {b}')
    exit(1)

rocks = set()
for scan in scans:
    vertex = []
    for point in scan.split('->'):
        coords = point.strip().split(',')
        vertex.append((int(coords[0]),int(coords[1])))
    for i in range(len(vertex)-1):
        rocks.update(set(unwrap(vertex[i], vertex[i+1])))

sand_source = (500, 0)

def sand_fall(pos, rocks):
    down = (pos[0], pos[1]+1)
    if down not in rocks:
        return down
    down_left = (pos[0]-1, pos[1]+1)
    if down_left not in rocks:
        return down_left
    down_right = (pos[0]+1, pos[1]+1)
    if down_right not in rocks:
        return down_right
    return pos

def feed_sand():
    pos = (sand_source[0], sand_source[1])
    x = 0
    while sand_fall(pos, rocks) != pos:
        pos = sand_fall(pos, rocks)
        # print(step, x, pos)
        # Catch infinite loop
        x += 1
        if x > 10000:
            print(f'Over the map on sand no: {step}')
            exit(0)
    rocks.add(pos)

print(rocks)
step = 0
while True:
    feed_sand()
    print(step)
    step += 1
