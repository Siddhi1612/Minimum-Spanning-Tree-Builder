import networkx as nx
import matplotlib
#better version of matplotlib when other programs are running
# in parallel
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
graph = nx.Graph()

userAlgorithm = "kruskal"
def drawGraph(userMST):
#userMST = nx.minimum_spanning_tree(graph, algorithm = userAlgorithm)
    nodePositions = nx.spring_layout(graph)
    #input graph subplot
    plt.subplot(1, 2, 1)
    print(f"graph: {graph}, node positions: {nodePositions}")
    nx.draw(graph,
        nodePositions,
        with_labels = True,
        node_color = 'black',
        node_size = 800,
        font_size = 10)
    edgeLabels = nx.get_edge_attributes(graph,'weight',)
    #final mst subplot
    plt.subplot(1, 2, 2)
    print(userMST, nodePositions, type(userMST), type(nodePositions))
    print(f"graph: {userMST}, node positions: {nodePositions}")

    nx.draw(userMST, 
        nodePositions, 
        with_labels = True, 
        node_color = 'lightgreen', 
        node_size = 800, 
        font_size = 10)
    nx.draw_networkx_edge_labels(userMST, nodePositions, edge_labels=edgeLabels)
    
    nx.draw_networkx_edge_labels(graph,nodePositions,edge_labels = edgeLabels)
    plt.show()