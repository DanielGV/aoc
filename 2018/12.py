def spreadValue(spread):
    v = 0
    for i, s in enumerate(spread):
        if (s == '#'):
            v += 2**i
    return v

def spreadSource(array, pos):
    return array[pos-2:pos+3]

rules = dict({})
pots = ''
with open('input12.txt') as f:
  initial = f.readline()
  pots = initial[15:-1]
  f.readline()
  for line in f:
    spread = line[0:5]
    res = line[9]
    rules[spreadValue(spread)] = res
f.closed

pots = ('.' * 20) + pots + ('.' * 30) 

print(rules)
print(0, ':', pots)

for gen in range(1, 21):
    newgen = ''
    for i, pot in enumerate(pots):
        if (i < 2 or i > len(pots)-2):
            newgen += '.'
            continue
        newgen += rules[spreadValue(spreadSource(pots, i))]
    pots = newgen
    print(gen, ':', pots)

print('Fin')

sums = 0
for i, pot in enumerate(pots):
    if pot == '#':
        sums += i - 20

print(sums) # too high

sums = 0
for i, pot in enumerate('.#....##....#####...#######....#.#..##.'):
    if pot == '#':
        sums += i-3

print(sums)# too high


# corridory = '.#.#.##.##..#...#'
# source = spreadSource(corridory, 5)
# print(source)
# value = spreadValue(source)
# print(value)
