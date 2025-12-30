import sys

def taxicabdist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

orbitmap = []
with open('inputday6.txt') as f:
    for line in f:
        orbitmap.append(line)
f.closed

orbits = { 'COM': 0 }

testorbitmap = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]

orbiters = [] #list(orbit.split(')')[1] for orbit in orbitmap)

while len(orbiters) != len(orbitmap):
    for orbit in orbitmap:
        orbitsides = orbit.split(')')
        orbitee = orbitsides[0]
        orbiter = orbitsides[1][:-1]
        #print(orbit, orbiter in orbiters, orbitee in orbits.keys())
        if (orbiter not in orbiters) and (orbitee in orbits.keys()):
            orbits[orbiter] = orbits[orbitee] + 1
            orbiters.append(orbiter)
    # print(len(orbiters))
    # print(orbits)


print(sum(orbits.values()))