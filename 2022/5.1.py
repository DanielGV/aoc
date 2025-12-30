def stacks(data):
    no_stacks = int(data[-1].split(' ')[-2])
    stacks = []
    for s in range(no_stacks):
        stack = []
        for pos in reversed(range(len(data)-1)):
            crate = data[pos][s*4+1]
            if (crate != ' '):
                stack.append(crate)
        stacks.append(stack)
    return stacks

class Proceduce:
    def __init__(self, num, from_idx, to_idx):
        self.num = num
        self.from_idx = from_idx
        self.to_idx = to_idx
    def __str__(self):
        return str(self.__dict__)

def procedures(data):
    procedures = []
    for step in data:
        stepo = list(filter(None, step.replace('move','').replace('from','').replace('to','').strip().split(' ')))
        # print(stepo)
        proc = Proceduce(int(stepo[0]),int(stepo[1]),int(stepo[2]))
        # print(proc)
        procedures.append(proc)
    return procedures

def crane(input, proc: Proceduce):
    move = []
    for i in range(proc.num):
        move.append(input[proc.from_idx-1].pop())
    for i in range(proc.num):
        input[proc.to_idx-1].append(move.pop())
    return input

input = []
with open('input5.txt') as f:
    for line in f:
        input.append(line)

splitidx = input.index('\n')
print(splitidx)
state = stacks(input[:splitidx])
print(state)
procs = procedures(input[splitidx+1:])
# print(procs)
for op in procs:
    print(state, op)
    state = crane(state, op)

print(state)

print(''.join(list(s.pop() for s in state)))