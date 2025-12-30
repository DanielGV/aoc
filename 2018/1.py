
i = 0
with open('input.txt') as f:
    for line in f:
        i = i + int(line)
f.closed
print(i)