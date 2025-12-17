from typing import List
 
def read_lines(filename: str) -> List[str]:
    """Read a file and return its lines as a list of strings."""
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
 
battery_size = 12
def find_max_joltage_bank(bank: str) -> int:
    """Find the max joltage for a battery bank."""
    # Take two batteries
    jolt = []
    pos = 0
    for battery in range(12):
        for lvl in range(9, 0, -1):
            to = -(battery_size-battery-1)
            working_window = bank[pos:to] if to != 0 else bank[pos:]
            pos_lvl = working_window.find(str(lvl))
            if pos_lvl == -1:
                continue
            jolt.append((lvl, pos_lvl + pos))
            pos += pos_lvl + 1
            break
    print(f"Jolt sequence: {jolt}")
    return int("".join([str(j[0]) for j in jolt]))
 
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