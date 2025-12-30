
entries = []
with open('input1.txt') as f:
    for line in f:
        entries.append(int(line))
f.closed

for entry in entries:
    for entry2 in entries:
        for entry3 in entries:
            if (entry + entry2 + entry3 == 2020):
                print(entry)
                print(entry2)
                print(entry3)
                print(entry * entry2 * entry3)
                exit()

