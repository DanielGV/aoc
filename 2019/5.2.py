with open('inputday5.txt') as f:
    for line in f:
        intcode = list(map(int, line.split(',')))
f.closed

def parameter_mode(instruction, parameter_number):
    pos = -2 - parameter_number
    if (len(instruction)<abs(pos)):
        return 0
    return int(instruction[pos])

def operation_code(instruction):
    return int(inst[-2:])

def parameter_value(instructions, position, parameter_mode):
    if (parameter_mode == 0):
        return instructions[instructions[position]]
    elif (parameter_mode == 1):
        return instructions[position]
    else:
        print("sumething wrong")

i = 0
while True:
    inst = str(intcode[i])
    op = operation_code(inst)

    if (op == 1):
        intcode[intcode[i+3]] = parameter_value(intcode, i+1, parameter_mode(inst, 1)) + parameter_value(intcode, i+2, parameter_mode(inst, 2))
        print("sum",intcode[i+1],"+",intcode[i+2],"on",intcode[i+3])
        i = i + 4
    elif (op == 2):
        intcode[intcode[i+3]] = parameter_value(intcode, i+1, parameter_mode(inst, 1)) * parameter_value(intcode, i+2, parameter_mode(inst, 2))
        print("mul",intcode[i+1],"*",intcode[i+2],"on",intcode[i+3])
        i = i + 4
    elif (op == 3):
        inputo = input()
        intcode[intcode[i+1]] = inputo
        print("save",inputo,"on",intcode[i+1])
        i = i + 2
    elif (op == 4):
        print("print",intcode[intcode[i+1]])
        i = i + 2
    elif (op == 5):
        print("jump-if",intcode[i+1],"to",intcode[i+2])
        if (parameter_value(intcode, i+1, parameter_mode(inst, 1))!=0):
            i = parameter_value(intcode, i+2, parameter_mode(inst, 2))
        else:
            i = i + 3
    elif (op == 6):
        print("jump-if-not",intcode[i+1],"to",intcode[i+2])
        if (parameter_value(intcode, i+1, parameter_mode(inst, 1))==0):
            i = parameter_value(intcode, i+2, parameter_mode(inst, 2))
        else:
            i = i + 3
    elif (op == 7):
        print("less-thank",intcode[i+1],intcode[i+2],"on",intcode[i+3])
        if (parameter_value(intcode, i+1, parameter_mode(inst, 1)) < parameter_value(intcode, i+2, parameter_mode(inst, 2))):
            intcode[intcode[i+3]] = 1
        else:
            intcode[intcode[i+3]] = 0
        i = i + 4
    elif (op == 8):
        print("equals",intcode[i+1],intcode[i+2],"on",intcode[i+3])
        if (parameter_value(intcode, i+1, parameter_mode(inst, 1)) == parameter_value(intcode, i+2, parameter_mode(inst, 2))):
            intcode[intcode[i+3]] = 1
        else:
            intcode[intcode[i+3]] = 0
        i = i + 4
    elif (op == 99):
        break
    else:
        print("sumething wrong")

print(intcode[0])