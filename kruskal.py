#set up the initial dictionaries for the parent node and size of treea
parent = {}
rank = {}

#sets up a new tree for each of the given nodes
def newTree(node):
    parent[node] = node
    rank[node] = 0

#helps to idenify the parent node
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

#combines two separate trees based on differences in rank
#hence, union by rank
def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        # Union by rank
        if rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        elif rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        else:
            parent[rootB] = rootA
            rank[rootA] += 1


def kruskal(nodes, edges):
    # nodes: list of vertices
    # edges: list of (weight, u, v)
    
    #validate nodes
    for weight, u, v in edges:
        if u not in nodes or v not in nodes:
            print(f"The edge ({u},{v}) references a node not in the graph")

    #new tree for each node
    for node in nodes:
        newTree(node)

    #sort edges in ascending order as in Kruskal's algorithm
    edges.sort()

    #initialise the MST and running weight counter
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((weight, u, v))
            total_weight += weight

    return mst, total_weight

"""
nodes = [0,1,2,3]
edges = [(1,0,2),
         (4,2,1),
         (5,2,3),
         (9,3,0)
        ]

mst, total = kruskal(nodes, edges)

print("MST:", mst)
print("Total weight:", total)
"""