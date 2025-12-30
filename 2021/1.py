entries = []
with open('input1.txt') as f:
    for line in f:
        entries.append(int(line))
f.closed

increase = 0
for idx in range(len(entries)-1):
    prev = entries[idx]
    next = entries[idx+1]
    if (next>prev):
        increase += 1
    print(prev, next, next>prev)

print(increase)
exit()
