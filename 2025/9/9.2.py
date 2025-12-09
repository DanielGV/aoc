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

def make_rectangle(point1: Tuple[int, int], point2: Tuple[int, int]) -> List[Tuple[int, int]]:
    return [(point1[0], point1[1]), (point1[0], point2[1]), (point2[0], point2[1]), (point2[0], point1[1])]

def rectangle_in_polygon(rectangle: Tuple[Tuple[int, int], Tuple[int, int]], polygon: List[Tuple[int, int]]):
    """
    Check if a rectangle is inside a polygon.
    As simple as making sure that 
     - all points of the rectangle are inside the polygon
     - none of the polygon points are inside the rectangle
     - none of the polygon lines cross the rectangle
    """
    for polygon_point in polygon:
        if point_in_rectangle(polygon_point, rectangle):
            print(f"Polygon vertex {polygon_point} is in rectangle {rectangle}")
            return False
    for rectangle_point in make_rectangle(rectangle[0], rectangle[1]):
        if not point_in_polygon(rectangle_point, polygon):
            print(f"Rectangle vertex {rectangle_point} is not in polygon {polygon}")
            return False
    for i in range(len(polygon)):
        polygon_line = (polygon[i], polygon[(i + 1) % len(polygon)])
        if line_crosses_rectangle(polygon_line, rectangle):
            print(f"Polygon line {polygon_line} crosses rectangle {rectangle}")
            return False
    return True

def line_crosses_rectangle(line: Tuple[Tuple[int, int], Tuple[int, int]], rectangle: Tuple[Tuple[int, int], Tuple[int, int]]):
    rectangle_points = make_rectangle(rectangle[0], rectangle[1])
    for i in range(len(rectangle_points)):
        rectangle_line = (rectangle_points[i], rectangle_points[(i + 1) % len(rectangle_points)])
        if line_crosses_line(line, rectangle_line):
            return True
    return False

def line_crosses_line(line: Tuple[Tuple[int, int], Tuple[int, int]], segment: Tuple[Tuple[int, int], Tuple[int, int]]):
    line_start, line_end = line
    segment_start, segment_end = segment
    if line_start[0] == line_end[0]:
        if segment_start[0] == segment_end[0]:
            # vertical lines
            return False
        return (min(segment_start[0], segment_end[0]) < line_start[0] < max(segment_start[0], segment_end[0]) and \
            min(line_start[1], line_end[1]) < segment_start[1] < max(line_start[1], line_end[1]))
    if line_start[1] == line_end[1]:
        if segment_start[1] == segment_end[1]:
            # horizontal lines
            return False
        return (min(segment_start[1], segment_end[1]) < line_start[1] < max(segment_start[1], segment_end[1]) and \
            min(line_start[0], line_end[0]) < segment_start[0] < max(line_start[0], line_end[0]))
    

def point_in_rectangle(point: Tuple[int, int], rectangle: Tuple[Tuple[int, int], Tuple[int, int]]):
    return (
        min(rectangle[0][0], rectangle[1][0]) < point[0] < max(rectangle[0][0], rectangle[1][0]) and \
        min(rectangle[0][1], rectangle[1][1]) < point[1] < max(rectangle[0][1], rectangle[1][1])
    )

def point_in_polygon(point: Tuple[int, int], polygon: List[Tuple[int, int]]):
    # Check if point is a vertex
    if point in polygon:
        return True
    inside = False
    for i in range(len(polygon)):
        polygon_line_start, polygon_line_end = polygon[i], polygon[(i + 1) % len(polygon)]

        # Check if point is on the boundary (rectilinear segments)
        if polygon_line_start[0] == polygon_line_end[0]: # Vertical edge
             if min(polygon_line_start[1], polygon_line_end[1]) <= point[1] <= max(polygon_line_start[1], polygon_line_end[1]):
                 return True
        if polygon_line_start[1] == polygon_line_end[1]: # Horizontal edge
             if min(polygon_line_start[0], polygon_line_end[0]) <= point[0] <= max(polygon_line_start[0], polygon_line_end[0]):
                 return True
                 
        # Ray casting algorithm
        if (polygon_line_start[1] < point[1] and polygon_line_end[1] >= point[1]) or (polygon_line_end[1] < point[1] and polygon_line_start[1] >= point[1]):
            if polygon_line_start[0] + (point[1] - polygon_line_start[1]) / (polygon_line_end[1] - polygon_line_start[1]) * (polygon_line_end[0] - polygon_line_start[0]) < point[0]:
                inside = not inside
        
    return inside

points = process_points(read_input("9/9.input.txt"))
print(points)

rectangles = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = rectangle_area(points[i], points[j])
        rectangles.append((area, points[i], points[j]))
rectangles.sort(key=lambda rectangle: rectangle[0], reverse=True)
best_rectangle = None
for rectangle in rectangles:
    print(f"Checking rectangle {rectangle}")
    if rectangle_in_polygon((rectangle[1], rectangle[2]), points):
        best_rectangle = rectangle
        break

print(best_rectangle)