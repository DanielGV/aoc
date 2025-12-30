import matplotlib.pyplot as plt
import matplotlib.animation as anim

points = []
velocities = []
with open('input10.txt') as f:
  for line in f:
    points.append([int(line[10:16]), int(line[18:24])])
    velocities.append([int(line[36:38]), int(line[40:42])])
f.closed

def move():
  global points
  for i, point in enumerate(points):
    point[0] += velocities[i][0]
    point[1] += velocities[i][1]

def moves(seconds):
  global points
  for i, point in enumerate(points):
    point[0] += velocities[i][0] * seconds
    point[1] += velocities[i][1] * seconds

# Normal plot
# time = 5
# for i in range(time):
#   moves(5000)
#   plt.plot([point[0] for point in points], [point[1] for point in points], 'ro')
#   #plt.axis([40, 160, 0, 0.03])
#   plt.show()

# Finding the time when all points converge
# i = 10300
# moves(10300)
# height = abs(max([point[0] for point in points]) - min([point[0] for point in points]))
# width = abs(max([point[1] for point in points]) - min([point[1] for point in points]))
# while True:
#     moves(1)
#     i += 1
#     oldheight = height
#     oldwidth = width
#     height = abs(max([point[0] for point in points]) - min([point[0] for point in points]))
#     width = abs(max([point[1] for point in points]) - min([point[1] for point in points]))
#     if (height > oldheight):
#         print(i)
#         break

# Animated plot
# plt.ion()
# i = 10475
# moves(10475)
# while True:
#     moves(1)
#     i += 1
#     plt.plot([point[0] for point in points], [point[1] for point in points], 'ro')
#     plt.draw()
#     plt.pause(1.0)
#     plt.clf()
#     print(i)

moves(10476)
plt.plot([point[0] for point in points], [point[1] for point in points], 'ro')
plt.show()

print('Fin')
print('BLGNHPJC')
print(10476)
