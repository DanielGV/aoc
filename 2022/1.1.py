
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
    cals.append(cal)
            
print(cals)

maxcals = 0
for i in range(3):    
    maxcals += max(cals)
    cals.remove(max(cals))

print(maxcals)