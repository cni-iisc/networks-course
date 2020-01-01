from modules.create_graph import *
from modules.visualize_graph import *


a = Node("router", {"type":"router"})
b = Node("node-1", {"type": "edge-device"})
c = Node("node-2", {"type": "edge-device"})
d = Node()
e = Node()
p =  Node()
q =  Node()
r =  Node()
f = Node("node-3", {"type": "edge-device"})
# f = Node(Graph.createGraph([p, q, r], directed=False), {"type": "Autonomous System"})

graphs = Graph.createGraph([a, b, c, d, e, f], directed=False)


graphs.add_Edge(a,b,1)
graphs.add_Edge(a,c,10)
graphs.add_Edge(a,e,2)
graphs.add_Edge(b,c,10)
graphs.add_Edge(b,d,6)
graphs.add_Edge(c,d,1)
graphs.add_Edge(c,f,10)
graphs.add_Edge(d,e,3)


visualizeDiGraph(graphs)