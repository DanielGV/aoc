from typing import List
 
def read_lines(filename: str) -> List[str]:
    """Read a file and return its lines as a list of strings."""
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
 
def is_roll(map: List[str], x: int, y: int) -> bool:
    """Check if a position has a roll."""
    return map[x][y] == '@'
 
def get_adjacent_positions(map: List[str], x: int, y: int) -> List[str]:
    """Get the adjacent positions for a roll."""
    adjacent_positions = []
    for i in range(max(x-1,0), min(x+2, len(map))):
        adjacent_positions.append(map[i][max(y-1,0):min(y+2, len(map[i]))])
    return adjacent_positions
 
def count_rolls(map: List[str]) -> int:
    """Get the adjacent positions for a roll."""
    rolls = 0
    for line in map:
        for char in line:
            if char == '@':
                rolls += 1
    return rolls
 
def is_accessible(map: List[str], x: int, y: int) -> bool:
    """Check if a position is accessible."""
    adjacent_positions = get_adjacent_positions(map, x, y)
    adjacent_rolls = count_rolls(adjacent_positions)
    return adjacent_rolls < 5
 
def remove_roll(map: List[str], x: int, y: int) -> None:
    """Remove a roll from the map."""
    map[x] = map[x][:y] + '.' + map[x][y+1:]
 
 
# Read the example file
lines = read_lines("4/4.input.txt")
print(f"Read {len(lines)} lines")
 
accessible_rolls = 0
rolls_to_remove = []
working_map = lines.copy()
while True:
    for x, line in enumerate(working_map):
        for y, char in enumerate(line):
            if is_roll(working_map, x, y):
                if is_accessible(working_map, x, y):
                    accessible_rolls += 1
                    rolls_to_remove.append((x, y))
    if len(rolls_to_remove) == 0:
        break
    for x, y in rolls_to_remove:
        remove_roll(working_map, x, y)
    rolls_to_remove = []
 
 
print(f"Total accessible rolls: {accessible_rolls}")