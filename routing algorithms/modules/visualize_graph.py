import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import networkx as nx

def animateGraph(num):
  pass


def displayPath(graph, edges):
    f, ax = plt.subplots(figsize=(8,6))
    layout = nx.shell_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_nodes(graph, pos=layout, node_size=700, node_color="gray") #place the nodes
    nx.draw_networkx_edges(graph, pos=layout, alpha=0.3, width=0.5)
    nx.draw_networkx_edges(graph, pos=layout, edgelist=edges, width=4, edge_color='r', style="dashed")

    nx.draw_networkx_labels(graph, pos=layout, font_size=20)
    nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels, font_size=20)

    ax.axis('off')
    return ax


def visualizeGraph(adjMatrix, nodeSet=None):
    graph = nx.from_numpy_matrix(np.matrix(adjMatrix), create_using=nx.Graph)
    layout = nx.shell_layout(graph)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw(graph, layout, node_size=800, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels)
    plt.axis('off')
    plt.show()
    return graph