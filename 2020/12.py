pos = (0,0)
direction = 'E'
directions = ['E', 'S', 'W', 'N']

def north(value):
    global pos
    pos = pos[0], pos[1] + value 

def east(value):
    global pos
    pos = pos[0] + value, pos[1]

def south(value):
    global pos
    pos = pos[0], pos[1] - value 

def west(value):
    global pos
    pos =  pos[0] - value, pos[1]

def right(value):
    global direction
    direction = directions[(directions.index(direction) + int(value / 90)) % 4]

def left(value):
    global direction
    direction = directions[(directions.index(direction) - int(value / 90)) % 4]

def forward(value):
    functions[direction](value)

functions = {
  'N': lambda x: north(x),
  'E': lambda x: east(x),
  'S': lambda x: south(x),
  'W': lambda x: west(x),
  'R': lambda x: right(x),
  'L': lambda x: left(x),
  'F': lambda x: forward(x)
}

def execute(ins):
    action = ins[0]
    value = int(ins[1:])
    functions[action](value)

instructions = []
with open('input12.txt') as f:
    for line in f:
        instructions.append(line.strip())
f.closed

for ins in instructions:
    print(pos, direction)
    print(ins)
    execute(ins)
    
print(pos)
print(abs(pos[0])+abs(pos[1]))