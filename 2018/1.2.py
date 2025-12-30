taken = set([])
x = 0
with open('input.txt') as f:
    while True:
        line = f.readline()
        if len(line.strip()) == 0 :
            f.seek(0)
            line = f.readline()
        x = x + int(line)
        if x in taken:
            break
        taken.add(x)
f.closed
print(x)