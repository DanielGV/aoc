import sys

acc0 = 0
pos = 0
visited = []

def instruction(line):
    return line[0:3], line[4:-1]

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
    return getattr(sys.modules[__name__], operation)(int(argument))

program = []
with open('input8.txt') as f:
    for line in f:
        program.append(instruction(line))
f.closed


while pos not in visited:
    visited.append(pos)
    call(program[pos])

print(acc0)

