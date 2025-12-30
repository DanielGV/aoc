with open('inputday2.txt') as f:
    for line in f:
        source = list(map(int, line.split(',')))
f.closed


for noun in range(0,100):
    for verb in range(0,100):
        intcode = source[:]
        intcode[1]=noun
        intcode[2]=verb
        i = 0
        while True:
            op = intcode[i]
            if (op == 1):
                intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
                #print("sum",intcode[i+1],"+",intcode[i+2],"on",intcode[i+3])
            elif (op == 2):
                intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
                #print("mul",intcode[i+1],"*",intcode[i+2],"on",intcode[i+3])
            elif (op == 99):
                break
            else:
                print("sumething wrong")
            i = i + 4

        if (intcode[0]==19690720):
            print(intcode[0], noun, verb)
            exit()
print(intcode[0])