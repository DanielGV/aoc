from typing import List, Tuple


def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()


def find_start(input: str) -> int:
    return input.find("S")


data = read_input("7/7.input.txt")
beams = set()
beams.add(find_start(data[0]))

splitter_count = 0
for line in data:
    new_beams = set()
    for beam in beams:
        if line[beam] == "^":
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
            splitter_count += 1
        else:
            new_beams.add(beam)
    beams = new_beams

print("Splitter count: " + str(splitter_count))



