from typing import List
 
def read_lines(filename: str) -> List[str]:
    """Read a file and return its lines as a list of strings."""
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
 
def find_max_joltage_bank(bank: str) -> int:
    """Find the max joltage for a battery bank."""
    # Take two batteries
    for deci in range(9, 0, -1):
        pos_dec = bank.find(str(deci))
        if pos_dec == -1:
            continue
        for unii in range(9, 0, -1):
            pos_uni = bank[pos_dec+1:].find(str(unii))
            if pos_uni == -1:
                continue
            return int(f"{deci}{unii}")
 
    return 0
 
# Read the example file
lines = read_lines("3/3.input.txt")
print(f"Read {len(lines)} lines:")
 
total_joltage = 0
for line in lines:
    print(f"Processing battery bank: {line}")
    max_joltage = find_max_joltage_bank(line)
    print(f"Max joltage for battery bank {line}: {max_joltage}")
    total_joltage += max_joltage
 
print(f"Total output joltage: {total_joltage}")