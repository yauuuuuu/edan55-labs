import copy
import math

# ============== Algorithm ==============

def R0 (graph):

    # Add numIter global counter
    global numIter_R0
    numIter_R0 += 1

    # Creating clone graphs for recursive call
    new_graph = copy.deepcopy(graph)
    new_graph_2 = copy.deepcopy(graph)

    # Check if input graph is empty
    if graph == {}:
        return 0

    max_degree = 0
    u = None

    for v in graph:
        if graph[v] == []:
            del new_graph[v]
            return 1 + R0(new_graph)

        # Identifying vertex u with maximum degree
        if len(graph[v]) > max_degree:
            max_degree = len(graph[v])
            u = v
        
    # G[V - N[u]]
    for neighbour in graph[u]:
        delete_node(new_graph, neighbour)
    delete_node(new_graph, u)
    
    # G[V - u]
    delete_node(new_graph_2, u)

    return max(1 + R0(new_graph), R0(new_graph_2))

def R1 (graph):

    # Add numIter global counter
    global numIter_R1
    numIter_R1 += 1

    # Creating clone graphs for recursive call
    new_graph = copy.deepcopy(graph)
    new_graph_2 = copy.deepcopy(graph)

    # Check if input graph is empty
    if graph == {}:
        return 0
    
    # Check for any vertex with degree = 1
    for v in graph:
        if len(graph[v]) == 1:

            # G[V - N[v]]
            for neighbour in graph[v]:
                delete_node(new_graph, neighbour)
            delete_node(new_graph, v)

            return 1 + R1(new_graph)

    max_degree = 0
    u = None

    for v in graph:
        if graph[v] == []:
            del new_graph[v]
            return 1 + R1(new_graph)

        # Identifying vertex u with maximum degree
        if len(graph[v]) > max_degree:
            max_degree = len(graph[v])
            u = v
    
    # G[V - N[u]]
    for neighbour in graph[u]:
        delete_node(new_graph, neighbour)
    delete_node(new_graph, u)

    # G[V - u]
    delete_node(new_graph_2, u)

    return max(1 + R1(new_graph), R1(new_graph_2))

def R2 (graph):

    # Add numIter global counter
    global numIter_R2
    numIter_R2 += 1

    # Creating clone graphs for recursive call
    new_graph = copy.deepcopy(graph)
    new_graph_2 = copy.deepcopy(graph)

    # Check if input graph is empty
    if graph == {}:
        return 0

    # Check for any vertex with degree = 2
    for v in graph:
        if len(graph[v]) == 2:

            # G[V - N[v]]
            for neighbour in graph[v]:
                delete_node(new_graph, neighbour)
            delete_node(new_graph, v)

            u = graph[v][0]
            w = graph[v][1]

            if w in graph[u]:
                return 1 + R2(new_graph)
            else:
                # Identify neighbours of u and w (excluding u,w and v)
                neighbours = set(graph[u] + graph[w])
                neighbours.discard(u)
                neighbours.discard(w)
                neighbours.discard(v)

                # Add new vertex z
                z = -1
                for v in new_graph:
                    if v > z:
                        z = v
                z += 1
                new_graph[z] = list(neighbours)

                for neighbour in neighbours:
                    new_graph[neighbour].append(z)

                return 1 + R2(new_graph)

    # Check for any vertex with degree = 1
    for v in graph:
        if len(graph[v]) == 1:

            # G[V - N[v]]
            for neighbour in graph[v]:
                delete_node(new_graph, neighbour)
            delete_node(new_graph, v)
            
            return 1 + R2(new_graph)

    max_degree = 0
    u = None

    for v in graph:
        if graph[v] == []:
            del new_graph[v]
            return 1 + R2(new_graph)

        # Identifying vertex u with maximum degree
        if len(graph[v]) > max_degree:
            max_degree = len(graph[v])
            u = v
        

    # G[V - N[u]]
    for neighbour in graph[u]:
        delete_node(new_graph, neighbour)
    delete_node(new_graph, u)

    # G[V - u]
    delete_node(new_graph_2, u)

    return max(1 + R2(new_graph), R2(new_graph_2))


def delete_node (graph, node):

    if node not in graph:
        return

    for neighbor in graph[node]:
        graph[neighbor].remove(node)

    del graph[node]

# ============== Main ==============
datas = ["30", "40", "50", "60","70","80","90","100","110","120","130"]
datas_R0 = ["30", "40", "50", "60"]
datas_R1 = ["30", "40", "50", "60","70","80","90","100"]

logResults_R0 = []
logResults_R1 = []
logResults_R2 = []

for data in datas:
    filename = f"g{data}.in"
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

    # Number of iterations
    numIter_R0 = 0
    numIter_R1 = 0
    numIter_R2 = 0

    print(data)
    if data in datas_R0:
        print("R0: ", R0(graph), numIter_R0)
        logResults_R0.append(math.log(numIter_R0))

    if data in datas_R1:    
        print("R1: ", R1(graph), numIter_R1)
        logResults_R1.append(math.log(numIter_R1))

    print("R2: ", R2(graph), numIter_R2)
    logResults_R2.append(math.log(numIter_R2))

# Save results to a .txt file
with open('result.txt', 'w') as f:

    for data in datas:
        f.write('%s ' % data)
    f.write('\n')

    for item in logResults_R0:
        f.write('%d ' % item)
    f.write('\n')

    for item in logResults_R1:
        f.write('%d ' % item)
    f.write('\n')

    for item in logResults_R2:
        f.write('%d ' % item)
    f.write('\n')