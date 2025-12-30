
entries = []
with open('input1.txt') as f:
    for line in f:
        entries.append(int(line))
f.closed

for entry in entries:
    for entry2 in entries:
        if (entry + entry2 == 2020):
            print(entry)
            print(entry2)
            print(entry * entry2)
            exit()

