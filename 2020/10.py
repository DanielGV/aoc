from itertools import combinations 

def is_valid(preamble, number):
    return number in [sum(pair) for pair in combinations(preamble, 2)]

adapters = [0]
with open('input10.txt') as f:
    for line in f:
        adapters.append(int(line))
f.closed

device = max(adapters) + 3
adapters.sort()

jolt_diffs = [0,0,0,0]
for i, adapter in enumerate(adapters):
    next_adapter = (adapters[i+1] if i < len(adapters)-1 else device)
    if (next_adapter - adapter <= 3):
        jolt_diffs[next_adapter - adapter] += 1
    else:
        print('error')

print(jolt_diffs)
print(jolt_diffs[1]*jolt_diffs[3])