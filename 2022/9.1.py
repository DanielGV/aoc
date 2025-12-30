moves = []
with open('input9.txt') as f:
    for line in f:
        moves.append(line.strip().split(' '))

print(moves)

def move_head(head, dir):
    match dir:
        case 'U': return (head[0], head[1]+1)
        case 'D': return (head[0], head[1]-1)
        case 'R': return (head[0]+1, head[1])
        case 'L': return (head[0]-1, head[1])
        case _: exit(1)

def move_tail(tail, head):
    dx = head[0]-tail[0]
    dy = head[1]-tail[1]
    # Directly aligned - move 1 dir
    if (abs(dx)>1 and dy==0):
        return (tail[0]+int(dx/abs(dx)),tail[1])
    if (dx==0 and abs(dy)>1):
        return (tail[0],tail[1]+int(dy/abs(dy)))
    # Not directly aligned - move diagonal
    if (abs(dx)>1 or abs(dy)>1):
        return (tail[0]+int(dx/abs(dx)),tail[1]+int(dy/abs(dy)))
    # Not far enough, stay put
    return tail

visited = {(0,0)}
knots = [(0,0)]*10

for move in moves:
    dir = move[0]
    steps = int(move[1])
    for step in range(steps):
        knots[0] = move_head(knots[0], dir)
        for k in range(1, len(knots)):
            knots[k] = move_tail(knots[k], knots[k-1])
        visited.add(knots[-1])
        # print(knots, visited)

print(len(visited))