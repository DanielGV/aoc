import re

zero_mask = 0
one_mask = 0
memory = {}

def apply_mask(value):
    return int(value) & zero_mask | one_mask

def write_to_mem(mem, value):
    global memory
    memory[mem] = apply_mask(value)

def update_mask(mask):
    global zero_mask, one_mask
    zero_mask = int(mask.replace('X', '1'), 2)
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

print(memory)
print(sum(memory.values()))