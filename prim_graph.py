import math
import heapq

def primGraph(graph):
    #input validation
    try:
        if not isinstance(graph, list):
            raise TypeError("Graph must be a list")
                
        n = len(graph)

        for neighbours in graph:
            if not isinstance(neighbours, list):
                raise TypeError("Each adjacency entry must be a list")
            
            for edge in neighbours:
                if not isinstance(edge, tuple) or len(edge) != 2:
                    raise ValueError("Edges must be tuples")
                i, j = edge
                if not isinstance(i, int) or i < 0 or i >= n:
                    raise ValueError("Invalid vertex edge")
                if not isinstance(j, (int, float)):
                    raise TypeError("Weight must be a number")
    except Exception as e:
        print(f"Input error is {e}")
        return None

    #initialise all arrays in a similar fashion to the distance matrix as input
    inMST = [False] * n
    parent = [-1] * n
    key = [math.inf] * n

    #set starting vertex as 0
    key[0] = 0

    #initialises the queue as a key-value pair
    #essentially it costs 0 to have this node in the MST
    priorityQueue = [(0, 0)]

    #This loop is meant to check each connection of the vertex
    while priorityQueue:
        #unpacks the tuple 
        weight_i,i = heapq.heappop(priorityQueue)

        if inMST[i]:
            continue

        inMST[i] = True

        for j, iWeights in graph[i]:
            #checks if the node has already been visited and if the weight
            #of the edge is less than the current minimum weight which is stored in key
            #Then, the new weight becomes the knew key value of that connection and is 
            #added to the minimum spanning tree via the parent array
            if not inMST[j] and iWeights < key[j]:
                key[j] = iWeights
                parent[j] = i
                heapq.heappush(priorityQueue, (key[j], j))

    return parent,key

"""
graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)]
]

#outputs as normal
parent,key = primGraph(graph)

print("Edge   Weight")
for j in range(1, len(graph)):
    print(parent[j], "-", j, "   ", key[j])
"""