them = []
me = []
with open('input2.txt') as f:
    for line in f:
        them.append(line.split(' ')[0].strip())
        me.append(line.split(' ')[1].strip())

total = 0
for i, move in enumerate(me):
    movescr = 0
    if move == 'X': movescr += 1
    if move == 'Y': movescr += 2
    if move == 'Z': movescr += 3
    smove = them[i]
    if (move == 'X' and smove == 'A') or (move == 'Y' and smove == 'B') or (move == 'Z' and smove == 'C'): movescr += 3
    if (move == 'X' and smove == 'C') or (move == 'Y' and smove == 'A') or (move == 'Z' and smove == 'B'): movescr += 6
    total += movescr
    print(smove, move)
    print(movescr)

print(total)
