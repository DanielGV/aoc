tree = []
with open('input8.txt') as f:
  for line in f:
    tree = [int(x) for x in line.split()]
f.closed

class Node:
    def __init__(self, children, metas):
        #8 @ 431,568: 16x23
        self.children = children
        self.metas = metas
        self.metasdatas = []

print(tree)

nodes = []
i = 0

def readNode(i):
  # readnode
  node = Node(tree[i], tree[i+1])
  i += 2
  # readNodeChildren
  for child in range(node.children):
    i = readNode(i)#readNode
  #readNodeMetas
  node.metasdatas = tree[i:i+node.metas]
  i += node.metas 
  nodes.append(node)
  return i


readNode(i)

sum = 0
for node in nodes:
  print('node', node.metasdatas)
  for meta in node.metasdatas:
    sum += meta

print(sum)