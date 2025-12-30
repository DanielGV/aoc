with open('input6.txt') as f:
    for line in f:
        window = []
        for i, s in enumerate(line):
            if s in window:
                window = window[window.index(s)+1:]
            window.append(s)
            if len(window) == 4:
                print(i + 1, window)
                exit()