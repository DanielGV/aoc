with open('inputday2.txt') as f:
    for line in f:
        intcode = list(map(int, line.split(',')))
f.closed

intcode[1]=12
intcode[2]=2

i = 0
while True:
    op = intcode[i]
    if (op == 1):
        intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
        print("sum",intcode[i+1],"+",intcode[i+2],"on",intcode[i+3])
    elif (op == 2):
        intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
        print("mul",intcode[i+1],"*",intcode[i+2],"on",intcode[i+3])
    elif (op == 99):
        break
    else:
        print("sumething wrong")
    i = i + 4

print(intcode[0])