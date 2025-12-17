
from typing import List, Tuple
import math
 
 
def read_lines(filename: str) -> List[str]:
    """Read a file and return its lines as a list of strings."""
    with open(filename, "r") as f:
        return f.readlines()[0].strip().split(',')
 
def process_line(line: str) -> Tuple[int, int]:
    """Process a line and return the new dial position."""
    start, end = line.split('-')[0], line.split('-')[1]
    return int(start), int(end)
 
def makeInvalid(seed: int) -> int:
    """Make the invalid product ID by using the seed."""
    number_of_digits = int(math.log10(seed)) + 1
    return (seed * (10 ** number_of_digits)) + (seed)
 
def makeSeed(number: int) -> int:
    """Find the seed that would produce the given number via makeInvalid."""
    total_digits = int(math.log10(number)) + 1
    if total_digits % 2 != 0:
        return int("9" * (total_digits // 2)) if total_digits // 2 > 0 else 1
    firstpart = number // (10 ** (total_digits // 2)) 
    return firstpart
 
def findInvalids(start: int, end: int) -> List[int]:
    """Find the invalid product IDs in the given range."""
    invalids = []
    seed = makeSeed(start)
    while makeInvalid(seed) <= end:
        print(f"Checking seed: {seed}, invalid: {makeInvalid(seed)}")
        if makeInvalid(seed) < start:
            seed+=1
            continue
        invalids.append(makeInvalid(seed))
        seed+=1
    return invalids
 
 
# Read the example file
lines = read_lines("2/2.input.txt")
print(f"Read {len(lines)} lines:")
 
total = 0
for line in lines:
    print(f"Processing line: {line}")
    start, end = process_line(line)
    # Do the work
    invalids = findInvalids(start, end)
    print(f"Between {start} and {end} found {invalids} invalids")
    total += sum(invalids)
    print(f"Total is now {total}")
 
print(f"The total is {total}")
 
 