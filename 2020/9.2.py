from itertools import combinations 

def is_valid(preamble, number):
    return number in [sum(pair) for pair in combinations(preamble, 2)]

xmas = []
with open('input9.txt') as f:
    for line in f:
        xmas.append(int(line))
f.closed

invalid_number = 0
preamble_size = 25
index = 0
for index in range(len(xmas)):
    preamble = xmas[index:index + preamble_size]
    number = xmas[index + preamble_size]
    if (not is_valid(preamble, number)):
        print(number)
        invalid_number = number
        break

for x in range(len(xmas)):
    for y in range(x + 1, len(xmas)):
        if (sum(xmas[x:y]) > number):
            break
        if (sum(xmas[x:y]) == number):
            print(min(xmas[x:y]) + max(xmas[x:y]))
            exit()
