commands = []
with open('input2.txt') as f:
    for line in f:
        commands.append(line)
f.closed

class Command:
    def __init__(self, command):
        self.op = command.split(' ')[0]
        self.x = int(command.split(' ')[1])

class Position:
    def __init__(self):
        self.aim = 0
        self.h = 0
        self.d = 0

pos = Position()

class operator:
    def forward(x):
        pos.h += x
        pos.d += pos.aim * x

    def down(x):
        pos.aim += x

    def up(x):
        pos.aim -= x

increase = 0
for command in commands:
    cmd = Command(command)
    getattr(operator, cmd.op)(cmd.x)
    print(cmd.op, cmd.x, pos)

print(pos, pos.d*pos.h)
exit()
