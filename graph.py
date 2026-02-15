import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np
import random

def generateNodes():
    nodes = []
    for i in range(int(input("number of nodes: "))):
        nodes.append([random.randint(1,100),random.randint(1,100)])
    return nodes

def plotGraph(nodes):
    xList = [i[0] for i in nodes]
    yList = [i[1] for i in nodes]

    x = np.array(xList)
    y = np.array(yList)

    fig, ax = plt.subplots()
    sc = ax.scatter(x, y, picker=True)


    def on_click(event):
        if event.inaxes is not None:
            # Calculate distance from click to each point
            distances = np.hypot(x - event.xdata, y - event.ydata)
            ind = np.argmin(distances)
            plt.scatter(x[ind], y[ind], c='red', s=100, marker='o')
                    
            print(f"Selected point: ({x[ind]:.3f}, {y[ind]:.3f})")

    fig.canvas.mpl_connect("button_press_event", on_click)

    plt.show()

nNodes = generateNodes()
plotGraph(nNodes)

