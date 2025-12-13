from functools import cache
from _struct import calcsize
from typing import List, Dict

def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()

def process_input(input: List[str]) -> Dict[str, List[str]]:
    connections = {}
    for line in input:
        parts = line.strip().split(":")
        source = parts[0]
        target = parts[1].strip().split(" ")
        connections[source] = target
    return connections

connections = process_input(read_input("2025/11/11.input.txt"))
print(connections)
connections["out"] = []
@cache # to avoid re-computing paths
def count_paths(current_node: str) -> int:
    if current_node == "out":
        return 1

    total_paths = 0
    for next in connections[current_node]:
        total_paths += count_paths(next)
    
    return total_paths
print(count_paths("you"))