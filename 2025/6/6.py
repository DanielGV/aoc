from typing import List, Tuple


def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()

def process_input(input: List[str]) -> List[Tuple[List[int], str]]:
    numbers = []
    for line in input:
        numbers.append([n for n in line.split(" ") if n != "" and n != "\n"])
    input = []
    for j in range(len(numbers[0])):
        calculation = []
        for i in range(len(numbers)-1):
            calculation.append(int(numbers[i][j]))
        input.append((calculation, numbers[-1][j]))
    return input


data = read_input("6/6.input.txt")
math_problems = process_input(data)
print(math_problems)
total = 0
for operators, operation in math_problems:
    result = 0 if operation == "+" else 1
    for number in operators:
        if operation == "+":
            result += number
        elif operation == "*":
            result *= number
    total += result
print("The total sum is:", total)

