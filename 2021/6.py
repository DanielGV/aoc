days_to_breed = 6
first_cycle = days_to_breed + 2

lanterfish = []
with open('input6.txt') as f:
    line = f.readline()
    lanterfish = list(map(int, line.strip().split(',')))
    

print('Initial state:', lanterfish)

days = 80

for day in range(days):
    babies = 0
    for i, fish in enumerate(lanterfish):
        if fish > 0:
            lanterfish[i] -= 1
        elif fish == 0:
            babies += 1
            lanterfish[i] = days_to_breed
    for baby in range(babies):
        lanterfish.append(first_cycle)

    print(f'After {day + 1} days:', lanterfish)

print('Result', len(lanterfish))
exit()
