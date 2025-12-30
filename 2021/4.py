class Board:
    def __init__(self, boardinput):
        self.grid = boardinput
        self.marked = []
        self.unmarked = [number for row in self.grid for number in row]
    
    def contains(self, number):
        return number in self.unmarked

    def mark(self, number):
        if self.contains(number):
            self.marked.append(number)
            self.unmarked.remove(number)
            return self.is_bingo()
        return False

    def columns(self):
        return [[row[i] for row in self.grid] for i in range(5)]

    def is_bingo(self):
        for row in self.grid:
            if all(number in self.marked for number in row):
                return True
        for column in self.columns():
            if all(number in self.marked for number in column):
                return True
    

draw = []
boards = []
with open('input4.txt') as f:
    draw = list(map(int, f.readline().strip().split(',')))
    print(draw)
    line = f.readline()
    while line != '':
        board = []
        for i in range(5):
            board.append(list(map(int, f.readline().strip().split())))
        boards.append(Board(board))
        line = f.readline()
        print(board)
    boards.pop() # Correct last read

winner = None
for i in range(len(draw)):
    last_drawn = draw[i]
    print(last_drawn)
    for board in boards:
        if (board.mark(last_drawn)):
            winner = board
            break
    if winner is not None:
        break


result = last_drawn * sum(winner.unmarked)
print('Result', result)
exit()
