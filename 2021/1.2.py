entries = []
with open('input1.txt') as f:
    for line in f:
        entries.append(int(line))
f.closed

increase = 0
for idx in range(len(entries)-3):
    prev = sum(entries[idx:idx+3])
    next = sum(entries[idx+1:idx+4])
    if (next>prev):
        increase += 1
    print(prev, next, next>prev)

print(increase)
exit()
