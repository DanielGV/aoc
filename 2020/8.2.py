import sys

acc0 = 0
pos = 0
visited = []

def instruction(line):
    return line[0:3], int(line[4:].strip())

def acc(input):
    global acc0, pos
    acc0 += input
    pos += 1

def jmp(input):
    global pos
    pos += input
    
def nop(input):
    global pos
    pos += 1
    
def call(ins):
    operation, argument = ins 
    return getattr(sys.modules[__name__], operation)(argument)

def fix_ins(ins):
    operation, argument = ins
    if operation == 'nop':
        operation = 'jmp'
    elif operation == 'jmp':
        operation = 'nop'
    return operation, argument


def fix(program, iteration):
    version = 0
    local_pos = 0
    while version < iteration:
        local_pos += 1
        if program[local_pos][0] in ['jmp', 'nop']:
            version += 1
    program[local_pos] = fix_ins(program[local_pos])
    return program

program = []
with open('input8.txt') as f:
    for line in f:
        program.append(instruction(line))
f.closed

for version in range(len(program)):
    pos = 0
    acc0 = 0
    visited = []
    program_version = fix(program.copy(), version)
    print(program_version)
    while pos not in visited:
        if (pos == len(program_version)):
            print(acc0)
            exit()
        visited.append(pos)
        call(program_version[pos])
