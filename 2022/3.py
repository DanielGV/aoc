def priority(item: chr):
    if item.isupper():
        return ord(item) - ord('A') + 27
    elif item.islower():
        return ord(item) - ord('a') + 1
    else:
        print('noletter', item)
        exit()

rucksacks = []
with open('input3.txt') as f:
    for line in f:
        rucksacks.append(line.strip())

totalprio = 0
for i, rucksack in enumerate(rucksacks):
    prio = 0
    compartment1 = set(rucksack[:int(len(rucksack)/2)])
    compartment2 = set(rucksack[int(len(rucksack)/2):])
    common = compartment1.intersection(compartment2)
    for misplaced in common:
        prio += priority(misplaced)
    totalprio += prio
    #print(compartment1, compartment2, common, prio)

print(totalprio)