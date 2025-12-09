from typing import List, Tuple


def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()


def find_start(input: str) -> int:
    return input.find("S")


data = read_input("7/7.input.txt")
beams = {}
for i in range(len(data[0])):
    beams[i] = 0
beams[find_start(data[0])] = 1
splitter_count = 0
for line in data:
    for beam, count in beams.items():
        if count == 0:
            continue
        if line[beam] == "^":
            beams[beam - 1] += count
            beams[beam + 1] += count
            beams[beam] -= count
            splitter_count += 1

print("Beams map: " + str(beams))
print("Splitter count: " + str(splitter_count))
print("Non zero beams: " + str(sum(count for beam, count in beams.items())))



