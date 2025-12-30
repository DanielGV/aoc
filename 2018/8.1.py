tree = []
with open('input8.txt') as f:
  for line in f:
    tree = [int(x) for x in line.split()]
f.closed

class Node:
    def __init__(self, children, metas):
        #8 @ 431,568: 16x23
        self.children = children
        self.childrendatas = []
        self.metas = metas
        self.metasdatas = []
        self.value = 0

nodes = []
idx = 0

def readNode():
  global idx
  # readnode
  node = Node(tree[idx], tree[idx+1])
  idx += 2
  # readNodeChildren
  for child in range(node.children):
    node.childrendatas.append(readNode())
  #readNodeMetas
  node.metasdatas = tree[idx:idx+node.metas]
  idx += node.metas 
  #readNodeValue
  for meta in node.metasdatas:
    if meta <= len(node.childrendatas):
      node.value += (node.childrendatas[meta-1]).value
  if node.children == 0:
    node.value = sum(node.metasdatas)
  nodes.append(node)
  return node

readNode()

rootvalue = nodes[-1].value

print(rootvalue)