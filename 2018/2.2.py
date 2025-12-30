
def findString(lines):
    for line in lines:
        for compare in lines:
            samechars = 0
            for i in range(len(line)):
                if compare[i] == line[i]:
                    samechars += 1
            if samechars == len(line) - 1:
                return makeString(line, compare)

def makeString(string1, string2):
    stringo = ''
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            stringo += string1[i]
    return stringo

lines = []
stringus = ''
with open('input2.txt') as f:
    for line in f:
        lines.append(line)
f.closed
print(findString(lines))

