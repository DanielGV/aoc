from itertools import combinations 

def is_valid(preamble, number):
    return number in [sum(pair) for pair in combinations(preamble, 2)]

xmas = []
with open('input9.txt') as f:
    for line in f:
        xmas.append(int(line))
f.closed

preamble_size = 25
index = 0
for index in range(len(xmas)):
    preamble = xmas[index:index + preamble_size]
    number = xmas[index + preamble_size]
    if (not is_valid(preamble, number)):
        print(number)
        exit()
