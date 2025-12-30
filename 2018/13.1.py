from enum import Enum
import copy

EAST = [0, 1]
WEST = [0, -1]
NORTH = [-1, 0]
SOUTH = [1, 0]

class Turn(Enum):
    RIGHT = 1
    STRAIGHT = 0
    LEFT = -1

track = []
with open('input13.txt') as f:
  for line in f:
    track.append(line)
f.closed

def charDir(char):
    if char == '>':
        return EAST
    if char == '<':
        return WEST
    if char == '^':
        return NORTH
    if char == 'v':
        return SOUTH

def dirChar(dirs):
    if dirs == EAST:
        return '>'
    if dirs == WEST:
        return '<'
    if dirs == NORTH:
        return '^'
    if dirs == SOUTH:
        return 'v'

def applyVel(coord, vel):
    return [coord[0] + vel[0], coord[1] + vel[1]]

def turnLeft(vel):
    if vel == EAST:
        return NORTH
    if vel == NORTH:
        return WEST
    if vel == WEST:
        return SOUTH
    if vel == SOUTH:
        return EAST

def turnRight(vel):
    if vel == EAST:
        return SOUTH
    if vel == SOUTH:
        return WEST
    if vel == WEST:
        return NORTH
    if vel == NORTH:
        return EAST

class Cart:
    def __init__(self, coord, char):
        self.pos = coord
        self.vel = charDir(char)
        self.nextTurn = Turn.LEFT
    
    def __repr__(self):
        return str(self.pos) + str(self.vel) + str(self.nextTurn)

    def __str__(self):
        return str(self.pos) + str(self.vel) + str(self.nextTurn)

    def move(self, track):
        newpos = applyVel(self.pos, self.vel)
        trackchar = track[newpos[0]][newpos[1]]
        
        self.pos = newpos
        if (trackchar in ['-', '|', '<', '>', '^', 'v']):
            return
        elif ((trackchar == '/' and self.vel[1] != 0) or (trackchar == '\\' and self.vel[0] != 0)):
            self.turnLeft()
        elif ((trackchar == '/' and self.vel[0] != 0) or (trackchar == '\\' and self.vel[1] != 0)):
            self.turnRight()
        elif (trackchar == '+'):
            self.takeIntersection()
        else:
            print('problem @', newpos, trackchar)
    
    def turnLeft(self):
        self.vel = turnLeft(self.vel)

    def turnRight(self):
        self.vel = turnRight(self.vel)

    def takeIntersection(self):
        if (self.nextTurn == Turn.LEFT):
            self.turnLeft()
            self.nextTurn = Turn.STRAIGHT
        elif (self.nextTurn == Turn.STRAIGHT):
            self.nextTurn = Turn.RIGHT
        elif (self.nextTurn == Turn.RIGHT):
            self.turnRight()
            self.nextTurn = Turn.LEFT


carts = []
for y, line in enumerate(track):
    for x, col in enumerate(line):
        if (col in ['<', '>', '^', 'v']):
            carts.append(Cart([y,x], col))

print(carts)


collision = None

while True:
    status = copy.deepcopy(track)
    carts = sorted(carts, key=lambda cart: cart.pos[0]*len(track)+cart.pos[1])
    cartstokill = []
    print(carts)
    for i, cart in enumerate(carts):
        cart.move(track)
        tmp = list(status[cart.pos[0]])
        tmp[cart.pos[1]] = dirChar(cart.vel)
        status[cart.pos[0]] = ''.join(tmp)
        for j, othercart in enumerate(carts):
            if i != j and cart.pos == othercart.pos:
                collision = cart.pos
                print('collision @', collision, 'carts', i, j, 'result:',collision[1],',',collision[0])
                cartstokill.append(i)
                cartstokill.append(j)
    #print(''.join(status))
    cartstokill = sorted(cartstokill, reverse=True)
    for numdel, todelete in enumerate(cartstokill):
        del carts[todelete]
        print('removed cart',todelete)
    if (len(carts)==1):
        break

print(carts)
print(f'{carts[0].pos[1]},{carts[0].pos[0]}')

