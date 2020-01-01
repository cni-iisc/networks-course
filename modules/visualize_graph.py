import os
import re
import fileinput
import numpy as np
import graphviz

def animateGraph(num):
  pass


def displayPath(edgeList):
  savedGraph = os.getcwd() + os.path.abspath("/modules/savedGraph.gv")

  f = open(savedGraph, "r")
  data = f.readlines()
  f.close()
  g = open(savedGraph, "w+")
  for index, line in enumerate(data):
    edgeLine = ""
    
    if re.findall("\w -- \w", line) and edgeLine == "":
      for (u, v, w) in edgeList:
        edge = line.strip().split()  #['\t0', '--', '1', '[label=1]\n']
        if (int(edge[0]) == u and int(edge[2]) == v) or (int(edge[0]) == v and int(edge[2]) == u) :
          edge[3] = edge[3].replace("]", ", color=red, penwidth=3]")
          edgeLine = "\t"+ edge[0] + " " + edge[1] + " " + edge[2]+ " " +edge[3] +"\n"
          line = edgeLine

    g.write(line)
  g.close()

  return graphviz.Source.from_file(savedGraph)


def visualizeGraph(graph):
    if graph.directed != True:
      visualGraph = graphviz.Graph('G',  node_attr={'shape': 'circle', 'color': 'lightblue2', 'style': 'filled'})
    else:
      visualGraph = graphviz.Digraph('G',  node_attr={'shape': 'circle', 'color': 'lightblue2', 'style': 'filled'})

    for gNode in graph.get_allNodes():
      visualGraph.node(str(gNode.index), str(gNode.index))
    for (u, v, w) in graph.get_allEdges():
      visualGraph.edge(str(u), str(v), label=str(w))
    visualGraph.save(filename=os.path.abspath(os.getcwd() + "/modules/savedGraph.gv"))
    return graphviz.Source(visualGraph)