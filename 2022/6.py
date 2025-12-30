input = []
with open('input6.txt') as f:
    for line in f:
        input.append(line)

data = input[0]
window = []
for i, s in enumerate(data):
    if s in window:
        window = window[window.index(s)+1:]
    window.append(s)
    if len(window) == 4:
        print(i + 1, window)
        exit()
    print(i + 1, s, window)
