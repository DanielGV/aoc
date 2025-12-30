crabs = []
with open('input7.txt') as f:
    line = f.readline()
    crabs = list(map(int, line.strip().split(',')))
    

print('Initial state:', crabs)

fuels = []
for h in range(min(crabs), max(crabs)): # Optimizable with binary search
    fuel = 0
    for crab in crabs:
        dist = abs(crab - h)
        fuel += dist
    fuels.append((h, fuel))
    print(f'Position {h} consumes: {fuel}')

print(fuels)
print('Result', min(fuels, key = lambda x: x[1]))
exit()
