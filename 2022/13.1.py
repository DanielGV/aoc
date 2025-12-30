lines = []
with open('input13.txt') as f:
    for line in f:
        lines.append(line.strip())

print(lines)

def compare(left, right):
    # print(f'Comparing: {left} AND {right}')
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

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if not compare(array[j], array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

divider1 = [[2]]
divider2 = [[6]]
packets = []
packets.append(divider1)
packets.append(divider2)
i = 0
while i < len(lines):
    packets.append(eval(lines[i]))
    packets.append(eval(lines[i+1]))
    i += 3

sorted = bubble_sort(packets)
print((sorted.index(divider1)+1) * (sorted.index(divider2)+1))