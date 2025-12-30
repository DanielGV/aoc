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

pots = ('.' * 5) + pots + ('.' * 505) 

print(rules)
print(0, ':', pots)

sums = []
for gen in range(1, 500):
    newgen = ''
    for i, pot in enumerate(pots):
        if (i < 2 or i > len(pots)-2):
            newgen += '.'
            continue
        newgen += rules[spreadValue(spreadSource(pots, i))]
    pots = newgen
    sumi = 0
    for i, pot in enumerate(pots):
        if pot == '#':
            sumi += i - 5
    print(gen, ':', pots, sumi)
    sums.append(sumi)

# Calculated the first 500 generations, seems like the increase converge

print(sums)
diffs = []
for i, sumi in enumerate(sums):
    if i < len(sums)-1:
        # print(sumi, sums[i+1], sums[i+1] - sumi)
        diffs.append(sums[i+1] - sumi)
print(diffs)
print(sum(diffs)/len(diffs))

# See the linear growth of each generation, seems to be exactly 109 from the ~100 generation

# Let's calculate the X generation, vased on the value att generation 499 which is 55557 and progress linearly with 109
val = 55557
startgen = 499
goalgen = 50000000000
genstoiterate = goalgen - startgen
step = 109
resval = val + genstoiterate * step
print(resval)

