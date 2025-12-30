import sys

def taxicabdist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

orbitmap = []
with open('inputday6.txt') as f:
    for line in f:
        orbitmap.append(line)
f.closed

orbits = { 'COM': 0 }

#orbitmap = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","I)SAN","E)J","J)K","K)YOU","K)L"]

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

orbitdict = {}
for orbit in orbitmap:
    orbitsides = orbit.split(')')
    orbitee = orbitsides[0]
    orbiter = orbitsides[1][:-1]
    orbitdict[orbiter] = orbitee

def path_to_com(orbitdict, entity):
    path = [ entity ]
    visit = entity
    while (visit != 'COM'):
        path.append(orbitdict[visit])
        visit = orbitdict[visit]
    return path

san_to_com = path_to_com(orbitdict, 'SAN')
print("SAN to COM",san_to_com)
you_to_com = path_to_com(orbitdict, 'YOU')
print("YOU to COM",you_to_com)

common_path = set(san_to_com).intersection(set(you_to_com))
print("common planets", common_path)

farthest_from_com = ('COM', 0)
for planet in common_path:
    if (orbits[planet] > farthest_from_com[1]):
        farthest_from_com = (planet, orbits[planet])

print("farthest common planet", farthest_from_com)

you_to_farthest = orbits['YOU'] - 1 - farthest_from_com[1]
san_to_farthest = orbits['SAN'] - 1 - farthest_from_com[1]
both = you_to_farthest + san_to_farthest
print(both)

print(sum(orbits.values()))