from typing import List
 
 
def read_lines(filename: str) -> List[str]:
    """Read a file and return its lines as a list of strings."""
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
 
def rotate_dial(dial: int, direction: str, distance: int) -> int:
    """Rotate the dial in the given direction by the given distance."""
    if direction == "L":
        return dial - distance
    elif direction == "R":
        return dial + distance
    else:
        raise ValueError(f"Invalid direction: {direction}")
 
def process_line(line: str) -> int:
    """Process a line and return the new dial position."""
    direction, distance = line[0], line[1:]
    return rotate_dial(dial, direction, int(distance))
 
 
# Dial starts at 50
dial = 50
# Count of times the dial is left pointing at 0
count = 0
# Read the example file
lines = read_lines("1.input.txt")
print(f"Read {len(lines)} lines:")
 
for line in lines:
    dial = process_line(line)
    print(f"Dial is now at {dial}")
    if dial % 100 == 0:
        count += 1
print(f"The dial was left pointing at 0 {count} times")
 