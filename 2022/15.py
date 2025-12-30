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
intervals = []
beacons = set()
for scan in scans:
    result = re.search(r'Sensor at x=([-]?\d+), y=([-]?\d+): closest beacon is at x=([-]?\d+), y=([-]?\d+)', scan)
    sensor = (int(result.group(1)),int(result.group(2)))
    beacon = (int(result.group(3)),int(result.group(4)))
    sect = y_coverage(sensor, beacon, y)
    print(sensor, beacon, distance(sensor, beacon))
    print(y, sect)
    if beacon[1] == y:
        beacons.add(beacon[0])
    if sect:
        intervals.append(sect)
    
columns = set()
for rango in intervals:
    columns.update(range(rango[0], rango[1]+1))
for b in beacons:
    if b in columns:
        columns.remove(b)

print(len(columns))
