
def consumption(mass):
    return (mass / 3) - 2

sums = 0
with open('inputday1.txt') as f:
    for line in f:
        module = consumption(int(line))
        latest = module
        while(consumption(latest)>0):
            module = module + consumption(latest)
            latest = consumption(latest)
        sums = sums + module
f.closed

print(sums)