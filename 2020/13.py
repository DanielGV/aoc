earliest = 0
buses = []
with open('input13.txt') as f:
    earliest = int(f.readline())
    buses = list(map(int, [bus for bus in f.readline().split(',') if bus != 'x']))
f.closed

timestamp = earliest
while True:
    for bus in buses:
        if (timestamp % bus == 0):
            print(timestamp, bus, (timestamp - earliest) * bus)
            exit()
    timestamp += 1
