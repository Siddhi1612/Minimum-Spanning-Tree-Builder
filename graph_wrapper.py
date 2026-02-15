import networkx as nx
import prim_matrix
import prim_graph
import kruskal
import Graph3


#convert networkx graph to be compatible with kruskal's input
def nxKruskal(graph):
    nodes = list(graph.nodes)
    edges = []
    #loop through each edge and its weight and put in the form
    #weight-from-to because networkx uses from-to-weight format
    for u, v, data in graph.edges(data = True):
        weight = data['weight']
        edges.append((weight, u, v))
    
    return nodes, edges

#convert the networkx graph into a distance matrix compatible 
#with prim's
def nxPrimMatrix(graph):
    nodes = list(graph.nodes())
    index = {nodes[i]: i for i in range(len(nodes))}
    n = len(nodes)

    # create matrix of zeros
    matrix = [[0 for a in range(n)] for a in range(n)]
    #loop through and convert the matrix form appropriately
    for u, v, data in graph.edges(data = True):
        w = data['weight']
        i, j = index[u], index[v]
        matrix[i][j] = w
        matrix[j][i] = w

    return matrix, nodes

#convert the networkx graph into an adjacency list for other
#version of Prim's
def nxPrimAdjList(graph):
    nodes = list(graph.nodes())
    #create dictionary to map each node label to an integer index
    print(nodes)
    index = {nodes[i]: i for i in range(len(nodes))}
    print(index)
    #initialises empty list with one list per node, storing neighbours
    adjList = [[] for a in range(len(nodes))]
    print(f"empty list: {adjList}")

    for u, v, data in graph.edges(data=True):
        w = data['weight']
        uIndex = index[u]
        vIndex = index[v]
        print(f"uIndex = {uIndex}, vIndex = {vIndex}")
        #converts input vertices into appropriate indexes
        wayOutTuple = (vIndex, w)
        returnTuple = (uIndex, w)
        adjList[uIndex].append(wayOutTuple) 
        adjList[vIndex].append(returnTuple)
    print(adjList)
    return adjList,nodes

#function to computer the mst with networkx
def findMST(graph, userAlgorithm, primType):
    if userAlgorithm == "kruskal":
        #executes Kruskal part
        nodes,edges = nxKruskal(graph)
        mst,total = kruskal.kruskal(nodes,edges)
        return[(u,v) for (w, u, v) in mst]
    
    elif userAlgorithm == "prim":
        #executes Prim's with matrix input
        if primType == "matrix":
            matrix, nodes = nxPrimMatrix(graph)
            parent = prim_matrix.primMatrix(matrix)
            return [(nodes[parent[i]], nodes[i]) for i in range(1, len(nodes))]
        #executes Prim's with graph input
        elif primType == "graph":
            adjList,nodes = nxPrimAdjList(graph)
            parent,key = prim_graph.primGraph(adjList)
            return [(nodes[parent[i]],nodes[i]) for i in range(1, len(parent))]



#main program uses a defined graph function from test.py using the payload variable
def graph(inps,edges):
    Graph3.userAlgorithm = inps["userAlgorithm"]
    nEdges = inps["numberOfEdges"]
    for i in range(int(nEdges)):
        Graph3.graph.add_weighted_edges_from([(edges[f"{i}fromNode"],edges[f"{i}toNode"],int(edges[f"{i}edgeWeight"]))])
    mst_edges = findMST(Graph3.graph, Graph3.userAlgorithm, inps["primType"])
    userMST = nx.Graph()
    userMST.add_nodes_from(Graph3.graph.nodes())
    userMST.add_edges_from(mst_edges)
    Graph3.drawGraph(userMST)