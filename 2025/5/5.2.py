from typing import List, Tuple
 
def read_lines(filename: str) -> List[str]:
    """Read a file and return its lines as a list of strings."""
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
 
def process_input(input: List[str]) -> List[Tuple[int, int]]:
    """Process the input and return the fresh ingredient ID ranges and the available ingredient IDs."""
    fresh_ingredient_id_ranges = []
    for line in input:
        if line == "":
            break
        parts = line.split("-")
        start, end = int(parts[0]), int(parts[1])
        fresh_ingredient_id_ranges.append((start, end))
    return fresh_ingredient_id_ranges
 
def union_ranges(range1: Tuple[int, int], range2: Tuple[int, int]) -> Tuple[int, int]:
    """Union two ranges and return the union."""
    return (min(range1[0], range2[0]), max(range1[1], range2[1]))
 
def is_range_intersecting(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    """Check if two ranges intersect."""
    return range1[1] + 1 >= range2[0]
 
def merge_ranges(input: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Merge the input ranges into a list of merged ranges."""
    iteration_list = sorted(input.copy(), key=lambda x: x[0])
    working_list = []
    merged = True
    while merged:
        merged = False
        i = 0
        while i < len(iteration_list):
            this = iteration_list[i]
            if i + 1 == len(iteration_list) or not is_range_intersecting(this, iteration_list[i + 1]):
                working_list.append(this)
                i += 1
            else:
                working_list.append(union_ranges(this, iteration_list[i + 1]))
                merged = True
                i += 2
        iteration_list = working_list.copy()
        working_list = []
    return iteration_list
 
# Read the example file
lines = read_lines("5/5.input.txt")
print(f"Read {len(lines)} lines:")
 
raw_fresh = process_input(lines)
print(f"Raw fresh: {raw_fresh}")
 
merged_fresh = merge_ranges(raw_fresh)
print(f"Merged fresh: {merged_fresh}")
 
fresh_count = 0
for fresh_interval in merged_fresh:
    fresh_start, fresh_end = fresh_interval
    print(f"Fresh interval: {fresh_start} to {fresh_end}: {fresh_end - fresh_start + 1} fresh products")
    fresh_count += fresh_end - fresh_start + 1
 
print(f"Fresh count: {fresh_count}")