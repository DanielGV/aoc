them = []
play = []
with open('input2.txt') as f:
    for line in f:
        them.append(line.split(' ')[0].strip())
        play.append(line.split(' ')[1].strip())

total = 0
for i, move in enumerate(play):
    movescr = 0
    smove = them[i]
    svalue = (ord(smove) - ord('A')) + 1
    if move == 'X': 
        movescr += 0
        if svalue - 1 == 0: movescr += 3
        else: movescr += svalue - 1
    if move == 'Y': 
        movescr += 3
        movescr += svalue
    if move == 'Z': 
        movescr += 6
        if svalue + 1 == 4: movescr += 1
        else: movescr += svalue + 1
    total += movescr
    print(smove, move)
    print(movescr)

print(total)
