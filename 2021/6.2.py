days_to_breed = 6
first_cycle = days_to_breed + 2

lanterfish = [0] * (first_cycle + 1)
with open('input6.txt') as f:
    line = f.readline()
    fishes = list(map(int, line.strip().split(',')))
    for fish in fishes:
        lanterfish[fish] += 1
    

print('Initial state:', lanterfish)

days = 256

for day in range(days):
    next_gen_lanterfish = [0] * (first_cycle + 1)
    for i in range(1, len(lanterfish)):
        next_gen_lanterfish[i-1] = lanterfish[i]
    next_gen_lanterfish[first_cycle] += lanterfish[0]
    next_gen_lanterfish[days_to_breed] += lanterfish[0]
    lanterfish = next_gen_lanterfish
    print(f'After {day + 1} days:', lanterfish)

print('Result', sum(lanterfish))
exit()
