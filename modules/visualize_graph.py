import os
import re
import json
import graphviz

def displayPath(edgeList, filename):
  savedGraph = os.path.abspath(os.getcwd() + "/graphFiles/"+filename+".gv")
  f = open(savedGraph, "r")
  data = f.readlines()
  f.close()
  temp = os.path.abspath(os.getcwd() + "/graphFiles/"+filename+"_temp.gv")
  g = open(temp, "w+")
  for line in data:
    edgeline = ""
    if re.findall(r"\w -- \w", line) and edgeline == "":
      for (u, v, w) in edgeList:
        edge = line.strip().split()  #['\t0', '--', '1', '[label=1]\n']
        if (int(edge[0]) == u and int(edge[2]) == v) or (int(edge[0]) == v and int(edge[2]) == u) :
          weight = re.findall(r"[+-]?\d+", edge[3])[0]
          edge[3] = edge[3].replace(("[label="+weight+"]"), ("[label="+weight+", color=red, penwidth=3]"))
          edgeLine = "\t"+ edge[0] + " " + edge[1] + " " + edge[2]+ " " +edge[3] +"\n"
          line = edgeLine
    if re.findall(r"\w -> \w", line) and edgeline == "":
      for (u, v, w) in edgeList:
        edge = line.strip().split()  #['\t0', '--', '1', '[label=1]\n']
        if (int(edge[0]) == u and int(edge[2]) == v) :
          weight = re.findall(r"[+-]?\d+", edge[3])[0]
          edge[3] = edge[3].replace(("[label="+weight+"]"), ("[label="+weight+", color=red, penwidth=3]"))
          edgeLine = "\t"+ edge[0] + " " + edge[1] + " " + edge[2]+ " " +edge[3] +"\n"
          line = edgeLine  
    g.write(line)
  g.close()

  return graphviz.Source.from_file(temp)




def visualizeGraph(graph, filename):
    if graph.directed != True:
      visualGraph = graphviz.Graph('G',  node_attr={'shape': 'circle', 'color': 'lightblue2', 'style': 'filled'})
    else:
      visualGraph = graphviz.Digraph('G',  node_attr={'shape': 'circle', 'color': 'lightblue2', 'style': 'filled'})

    for gNode in graph.get_allNodes():
      visualGraph.node(str(gNode.index), str(gNode.index))
    
    for (u, v, w) in graph.get_allEdges():
      visualGraph.edge(str(u), str(v), label=str(w))

    visualGraph.save(filename=os.path.abspath(os.getcwd() + "/graphFiles/"+filename+".gv"))
    return graphviz.Source(visualGraph)