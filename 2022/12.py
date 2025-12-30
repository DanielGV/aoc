heightmap = []
with open('input12.txt') as f:
    for line in f:
        heightmap.append(list(line.strip()))

print(heightmap)

start = (0, 0)
end = (0, 0)
for x, line in enumerate(heightmap):
    if 'S' in line:
        start = (x, line.index('S'))
    if 'E' in line:
        end = (x, line.index('E'))
    
heightmap[start[0]][start[1]] = 'a'
heightmap[end[0]][end[1]] = 'z'

print(start)
print(end)
print(heightmap)

def h(pos):
    return ord(heightmap[pos[0]][pos[1]])

def invalid(pos):
    return (pos[0]>=len(heightmap) or pos[0]<0 or pos[1]>=len(heightmap[0]) or pos[1]<0)

def valid_move(f, t):
    if invalid(f):
        return False
    return h(f) + 1 >= h(t)

def candidates(pos):
    cand = []
    if valid_move((pos[0]-1,pos[1]), pos):
        cand.append((pos[0]-1,pos[1]))
    if valid_move((pos[0]+1,pos[1]), pos):
        cand.append((pos[0]+1,pos[1]))
    if valid_move((pos[0],pos[1]-1), pos):
        cand.append((pos[0],pos[1]-1))
    if valid_move((pos[0],pos[1]+1), pos):
        cand.append((pos[0],pos[1]+1))
    return cand

pos = end
steps = 0
path = [ end ]

def transvers(path, pos):
    candits = candidates(pos)
    if not candits:
        return None
    patos = []
    for candit in candits:
        # print(f'from {path} investigate {candit}')
        if candit == start:
            return len(path)
        if candit not in path:
            patos.append(transvers(path + [candit], candit))
    return min(filter(lambda item: item is not None, patos), default=None)

print(transvers([end], end))
