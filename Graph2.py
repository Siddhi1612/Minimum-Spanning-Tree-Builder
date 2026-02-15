import networkx as nx
import matplotlib.pyplot as plt
graph = nx.Graph()

while True:
        userAlgorithm = input("Which algorithm for the minimum spanning tree: ").lower()
        if userAlgorithm == "kruskal" or userAlgorithm == "prim":
             break
        
while True:
    try:     
        noOfEdges = int(input("number of edges: "))
        if noOfEdges > 1:
            break
        else:
            print("Invalid input, please try again.")
    except ValueError:
        print("Invalid input, please try again.")

while True:
    try:
        for i in range(1, noOfEdges+1):
            fromNode = input("Edge " + str(i) +" from: ")
            toNode = input("Edge " + str(i) +" to: ")
            edgeWeight = int(input("Weight of edge " + str(i) + ": "))
            graph.add_weighted_edges_from([
            (fromNode, toNode, edgeWeight)
            ])
        break
    except ValueError:
         print("Invalid Input, Please try again.")

def drawGraph(userMST):
#userMST = nx.minimum_spanning_tree(graph, algorithm = userAlgorithm)
    nodePositions = nx.spring_layout(graph)

    plt.subplot(1, 2, 1)
    print(f"graph: {graph}, node positions: {nodePositions}")
    input()
    nx.draw(graph,
        nodePositions,
        with_labels = True,
        node_color = 'black',
        node_size = 800,
        font_size = 10)
    edgeLabels = nx.get_edge_attributes(graph,'weight',)
    plt.subplot(1, 2, 2)
    print(userMST, nodePositions, type(userMST), type(nodePositions))
    print(f"graph: {userMST}, node positions: {nodePositions}")
    input()

    nx.draw(userMST, 
        nodePositions, 
        with_labels = True, 
        node_color = 'lightgreen', 
        node_size = 800, 
        font_size = 10)
    nx.draw_networkx_edge_labels(userMST, nodePositions, edge_labels=edgeLabels)

    nx.draw_networkx_edge_labels(graph,nodePositions,edge_labels = edgeLabels)
    plt.show()