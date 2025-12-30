def guardsMinutes(lines):
    guardsleeps = dict({})
    registers = iter(lines)
    register = next(registers)
    while True:#register in registers:
        guard_id = int(register.split('#')[1][0:4])
        register = next(registers)
        while 'Guard' not in register:
            fro = int(register[15:17])
            to = int(next(registers)[15:17])
            if guard_id in guardsleeps:
                guardsleeps[guard_id] = guardsleeps[guard_id] + (to - fro)
            else:
                guardsleeps[guard_id] = to - fro
            #print('guard {} naps from {} to {}'.format(guard_id, fro, to))
            register = next(registers, None)
            if register is None:
                break
        if register is None:
            break
    return guardsleeps

def guardMinutes(lines, guardid):
    minutessleeps = [0] * 60
    registers = iter(lines)
    register = next(registers)
    while True:#register in registers:
        guard_id = int(register.split('#')[1][0:4])
        register = next(registers)
        while 'Guard' not in register:
            fro = int(register[15:17])
            to = int(next(registers)[15:17])
            
            if (guardid == guard_id):    
                for minu in range(fro, to):
                    minutessleeps[minu] = minutessleeps[minu] + 1
            #print('guard {} naps from {} to {}'.format(guard_id, fro, to))
            register = next(registers, None)
            if register is None:
                break
        if register is None:
            break
    return minutessleeps

def mostSleep(guardsminutes):
    sortedBySleep = [(k, guardsminutes[k]) for k in sorted(guardsminutes, key=guardsminutes.get, reverse=True)]
    for key, value in sortedBySleep:
        #print ('{}: {}'.format(key, value))
        return key

lines = []
with open('input4.txt') as f:
    for line in f:
        lines.append(line)
f.closed
lines.sort()

guardsleeps = guardsMinutes(lines)
mostsleepy = mostSleep(guardsleeps)
for guard, value in sortedBySleep:
    sortedBySleep[guard] = guardMinutes(lines, guard)

for guard, value in sortedBySleep:
    print('guard {}, min {}, times{}'.format(guard, value.index(max(value)), max(value))

# print(minutes)
# print(mostsleepy, minutes.index(max(minutes)))
# print(mostsleepy * minutes.index(max(minutes)))