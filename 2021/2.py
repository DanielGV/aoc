commands = []
with open('input2.txt') as f:
    for line in f:
        commands.append(line)
f.closed

class Command:
    def __init__(self, command):
        self.op = command.split(' ')[0]
        self.x = int(command.split(' ')[1])

pos = [0, 0]

class operator:
    def forward(x):
        pos[0] += x

    def down(x):
        pos[1] += x

    def up(x):
        pos[1] -= x

increase = 0
for command in commands:
    cmd = Command(command)
    getattr(operator, cmd.op)(cmd.x)
    print(cmd.op, cmd.x, pos)

print(pos, pos[0]*pos[1])
exit()
