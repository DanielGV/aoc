scans = []
with open('input15.txt') as f:
    for line in f:
        scans.append(line.strip())

print(scans)

def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def section(center, y, radius):
    d = abs(center[1] - y)
    p1 = center[0] + (radius - d)
    p2 = center[0] - (radius - d)
    return (p1, p2) if p1 < p2 else (p2, p1) 

def y_coverage(sensor, beacon, y:int):
    radius = distance(sensor, beacon)
    if (sensor[1] - radius <= y <= sensor[1] + y):
        print('In range')
        scanned = section(sensor, y, radius)
        return scanned
    return None

import re

y = 2000000
signals = []
for scan in scans:
    result = re.search(r'Sensor at x=([-]?\d+), y=([-]?\d+): closest beacon is at x=([-]?\d+), y=([-]?\d+)', scan)
    sensor = (int(result.group(1)),int(result.group(2)))
    beacon = (int(result.group(3)),int(result.group(4)))
    #sect = y_coverage(sensor, beacon, y)
    print(sensor, beacon, distance(sensor, beacon))
    #print(y, sect)
    signals.append((sensor, distance(sensor, beacon)))    

constrains = (0, 4000000)

def tuning_frequency(p):
    return p[0] * 4000000 + p[1]

figures = []
for signal in signals:
    center = signal[0]
    radius = signal[1]
    up = (center[0], center[1]+radius)
    down = (center[0], center[1]-radius)
    left = (center[0]+radius, center[1])
    right = (center[0]-radius, center[1])

for y in range(constrains[0], constrains[1]):
    for x in range(constrains[0], constrains[1]):
        loc = (x,y)
        found = False
        for signal in signals:
            if (distance(loc, signal[0]) <= signal[1]):
                found = True
                break
        if not found:
            print(loc)

            