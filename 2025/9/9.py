from typing import List, Tuple

def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()

def process_points(input: List[str]) -> List[Tuple[int, int]]:
    points = []
    for line in input:
        points.append(tuple(map(int, line.strip().split(","))))
    return points

def rectangle_area(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    return (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

points = process_points(read_input("9/9.input.txt"))
print(points)

max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = rectangle_area(points[i], points[j])
        max_area = max(max_area, area) 

print(max_area)