from typing import List, Tuple

class Machine():  
  
    def __init__(self, light_diagram: str, buttons: List[List[int]], requirements: List[int]):  
        self.light_diagram = light_diagram  
        self.buttons = buttons  
        self.requirements = requirements
    
    def number_of_lights(self) -> int:
        return len(self.light_diagram)

    def desired_state(self) -> List[int]:
        desired_state = []
        for i, light in enumerate(self.light_diagram):
            if light == "#":
                desired_state.append(i)
        return desired_state

def read_input(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.readlines()

def process_input(input: List[str]) -> List[Tuple[str, List[int], List[int], List[int]]]:
    machines = []
    for line in input:
        parts = line.strip().split(" ")
        light_diagram = parts[0].strip("[]")
        buttons = [list(map(int, button.strip("()").split(","))) for button in parts if button.startswith("(")]
        requirements = list(map(int, parts[-1].strip("{}").split(",")))
        machine = Machine(light_diagram, buttons, requirements)
        machines.append(machine)
    return machines

def press_button(state: List[int], button: List[int]) -> List[int]:
    new_state = state.copy()
    for light_pos in button:
        if light_pos in new_state:
            new_state.remove(light_pos)
        else:
            new_state.append(light_pos)
    return new_state

def minimum_number_of_presses(machine: Machine) -> int:
    for number_of_presses in range(1, len(machine.buttons)):
        combinations = append_combinations(machine.buttons, number_of_presses)
        for combination in combinations:
            state = []
            for button in combination:
                state = press_button(state, button)
            if set(state) == set(machine.desired_state()):
                print(f"Found solution: {combination}")
                return number_of_presses
    print("No solution found")
    return None
     
def append_combinations(buttons: List[List[int]], number_of_presses: int) -> List[List[int]]:
    if number_of_presses == 1:
        return [[button] for button in buttons]
    super_new_combinations = []
    for i, button in enumerate(buttons):
        new_combinations = append_combinations(buttons[i+1:], number_of_presses - 1)
        for new_combination in new_combinations:
            new_combination.append(button)
        super_new_combinations.extend(new_combinations)
    return super_new_combinations

input = read_input("2025/10/10.input.txt")
machines = process_input(input)

button_presses = 0
for machine in machines:
    print(f"Machine: {machine.light_diagram}, desired state: {machine.desired_state()}, buttons: {machine.buttons}, requirements: {machine.requirements}")
    machine_minimum_number_of_presses = minimum_number_of_presses(machine)
    button_presses += machine_minimum_number_of_presses
    print(f"Minimum number of presses: {machine_minimum_number_of_presses}")
print(button_presses)
