def distance(p, q):
  return abs(p[0]-q[0]) + abs(p[1]-q[1])

points = []
with open('input6.txt') as f:
  for line in f:
    coords = line.split(',')
    points.append([int(coords[0]), int(coords[1])])
f.closed

print(points)

quads = [[0] * 600 for i in range(600)]
for x in range(600):
  for y in range(600):
    closest = 600 * 2
    for i, point in enumerate(points):
      dist = distance(point, [x, y])
      if (dist < closest):
        quads[x][y] = i
        closest = dist
      elif (dist == closest):
        quads[x][y] = None
        closest = dist

print(quads)

sums = dict({})
for x in range(600):
  for y in range(600):
    i = quads[x][y]
    if (i in sums):
      sums[i] = sums[i] + 1
    else:
      sums[i] = 1

print(sums)

for a in [0,599]:
  for b in range(600):
    if quads[a][b] in sums:
      del sums[quads[a][b]]
    if quads[b][a] in sums:
      del sums[quads[b][a]]

s = [(k, sums[k]) for k in sorted(sums, key=sums.get, reverse=True)]
print (s)
