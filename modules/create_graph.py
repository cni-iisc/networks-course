import sys
import collections

__author__ = "Sharad Shriram"

class Node:
  def __init__(self, data=None, nodeProperty=None, indexLocation=None):
    self.data = data             # name of the node
    self.index = indexLocation
    self.adjacent = {}
    self.previous = []
    self.distance = sys.maxsize #distance set as infinity
    self.property = {} # type or function of the node
    self.visited = False

class Graph: 
  def __init__(self, nodes=None, directed=False):
    
    self.nodes = nodes
    self.directed = directed
    self.edgeList = []
    self.graph_data = {}
    self.adjList = collections.defaultdict(dict)
    for i in range(len(nodes)):
      self.nodes[i].index = i
  
  @classmethod
  def createGraph(self, nodes, directed=False):
    if type(nodes) == list:
      return Graph(nodes, directed)

    if type(nodes) == int:
      nodeList = []
      for i in range(nodes):
        nodeList.append(Node(i))
      return Graph(nodeList, directed)
  
  def add_Node(self, node):
    newIndex = len(self.nodes) - 1
    newNode = Node(node)
    newNode.index = newIndex
    self.nodes.append(node)

  def add_Edge(self, node1, node2, weight=1):
    node1Index, node2Index = self.get_nodeIndex(node1), self.get_nodeIndex(node2)

    if self.directed == False: # un-directed graph
      self.nodes[node1Index].adjacent[node2Index] = weight
      self.nodes[node2Index].adjacent[node1Index] = weight
      self.adjList[node1Index][node2Index] = weight
      self.adjList[node2Index][node1Index] = weight

    else: # directed graph
      self.nodes[node1Index].adjacent[node2Index] = weight
      self.adjList[node1Index][node2Index] = weight
    
    self.edgeList.append([node1Index, node2Index, weight])
  
  def delete_Edge(self, node1, node2):
    node1Index, node2Index = self.get_nodeIndex(node1), self.get_nodeIndex(node2)
    if self.directed == False:
      del self.nodes[node1Index].adjacent[node2Index]
      del self.nodes[node2Index].adjacent[node1Index]
      del self.adjList[node1Index][node2Index] 
      del self.adjList[node2Index][node1Index] 
    else:
      del self.nodes[node1Index].adjacent[node2Index]
      del self.adjList[node1Index][node2Index]


  def get_nodeIndex(self, node):
    if not isinstance(node, Node) and not isinstance(node, int):
      raise ValueError("Check Nodes: nodes should be an instance of Node Class or Int, not any other types")
    if isinstance(node, int):
      return node
    else:
      return node.index
  
  def get_allNodes(self):
    return self.nodes
  
  def get_allEdges(self):
    return self.edgeList
  
  def get_edgeWeight(self, node1, node2):
    try:
      node1Index, node2Index = self.get_nodeIndex(node1), self.get_nodeIndex(node2)
      return self.nodes[node1Index].adjacent[node2Index]
    except KeyError:
      return 0

  def get_connections(self, node):
    nodeIndex = self.get_nodeIndex(node)
    return self.nodes[nodeIndex].adjacent 

  def get_node(self, node):
    nodeIndex = self.get_nodeIndex(node)
    return [self.nodes[nodeIndex].index, self.nodes[nodeIndex].data, self.nodes[nodeIndex].property]

  def get_distance(self, node):
    nodeIndex = self.get_nodeIndex(node)
    return self.nodes[nodeIndex].distance
  
  def get_adjacentNodes(self, node):
    nodeIndex = self.get_nodeIndex(node)
    return str(nodeIndex) +"is adjacent to: " + str([ self.get_nodeIndex(node) for node in self.nodes[nodeIndex].adjacent])
  
  def get_previous(self, node):
    nodeIndex = self.get_nodeIndex(node)
    return self.nodes[nodeIndex].previous

  def get_adjList(self):
    return self.adjList

  def get_adjMatrix(self):
    self.adjMatrix = [[0]* len(self.adjList.keys()) for _ in range(len(self.adjList.keys()))]
    for key, value in self.adjList.items():
      for k, v in value.items():
        self.adjMatrix[key][k]= v
    return self.adjMatrix

  def set_previous(self, currentNode, previousNode):
    currentNodeIndex = self.get_nodeIndex(currentNode)
    self.nodes[currentNodeIndex].previous = previousNode

  def set_visited(self, node):
    nodeIndex = self.get_nodeIndex(node)
    self.nodes[nodeIndex].visited = True

  def set_distance(self, node, distance):
    nodeIndex = self.get_nodeIndex(node)
    self.nodes[nodeIndex].distance = distance

  def has_edge(self, node1, node2):
    node1Index, node2Index = self.get_nodeIndex(node1), self.get_nodeIndex(node2)
    if self.directed == False and ((self.nodes[node1Index].adjacent.get(node2Index) != None) or (self.nodes[node2Index].adjacent.get(node1Index) != None)):
      return 1
    else:
      return 0
    
    if self.directed == True and (self.nodes[node1Index].adjacent.get(node2Index) != None):
      return 1
    else:
      return 0

  def get_json(self):
    node_data = []
    for node in self.nodes:
      node_data.append({"index": node.index, "name": node.data, "property": node.property})

    edge_data = []
    for edge in self.edgeList:
      edge_data.append({"source": edge[0], "target": edge[1], "value": edge[2]})
    
    self.graph_data["isDirected"] = self.directed
    self.graph_data["nodes"] = node_data
    self.graph_data["edges"] = edge_data
    return self.graph_data