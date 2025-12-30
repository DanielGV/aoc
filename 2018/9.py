import math

players = 476
lastmarble = 7165700

# players = 10
# lastmarble = 1618

# players = 8
# lastmarble = 25

scores = [0] * players
circle = [0]
current = 0

player = 1
perc = 0
for i in range(1, lastmarble + 1):
  # score points
  if i % 23 == 0 and i != 0:
    current = (current - 7) % len(circle)
    # print('player ', player, 'at turn: ', i, 'scores: ', circle[current], 'pos: ', current)
    scores[player] += i
    scores[player] += circle.pop(current)
  # add marble
  else:
    current = ((current + 1) % len(circle)) + 1
    circle.insert(current, i)
  player = (player + 1) % players
#   print(circle, current)
  if math.ceil(i * 100 / lastmarble) > perc:
    perc = math.ceil(i * 100 / lastmarble)
    print(perc)
    

for player in range(players):
  print('player: ', player, "score: ", scores[player])

print('Max score: ', max(scores))