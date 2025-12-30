monkeystate = []
with open('input11.txt') as f:
    for line in f:
        monkeystate.append(line.strip())

print(monkeystate)

class Monkey:
    def __init__(self, idx, items, operation, test, true, false):
        self.idx = idx
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspections = 0

def read_monkey(decl):
    monkey_idx = int(decl[0].split(' ')[1].replace(':', ''))
    items = list(map(int,decl[1].replace('Starting items: ', '').split(', ')))
    def calc(old):
        return eval(decl[2].replace('Operation: new = ', ''))
    operation = calc
    test = lambda worry: (worry % int(decl[3].split(' ')[-1])) == 0
    true = int(decl[4].split(' ')[-1])
    false = int(decl[5].split(' ')[-1])
    print(monkey_idx, items, operation, test, true, false)
    return Monkey(monkey_idx, items, operation, test, true, false)

monkeys = []
idx = 0
while idx < len(monkeystate):
    monkeys.append(read_monkey(monkeystate[idx:idx+6]))
    idx += 7


for round in range(20):
    for monkey in monkeys:
        print(f'monkey {monkey.idx} turn')
        while len(monkey.items)>0:
            worry = monkey.items.pop(0)
            print(f'monkey checks {worry} out')
            worry = monkey.operation(worry)
            print(f'monkey operates {worry}')
            monkey.inspections += 1
            worry = int(worry/3)
            print(f'calmed worry {worry}')
            if (monkey.test(worry)):
                monkeys[monkey.true].items.append(worry)
                print(f'trows to {monkey.true}')
            else:
                monkeys[monkey.false].items.append(worry)
                print(f'trows to {monkey.false}')

monkey_inspections = [monkey.inspections for monkey in monkeys]
inspection1 = max(monkey_inspections)
monkey_inspections.remove(inspection1)
inspection2 = max(monkey_inspections)
monkey_business = inspection1 * inspection2

print(monkey_business)