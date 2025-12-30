import re

x_mask = ''
one_mask = 0
memory = {}

def generate_combos(address):
    combos = ['']
    for bit in list(address):
        for combo in combos.copy():
            if bit != 'X':
                combos.remove(combo)
                combo += bit
                combos.append(combo)
            else:
                combos.remove(combo)
                combos.append(combo + '1')
                combos.append(combo + '0')
    return combos

def apply_mask(value):
    new_value = list(format(int(value) | one_mask, "36b").replace(' ', '0'))
    for i in range(len(new_value)):
        if x_mask[-i] == 'X':
            new_value[-i] = 'X'
    return ''.join(new_value)

def write_to_mem(mem, value):
    global memory
    addresses = generate_combos(apply_mask(mem))
    for address in addresses:
        memory[int(address,2)] = int(value)

def update_mask(mask):
    global x_mask, one_mask
    x_mask = mask.replace('1', '0')
    one_mask = int(mask.replace('X', '0'), 2)

mem_pattern = re.compile(r'mem\[(\d+)\] = (\d+)')
with open('input14.txt') as f:
    for line in f:
        if line.startswith('mask'):
            update_mask(line[7:-1])
        elif line.startswith('mem'):
            match = re.match(mem_pattern, line)
            write_to_mem(match.group(1), match.group(2))
f.closed

print(sum(memory.values()))