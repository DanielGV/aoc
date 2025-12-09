from typing import List, Tuple


def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()

def process_input(input: List[str]) -> List[Tuple[List[int], str]]:
    numbers = []
    calc_i = 0
    operators = []
    operation = input[-1][0]
    for i in range(len(input[0])):
        number_chars = ""
        for j in range(len(input)-1):
            number_chars += input[j][i]
        number_str = number_chars.strip()
        if number_str != "":
            operators.append(int(number_str))
        else:
            numbers.append((operators, operation))
            if i == len(input[0]) - 1:
                break
            operators = []
            calc_i += 1
            operation = input[-1][i+1]
    return numbers


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

