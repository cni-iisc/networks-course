import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import networkx as nx

def visualizeGraph(adjMatrix, nodeSet= None):
  graph = nx.from_numpy_matrix(np.matrix(adjMatrix), create_using=nx.Graph)
  layout = nx.spring_layout(graph)
  labels = nx.get_edge_attributes(graph, "weight")
  nx.draw(graph, layout, node_size=600, with_labels=True)
  nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels) 
  plt.show()

def animatedGraph():
  pass