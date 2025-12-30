class Segment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def elems(self):
        if self.x1==self.x2:
            return [(self.x1, y) for y in rango(self.y1, self.y2)]
        elif self.y1==self.y2:
            return [(x, self.y2) for x in rango(self.x1, self.x2)]
        else:
            xs = rango(self.x1, self.x2)
            ys = rango(self.y1, self.y2)
            return [(xs[i], ys[i]) for i in range(len(xs))]

def rango(a, b):
    if a > b:
        rango = list(range(b, a + 1))
        rango.reverse()
        return rango
    elif b > a:
        return range(a, b + 1)
    else:
        print('NONO')

segments = []
with open('input5.txt') as f:
    line = f.readline()
    while line != '':
        s = line.replace('->', ' ').replace(',', ' ').strip().split()
        segments.append(Segment(s[0],s[1],s[2],s[3]))
        line = f.readline()
        print(s)


visited = dict()
for segment in segments:
    print(segment.elems())
    for point in segment.elems():
        if point in visited:
            visited[point] += 1
        else:
            visited[point] = 1

print(visited)

dangers = 0
for visit in visited:
    if visited[visit] >= 2:
        dangers += 1

print('Result', dangers)
exit()
