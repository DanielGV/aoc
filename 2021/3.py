diagnostics = []
with open('input3.txt') as f:
    for line in f:
        diagnostics.append(str(line).strip())
f.closed

l = len(diagnostics[0])
gamma = ""
epsilon = ""

ones = [0] * l
zeroes = [0] * l
for diagnos in diagnostics:    
    for idx, bit  in enumerate(diagnos):
        if (bit == '0'):
            zeroes[idx] += 1
        elif (bit == '1'):
            ones[idx] += 1

for idx in range(l):
    if (ones[idx]>zeroes[idx]):
        epsilon += '0'
        gamma += '1'
    elif (ones[idx]<zeroes[idx]):
        epsilon += '1'
        gamma += '0'
    else:
        print('Even')


print('Gamma', gamma, int(gamma, 2))
print('Epsilon', epsilon, int(epsilon, 2))
consumption = int(gamma, 2) * int(epsilon, 2)
print('Consumption', consumption)
exit()
