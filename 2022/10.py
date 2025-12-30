program = []
with open('input10.txt') as f:
    for line in f:
        program.append(line.strip())

print(program)

cyc = [20, 60, 100, 140, 180, 220]
signal = 0

x = 1
# addx V
# noop
cycle = 1

for inst in program:
    #print(cycle, inst)
    if inst.startswith('noop'):
        if cycle in cyc:
            signal += cycle * x
            print(cycle, x)
        cycle += 1
    elif inst.startswith('addx'):
        if (cycle in cyc):
            signal += cycle * x
            print(cycle, x)
        if (cycle + 1 in cyc):
            signal += (cycle + 1) * x
            print(cycle+1, x)
        v = int(inst.split(' ')[1])
        x += v
        cycle += 2
    else:
        print('problemo')
        exit(1)

print(signal)