
def consumption(mass):
    return (mass / 3) - 2

sums = 0
with open('inputday1.txt') as f:
    for line in f:
        sums = sums + consumption(int(line))
f.closed

print(sums)