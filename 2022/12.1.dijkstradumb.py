heightmap = []
with open('input12.txt') as f:
    for line in f:
        heightmap.append(list(line.strip()))

print(heightmap)

start = (0, 0)
end = (0, 0)
for x, line in enumerate(heightmap):
    if 'S' in line:
        start = (x, line.index('S'))
    if 'E' in line:
        end = (x, line.index('E'))
    
heightmap[start[0]][start[1]] = 'a'
heightmap[end[0]][end[1]] = 'z'

print(start)
print(end)
print(heightmap)

def h(pos):
    return ord(heightmap[pos[0]][pos[1]])

def invalid(pos):
    return (pos[0]>=len(heightmap) or pos[0]<0 or pos[1]>=len(heightmap[0]) or pos[1]<0)

def valid_move(f, t):
    if invalid(f):
        return False
    return h(f) + 1 >= h(t)

def candidates(pos):
    cand = []
    if valid_move((pos[0]-1,pos[1]), pos):
        cand.append((pos[0]-1,pos[1]))
    if valid_move((pos[0]+1,pos[1]), pos):
        cand.append((pos[0]+1,pos[1]))
    if valid_move((pos[0],pos[1]-1), pos):
        cand.append((pos[0],pos[1]-1))
    if valid_move((pos[0],pos[1]+1), pos):
        cand.append((pos[0],pos[1]+1))
    return cand

import sys
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = init_graph#self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(list(map(str,path)))))
    return shortest_path[target_node]

nodes = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        nodes.append((x,y))

init_graph = {}
for node in nodes:
    init_graph[node] = {}

for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        for can in candidates((x,y)):
            init_graph[(x, y)][can] = 1

g = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=g, start_node=end)

#print_result(previous_nodes, shortest_path, start_node=end, target_node=start)
lenzo = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        if heightmap[x][y]=='a':
            try:
                lenzo.append(print_result(previous_nodes, shortest_path, start_node=end, target_node=(x,y)))
            except KeyError:
                print(f'No path to {(x,y)}')
print(min(lenzo))