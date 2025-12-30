
cals = []
cal = 0
with open('input1.txt') as f:
    for line in f:
        if line == '\n':
            cals.append(cal)
            cal = 0
        else:
            lcal = int(line)
            cal += lcal
            
print(cals)

maxcals = max(cals)
print(maxcals)
