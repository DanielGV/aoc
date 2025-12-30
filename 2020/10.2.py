from itertools import combinations 

init = [1,1,2]
def tribonacci(n) :
    if n in {0, 1, 2}:
        return init[n]
    else :
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

adapters = [0]
with open('input10.txt') as f:
    for line in f:
        adapters.append(int(line))
f.closed

device = max(adapters) + 3
adapters.sort()

jolt_diffs = [0,0,0,0]
jolt_diff_list = []
for i, adapter in enumerate(adapters):
    next_adapter = (adapters[i+1] if i < len(adapters)-1 else device)
    if (next_adapter - adapter <= 3):
        jolt_diffs[next_adapter - adapter] += 1
        jolt_diff_list.append(next_adapter - adapter)
    else:
        print('error')

successive_one_jolts = []
acc = 0
for jolt_diff in jolt_diff_list:
    if (jolt_diff == 1):
        acc += 1
    elif (jolt_diff == 3 and acc > 0):
        successive_one_jolts.append(acc)
        acc = 0

paths = 1
for jump in successive_one_jolts:
    paths *= tribonacci(jump)

print(jolt_diffs)
print(jolt_diff_list)
print(successive_one_jolts)
print(paths)