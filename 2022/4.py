def contains(elf1, elf2):
    return int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])

def contained(assignment: str):
    elf1 = assignment.split(',')[0].split('-')
    elf2 = assignment.split(',')[1].split('-')
    return contains(elf1, elf2) or contains(elf2, elf1)
    
assignments = []
with open('input4.txt') as f:
    for line in f:
        assignments.append(line.strip())

duplications = 0
for assign in assignments:
    if (contained(assign)):
        duplications += 1
    print(assign, contained(assign))

print(duplications)
