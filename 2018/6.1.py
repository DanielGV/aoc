def distance(p, q):
  return abs(p[0]-q[0]) + abs(p[1]-q[1])

points = []
with open('input6.txt') as f:
  for line in f:
    coords = line.split(',')
    points.append([int(coords[0]), int(coords[1])])
f.closed

print(points)

limit = 10000
size = 0

quads = [[0] * 600 for i in range(600)]
for x in range(600):
  for y in range(600):
    sumdist = 0
    for point in points:
      sumdist = sumdist + distance(point, [x, y])
    quads[x][y] = sumdist
    if (sumdist < limit):
      size = size + 1
        
print(quads)
print(size)
