import math

def primMatrix(graph):
    #input validation
    try:
        if not isinstance(graph, list):
            raise TypeError("Graph must be a list")
    
        n = len(graph)

        for row in graph:
            if len(row) != n:
                raise ValueError("Graph must be a square matrix")
            
            for i in range(n):
                for j in range(n):
                    if not isinstance(graph[i][j], (int, float)):
                        raise TypeError("Weights must be numbers")
    except Exception as e:
        print(f"Input Error: {e}")
        return None
    #initialising the lowest weight with an arbitrarily large number
    key = [math.inf] * n
    #initialising the array which contains the final MST
    parent = [-1] * n
    #initialising that none of the nodes have been visiting
    inMST = [False] * n

    #sets starting vertex to the first one
    key[0] = 0

    #loops through each 'from' node
    for i in range(n):
        min_key = math.inf
        #check if the node's been visited or
        #if the weight is less than the current minimum key value
        for j in range(n):
            if not inMST[j] and key[j] < min_key:
                #update the new weight
                min_key = key[j]
                i = j
        #set the node as visited
        inMST[i] = True

        #loops through each 'to' node and repeats
        for j in range(n):
            weight = graph[i][j]
            if weight != 0 and not inMST[j] and weight < key[j]:
                key[j] = weight
                #adds the edge to the final minimum spanning tree
                parent[j] = i

    return parent

"""
inpGraph = [[0, 2, 0, 6, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]] 

#calls the function and sets up the output
parent = primMatrix(inpGraph)
print("Edge   Weight")
for i in range(1, len(inpGraph)):
    print(parent[i], "-", i, "   ", inpGraph[i][parent[i]])
"""