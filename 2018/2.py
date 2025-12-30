doubles = 0
triples = 0
with open('input2.txt') as f:
    for line in f:
        letters = dict()
        for char in line:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        for letter in letters:
            if letters[letter] == 2:
                doubles += 1
                break
        for letter in letters:
            if letters[letter] == 3:
                triples += 1
                break
f.closed
print(doubles)
print(triples)
print(doubles * triples)