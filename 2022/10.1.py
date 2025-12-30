program = []
with open('input10.txt') as f:
    for line in f:
        program.append(line.strip())

#print(program)
spritepos = 1
screen = ['X']*240

cycle = 1
def paint(cl, x):
    pxl = cl-1
    pos = (cl-1) % 40
    # print(''.join(['#' if (x - 1 <= i and x + 1 >= i) else '.' for i in range(1,41)]))
    # print(''.join(screen[:cl-1]))
    if (x - 1 <= pos and x + 1 >= pos):
        screen[pxl] = '#'
        # print(cl, pos, x, '#')
    else:
        screen[pxl] = '.'
        # print(cl, pos, x, '.')

for inst in program:
    if inst.startswith('noop'):
        paint(cycle, spritepos)
        cycle += 1
    elif inst.startswith('addx'):
        paint(cycle, spritepos)
        paint(cycle+1, spritepos)
        v = int(inst.split(' ')[1])
        spritepos += v
        cycle += 2
    else:
        print('problemo')
        exit(1)

# print CTR screen
for line in range(6):
    print(''.join(screen[line*40:(line+1)*40]))
