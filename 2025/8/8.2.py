from math import sqrt
from typing import List, Tuple

def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()


def process_points(input: List[str]) -> List[Tuple[int, int, int]]:
    points = []
    for line in input:
        points.append(tuple(map(int, line.strip().split(","))))
    return points

def distance(point1: Tuple[int, int, int], point2: Tuple[int, int, int]) -> float:
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2)

def connect_junction_boxes(box1: int, box2: int, circuits: List[List[int]]):
    index1, index2 = -1, -1 
    for i, circuit in enumerate(circuits):
        if box1 in circuit:
            index1 = i
        if box2 in circuit:
            index2 = i
    assert(index1 != -1 and index2 != -1, "Boxes not found in circuits")
    if index1 != index2:
        circuits[index1].extend(circuits[index2])
        circuits.remove(circuits[index2])
    

points = process_points(read_input("8/8.input.txt"))
print(points)
print(distance(points[0], points[1]))

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append((distance(points[i], points[j]), i, j))
distances.sort(key=lambda distance: distance[0])

circuits = [[i] for i in range(len(points))]
for i in range(len(distances)):
    box1, box2 = distances[i][1], distances[i][2]
    connect_junction_boxes(box1, box2, circuits)
    if len(circuits) == 1:
        last_connection = box1, box2
        break

product = (points[last_connection[0]][0] * points[last_connection[1]][0])
print(product)
