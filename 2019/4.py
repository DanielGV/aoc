import sys

def rule1(candidate):
    return candidate < 1000000 and candidate > 99999

def rule2(candidate):
    return candidate < 643281 and candidate > 128392

def rule3(candidate):
    number = str(candidate)
    return sum(number[th]==number[th+1] for th in range(0,5)) >= 1

def rule4(candidate):
    number = str(candidate)
    return sum(int(number[th])<=int(number[th+1]) for th in range(0,5)) == 5

def password(candidate):
    return rule2(candidate) and rule3(candidate) and rule4(candidate)

test = 111111
print(test, password(test), rule1(test), rule2(test), rule3(test), rule4(test))

test = 223450
print(test, password(test), rule1(test), rule2(test), rule3(test), rule4(test))

test = 123789
print(test, password(test), rule1(test), rule2(test), rule3(test), rule4(test))

test = 223456
print(test, password(test), rule1(test), rule2(test), rule3(test), rule4(test))

candidates = [x for x in range(100000, 1000000)]

numberoo = sum(password(candidate) for candidate in candidates)

print numberoo