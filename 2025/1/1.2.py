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
 
def position_in_circle(dial: int) -> int:
    """Return the position of the dial in the circle."""
    return dial // 100 
 
 
# Dial starts at 50
dial = 50
# Count of times the dial is left pointing at 0
count = 0
# Read the example file
lines = read_lines("1.input.txt")
print(f"Read {len(lines)} lines:")
 
for line in lines:
    print(f"Processing line: {line}")
    new_dial = process_line(line)
    print(f"From {dial} to {new_dial}")
    dialsteps = position_in_circle(new_dial) - position_in_circle(dial)
    passes_by_zero = abs(dialsteps)
    if dialsteps <= 0:
        if new_dial % 100 == 0:
            passes_by_zero += 1
        if dial % 100 == 0 and passes_by_zero > 0:
            passes_by_zero -= 1
    count += passes_by_zero
    print(f"Dial passed by zero {passes_by_zero} times")
    dial = new_dial
    print(f"Dial is now at {dial}")
 
print(f"The dial passed by zero {count} times")
 
