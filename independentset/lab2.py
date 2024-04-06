import copy

# ============== Algorithm ==============
def R0 (graph):

    # Check if input graph is empty
    if graph == {}:
        return 0
    
    v_without_neighbours = False
    max_degree = 0
    u = None

    new_graph = copy.deepcopy(graph)
    new_graph_2 = copy.deepcopy(graph)

    for v in graph:
        if graph[v] == []:
            v_without_neighbours = True
            break
        if len(graph[v]) > max_degree:
            max_degree = len(graph[v])
            u = v
        
    if v_without_neighbours == True:
        del new_graph[v]
        return 1 + R0(new_graph)
    else:
        # G[V - N[u]]
        for neighbour in graph[u]:
            delete_node(new_graph, neighbour)
        
        # G[V - u]
        delete_node(new_graph_2, u)

        return max(1 + R0(new_graph), R0(new_graph_2))

def delete_node (graph, node):
    for neighbor in graph[node]:
        graph[neighbor].remove(node)

    del graph[node]

# ============== Main ==============
filename = "g30.in"
file = open(f"data/{filename}",'r')

# Reading the text input file
n = int(file.readline().strip())

# Initialise graph
graph = {}

for v_index in range(n):

    graph[v_index] = []

    row = file.readline().strip().split(" ")

    for neighbour_index in range(n):
        if row[neighbour_index] == '1':
            graph[v_index].append(neighbour_index)
            
file.close()

print(graph)
print(R0(graph))

