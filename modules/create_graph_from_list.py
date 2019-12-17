"""Creating a graph given adjacency list"""

__author__      = "Sharad Shriram"

import sys

class Node():
    def __init__(self, node):
      self.id = node
      self.adjacent = {} 
      self.distance = sys.maxsize # Set distance to infinity for all nodes
      self.visited = False # Mark all nodes unvisited  
      self.previous = None # Predecessor

    def add_neighbor(self, neighbor, weight=0.0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])
    
    def get_node(self, id):
        if self.id == id:
         return self



class build_graph(object):
  def __init__(self, adjList):
    self.adjList = adjList
    self.num_nodes = 0
    self.nodesDict = {}
    
    for key, value in self.adjList.items():
      self.add_node(key)
      for k, v in value.items():
        self.add_edge(key, k, v)

  def add_node(self, node):
    self.num_nodes = self.num_nodes + 1
    new_node = Node(node)
    self.nodesDict[node] = new_node
    return new_node

  def add_edge(self, frm, to, weight = 0.0):
      if frm not in self.nodesDict:
          self.add_node(frm)
      if to not in self.nodesDict:
          self.add_node(to)
      
      self.nodesDict[frm].add_neighbor(self.nodesDict[to], weight)
      self.nodesDict[to].add_neighbor(self.nodesDict[frm], weight)

  def get_all_nodes(self):
    return self.nodesDict.keys()

  def set_previous(self, current):
      self.previous = current

  def get_previous(self, current):
      return self.previous

  def get_node(self, n):
      if n in self.nodesDict:
          return self.nodesDict[n]
      else:
          return None

  def __iter__(self):
      return iter(self.nodesDict.values())