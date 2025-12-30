def timetostep(step):
  return ord(step)+60-64

steps = set([])
dependencies = dict({})
with open('input7.txt') as f:
  for line in f:
    requirement = line[5:6]
    step = line[36:37]
    print(step, ' depends on ', requirement)
    if step in dependencies:
        dependencies[step].append(requirement)
    else:
        dependencies[step] = [requirement]
    steps.add(step)
    steps.add(requirement)
f.closed

print(dependencies)
print(steps)

steps = sorted(steps)
print(steps)

secs = 0
path = []
workQueue = dict({})
workernumber = 5
while len(path) != len(steps):
  for step in steps:
    if (len(workQueue) <= workernumber) and (step not in workQueue) and (step not in path) and ((step not in dependencies) or (len(dependencies[step]) == 0)):
      workQueue[step] = timetostep(step)
  workers = list(workQueue.keys())
  for worker in workers:
    print('working', worker, workQueue[worker])
    oneSecLess = workQueue[worker] - 1
    workQueue[worker] = oneSecLess
    if (oneSecLess == 0):
      del workQueue[worker]
      path.append(worker)
      for key in dependencies:
        deps = dependencies[key]
        if worker in deps:
          deps.remove(worker)
  secs += 1

print(''.join(path))
print(secs)