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
server_rack = "svr"
digital_to_analog = "dac"
fast_fourier_transform = "fft"
@cache # to avoid re-computing paths
def count_paths(current_node: str, target: str, exclusion: str) -> int:
    if current_node == target:
        return 1
    if current_node == exclusion:
        return 0
    total_paths = 0
    for next in connections[current_node]:
        total_paths += count_paths(next, target, exclusion)
    
    return total_paths

srv_dac = count_paths(server_rack, digital_to_analog, fast_fourier_transform)
print(f"srv -> dac: {srv_dac}")
srv_fft = count_paths(server_rack, fast_fourier_transform, digital_to_analog)
print(f"srv -> fft: {srv_fft}")
dac_fft = count_paths(digital_to_analog, fast_fourier_transform, server_rack)
print(f"dac -> fft: {dac_fft}")
fft_dac = count_paths(fast_fourier_transform, digital_to_analog, server_rack)
print(f"fft -> dac: {fft_dac}")
dac_out = count_paths(digital_to_analog, "out", fast_fourier_transform)
print(f"dac -> out: {dac_out}")
fft_out = count_paths(fast_fourier_transform, "out", digital_to_analog)
print(f"fft -> out: {fft_out}")
srv_dac_fft_out = srv_dac * dac_fft * fft_out
print(f"srv -> dac -> fft -> out: {srv_dac_fft_out}")
srv_fft_dac_out = srv_fft * fft_dac * dac_out
print(f"srv -> fft -> dac -> out: {srv_fft_dac_out}")
print(f"Total paths: {srv_dac_fft_out + srv_fft_dac_out}")

