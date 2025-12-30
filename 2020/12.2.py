import math

pos = (0,0)
waypoint = (10,1)

def north(value):
    global waypoint
    waypoint = waypoint[0], waypoint[1] + value 

def east(value):
    global waypoint
    waypoint = waypoint[0] + value, waypoint[1]

def south(value):
    global waypoint
    waypoint = waypoint[0], waypoint[1] - value 

def west(value):
    global waypoint
    waypoint =  waypoint[0] - value, waypoint[1]

def right(value):
    global waypoint
    angle = - value * math.pi / 180
    waypoint = round(math.cos(angle)*waypoint[0]-math.sin(angle)*waypoint[1]), round(math.sin(angle)*waypoint[0]+math.cos(angle)*waypoint[1])

def left(value):
    global waypoint
    angle = value * math.pi / 180
    waypoint = round(math.cos(angle)*waypoint[0]-math.sin(angle)*waypoint[1]), round(math.sin(angle)*waypoint[0]+math.cos(angle)*waypoint[1])

def forward(value):
    global pos
    pos = pos[0] + waypoint[0] * value, pos[1] + waypoint[1] * value 

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
    print(pos, waypoint)
    print(ins)
    execute(ins)
    
print(pos, waypoint)
print(abs(pos[0])+abs(pos[1]))