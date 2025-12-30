lines = []
with open('input13.txt') as f:
    for line in f:
        lines.append(line.strip())

print(lines)

pairs = []
i = 0
while i < len(lines):
    pairs.append((lines[i],lines[i+1]))
    i += 3

def compare(left, right):
    print(f'Comparing: {left} AND {right}')
    if (type(left) is int and type(right) is int):
        if left == right:
            return None
        else:
            return left < right
    elif (type(left) is list and type(right) is list):
        for i in range(len(left)):
            if i >= len(right):
                return False
            res = compare(left[i], right[i])
            if (res is not None):
                return res
        if len(left) < len(right):
            return True
    elif (type(left) is list and type(right) is int):
        return compare(left, [right])
    elif (type(left) is int and type(right) is list):
        return compare([left], right)
    else:
        print('Superbad')

sum = 0
for i, pair in enumerate(pairs):
    print(i+1, pair[0], pair[1])
    idx = i + 1
    left = eval(pair[0])
    right = eval(pair[1])
    res = compare(left, right)
    if res:
        sum += idx
        print(f'{idx} in order')
    else:
        print(f'{idx} NOT in order')
    
print(sum)