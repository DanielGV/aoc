def notintersect(elf1, elf2):
    return int(elf1[1]) < int(elf2[0]) or int(elf1[0]) > int(elf2[1])

def intersect(assignment: str):
    elf1 = assignment.split(',')[0].split('-')
    elf2 = assignment.split(',')[1].split('-')
    return not notintersect(elf2, elf1)
    
assignments = []
with open('input4.txt') as f:
    for line in f:
        assignments.append(line.strip())

duplications = 0
for assign in assignments:
    if (intersect(assign)):
        duplications += 1
    print(assign, intersect(assign))

print(duplications)
