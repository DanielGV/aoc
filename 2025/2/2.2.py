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
 
def makeInvalid(seed: int, digits: int) -> int:
    """Make the invalid product ID by using the seed."""
    number_of_digits = int(math.log10(seed)) + 1
    if digits % number_of_digits != 0 or len(str(seed)) == digits:
        print(f"Seed {seed} has {number_of_digits} digits, but digits {digits} is not a multiple of {number_of_digits}")
        return None
    return int(str(seed) * (digits // number_of_digits))
 
def makeSeed(number: int, digits: int) -> int:
    """Find the seed that would produce the given number via makeInvalid."""
    return int(str(number)[:digits])
 
def findInvalids(start: int, end: int) -> List[int]:
    """Find the invalid product IDs in the given range."""
    invalids = []
    full_length = len(str(end))
    for d in range(1, (full_length//2)+1):
        seed = makeSeed(start, d)
        for i, li in enumerate(range(len(str(start)), len(str(end))+1)):
            print(f"Looking for seed lenght {d}, numbers length {li}, seed {seed}")
            seed = makeSeed(start, d) if i == 0 else 10**(d-1)
            pid = makeInvalid(seed, li)
            while len(str(seed)) == d and pid is not None and pid <= end:
                print(f"Checking seed lenght {d}: {seed}, invalid: {pid}")
                if pid >= start:
                    invalids.append(pid)
                seed+=1
                pid = makeInvalid(seed, li)
    return set(invalids)
 
 
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