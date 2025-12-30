input = []
with open('input7.txt') as f:
    for line in f:
        input.append(line.strip())

# filesystem = { '/' : {}}

# def addFolder(path, folder):
#     loc = filesystem
#     for f in path:
#         loc = loc[f]    
#     loc[folder] = {}

path = ['/']
sizes = { '/' : 0}
for command in input:
    cursor = command.split(' ')[0]
    if cursor == '$':
        op = command.split(' ')[1]
        if op == 'cd':
            folder = command.split(' ')[2]
            if folder == '/':
                path = [ '/' ]
            elif folder == '..':
                path.pop()
            else:
                path.append(folder)
                sizes['/'.join(path)] = 0
            print(f'gone to {folder}: {path}')
        # elif op == 'ls':
        #     None
    else:
        # if cursor == 'dir': # found folder
        #     folder = command.split(' ')[1]
        #     addFolder(path, folder)
        # else: # found file
        if (cursor != 'dir'):
            size = command.split(' ')[0]
            name = command.split(' ')[1] # irrelevant
            for lvl in range(1, len(path)+1):
                lvlpath = '/'.join(path[:lvl])
                sizes[lvlpath] = sizes[lvlpath] + int(size)
                # print(f'Adding {size} because of {name} to {lvlpath}')

# print(filesystem)
print(sizes)

disk = 70000000
used = sizes['/']
needed = 30000000
print(f'Used space: {used}/{disk}')
print(f'Need a folder with at least {needed - disk + used}')

best = min(filter(lambda size: disk - used + size >= needed, sizes.values()))

print(best)