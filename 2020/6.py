import functools

def group_yes(group):
    return len(set(functools.reduce(set.union, map(set, group))))
    
groups = []
group = []
with open('input6.txt') as f:
    for line in f:
        if (line == '\n'):
            groups.append(group)
            group = []
        else: 
            group.append(line.strip())
    groups.append(group)
f.closed

print(sum(map(group_yes, groups)))