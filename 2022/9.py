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
        return (tail[0]+(dx/abs(dx)),tail[1])
    if (dx==0 and abs(dy)>1):
        return (tail[0],tail[1]+(dy/abs(dy)))
    # Not directly aligned - move diagonal
    if (abs(dx)>1 or abs(dy)>1):
        return (tail[0]+(dx/abs(dx)),tail[1]+(dy/abs(dy)))
    # Not far enough, stay put
    return tail

visited = {(0,0)}
head = (0,0)
tail = (0,0)

for move in moves:
    dir = move[0]
    steps = int(move[1])
    for step in range(steps):
        head = move_head(head, dir)
        tail = move_tail(tail, head)
        visited.add(tail)
        # print(head, tail, visited)

print(len(visited))