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

path = []
while len(path) != len(steps):
  for step in steps:
    if (step not in path) and ((step not in dependencies) or (len(dependencies[step]) == 0)):
      path.append(step)
      for key in dependencies:
        deps = dependencies[key]
        if step in deps:
          deps.remove(step)
      break    

print(''.join(path))