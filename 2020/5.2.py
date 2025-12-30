directions = set(['F','B','L','R'])

# Front and back binary 0 and 1 right to left
# Left and right binary 0 and 1 right to left

def row(seat):
    return int(seat[0:7].replace('F','0').replace('B','1'), 2)
    
def col(seat):
    return int(seat[-3:].replace('L','0').replace('R','1'), 2)

def seat_id(seat):
    return row(seat) * 8 + col(seat)

def print_seat(seat):
    print('row', row(seat), 'col', col(seat), 'id', seat_id(seat))

def find_missing(seats): 
    return [seat for seat in range(min(map(seat_id, seats)), max(map(seat_id, seats))+1) if seat not in map(seat_id, seats)] 
  
seats = []
with open('input5.txt') as f:
    for line in f:
        seats.append(line.strip())
f.closed

print(find_missing(seats))