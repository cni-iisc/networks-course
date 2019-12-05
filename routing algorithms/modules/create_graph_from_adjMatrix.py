import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Node:
  def __init__(self, data=None, indexLocation=None):
    self.data = data
    self.index = indexLocation

class Graph:
  @classmethod #Graph class is implicitly passed as first argument
  def create_from_nodeList(self, nodeList):
    #if number of verices is specified
    if type(nodeList) == int:
      createdNodes = []
      for i in range(nodeList):
        createdNodes.append(Node(i))
      return Graph(len(createdNodes), len(createdNodes), createdNodes)
    #if vertices are explicitly specified as a list
    if type(nodeList) == list:
      return Graph(len(nodeList), len(nodeList), nodeList)

  def __init__(self, row, column, nodeList = None):
    #initializing the adjacency matrix
    #representation: row = source and column = destination
    self.adjMatrix = [[0]* column for _ in range(row)]
    self.nodes = nodeList
    for i in range(len(self.nodes)):
      self.nodes[i].index = i

  def get_adjMatrix(self):
    return self.adjMatrix

  def print_adjMatrix(self):
    for row in self.adjMatrix:
      print(row)

  def get_nodeIndex(self, node):
    if not isinstance(node, Node) and not isinstance(node, int):
      raise ValueError("node must be an Integer or a Node Object")
    if isinstance(node, int):
      return node
    else:
      return node.index
  
  #connects node 1 and node 2
  def connect_dir(self, node1, node2, weight=1):
    node1, node2 = self.get_nodeIndex(node1), self.get_nodeIndex(node2)
    self.adjMatrix[node1][node2] = weight

  #creating weighted edges
  def connect(self, node1, node2, weight):
    self.connect_dir(node1, node2, weight)
    self.connect_dir(node2, node1, weight)
  
  #get the weight from the adjacency matrix
  def getWeight(self, node1, node2):
    node1, node2 = self.get_nodeIndex(node1), self.get_nodeIndex(node2)
    return self.adjMatrix[node1][node2]
  
  def connectionsFrom(self, node):
    currentNode = self.get_nodeIndex(node)
    return [(self.nodes[col_num], self.adjMatrix[currentNode][col_num]) for col_num in range(len(self.adjMatrix[currentNode])) if self.adjMatrix[currentNode][col_num] != 0]

  def connectionsTo(self, node):
    currentNode = self.get_nodeIndex(node)
    matColumn = [row[currentNode] for row in self.adjMatrix]
    return [(self.nodes[row_num], matColumn[row_num]) for row_num in range(len(matColumn)) if matColumn[row_num] != 0]

  def getNode(self, index):
    return self.nodes[index]

  def disconnect(self, node1, node2):
    self.disconnect_dir(node1, node2)
    self.disconnect_dir(node2, node1)

  def disconnect_dir(self, node1, node2):
    node1, node2 = self.get_nodeIndex(node1), self.get_nodeIndex(node2)
    self.adjMatrix[node1][node2] = 0

  #is node 2 reachable from node 1
  def isTraversable(self, node1, node2):
    node1, node2 = self.get_nodeIndex(node1), self.get_nodeIndex(node2)
    if self.adjMatrix[node1][node2] != 0:
      return 1
    else:
      return 0
  
  def edgeExists(self, node1, node2):
    return self.isTraversable(node1, node2) or self.isTraversable(node2, node1)

  def addNode(self, node):
    self.nodes.append(node)
    node.index = len(self.nodes) - 1
    for row in self.adjMatrix:
      row.append(0)     
    self.adjMatrix.append([0] * (len(self.adjMatrix) + 1))
 

  # #compute centrality
  # #compute degree
  # #determine connectedness of the graph - networkx
  # # determine clustering coefficient 
  # def standardDijkstra(self, node):
  #     nodenum = self.get_nodeIndex(node) 

  #     # Make an array keeping track of distance from node to any node
  #     # in self.nodes. Initialize to infinity for all nodes but the 
  #     # starting node, keep track of "path" which relates to distance.
  #     # Index 0 = distance, index 1 = node hops
  #     dist = [None] * len(self.nodes)
  #     for i in range(len(dist)):
  #         dist[i] = [float("inf")]
  #         print(self.nodes)
  #         print(self.nodes)
  #         dist[i].append([self.nodes[nodenum]])
      
  #     dist[nodenum][0] = 0
  #     # Queue of all nodes in the graph
  #     # Note the integers in the queue correspond to indices of node
  #     # locations in the self.nodes array
  #     queue = [i for i in range(len(self.nodes))]
  #     # Set of numbers seen so far
  #     seen = set()
  #     while len(queue) > 0:
  #         # Get node in queue that has not yet been seen
  #         # that has smallest distance to starting node
  #         min_dist = float("inf")
  #         min_node = None
  #         for n in queue: 
  #             if dist[n][0] < min_dist and n not in seen:
  #                 min_dist = dist[n][0]
  #                 min_node = n
          
  #         # Add min distance node to seen, remove from queue
  #         queue.remove(min_node)
  #         seen.add(min_node)
  #         # Get all next hops 
  #         connections = self.connectionsFrom(min_node)
  #         # For each connection, update its path and total distance from 
  #         # starting node if the total distance is less than the current distance
  #         # in dist array
  #         print("current node %s" % min_node)
  #         for (node, weight) in connections: 
  #             tot_dist = weight + min_dist
  #             if tot_dist < dist[node.index][0]:
  #                 dist[node.index][0] = tot_dist
  #                 dist[node.index][1] = list(dist[min_node][1])
  #                 dist[node.index][1].append(node)
  #                 print("Distance from Node %s to Node %s is of weight %d" % (min_node, node.index, weight))
  #         print("-------------------------------------------------")
  #     return dist  
