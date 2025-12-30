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
i = 0
while i < len(rucksacks):
    elf1 = set(rucksacks[i])
    elf2 = set(rucksacks[i+1])
    elf3 = set(rucksacks[i+2])
    badge = elf1 & elf2 & elf3
    if (len(badge) > 1 or len(badge) == 0):
        print('error', badge)
        exit()
    badgeprio = priority(list(badge)[0])
    totalprio += badgeprio
    print(i, badge, badgeprio)
    i += 3

print(totalprio)