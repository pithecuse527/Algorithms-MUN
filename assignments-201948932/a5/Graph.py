#!/usr/bin/python3

"""
  Assignment5 implementation using Graph ADT
  201948932
  Hong Geun Ji
  03/04/20
"""

# Simple Vertex class
class Vertex:
  """ Lightweight vertex structure for a graph.
      Vertices can have the following labels:
        UNEXPLORED
        VISITED
      Assuming the element of a vertex is string type
  """
  __slots__ = '_element', '_label'

  def __init__(self, element, label="UNEXPLORED"):
    """ Constructor. """
    self._element = element
    self._label = label

  def element(self):
    """ Return element associated with this vertex. """
    return self._element

  def getLabel(self):
    """ Get label assigned to this vertex. """
    return self._label

  def setLabel(self, label):
    """ Set label after the vertex has been created. """
    if label not in ("UNEXPLORED", "VISITED"):     # validation check
      print("The label is not valid...")
      return
    
    self._label = label

  def __str__(self):
    """ Used when printing this object. """
    return "(%s, %s)" % (self._element,self._label)

# Simple Edge class
class Edge:
  """ Lightweight edge structure for a graph.
      Edges can have the following labels:
        UNEXPLORED
        DISCOVERY
        BACK
  """
  __slots__ = '_origin', '_destination','_element', '_label'

  def __init__(self, u, v, element = None,label = "UNEXPLORED"):
    """ Constructor.  Note that u and v are Vertex objects. """
    self._origin = u
    self._destination = v
    self._element = element
    self._label = label

  def getLabel(self):
    """ Get label assigned to this edge. """
    return self._label

  def setLabel(self, label):
    """ Set label after the edge has been created. """
    if label not in ("UNEXPLORED", "DISCOVERY", "BACK"):     # validation check
      print("The label is not valid...")
      return
    
    self._label = label

  def endpoints(self):
    """ Return (u,v) tuple for source and destination vertices. """
    return (self._origin, self._destination)

  def isIncident(self, v):
    """ Return True if vertex v is incident upon this edge, else False. """
    return v == self._origin or v == self._destination

  def isEndponts(self, u, v):
    """ Return True if both vertics u and v are incident upon this edge, else False. """
    return self.isIncident(u) and self.isIncident(v)
  
  def opposite(self, v):
    """ Return the vertex that is opposite v on this edge. """
    if not isinstance(v, Vertex):
      raise TypeError('v must be a Vertex')
    if v not in [self._destination, self._origin]:
      raise ValueError('v not incident to edge')
    return self._destination if v is self._origin else self._origin

  def __str__(self):
    """ Used when printing this object. """
    return "(%s, %s, %s)" %  (self._origin._element,self._destination._element,self._label)

class Graph:
  """ Partial Graph ADT represented by an edge list structure."""
      
  #---- Graph implementation -------------------------
  __slots__ = '_edges', '_vertices', '_DFS_lst'

  def __init__(self):
    self._edges    = []
    self._vertices = []
    self._DFS_lst = []

  #-- Public methods
  def edges(self):
    """ Return all edges of the graph. """
    # ... Implement this (1)
    return self._edges

  def edgeCount(self):
    """ Return the number of edges in the graph. """
    # ... Implement this (2)
    return len(self._edges)

  def vertices(self):
    """ Return all vertices of the graph. """
    # ... Implement this (3)
    return self._vertices

  def vertexCount(self):
    """ Return the number of vertices in the graph. """
    # ... Implement this (4)
    return len(self._vertices)

  def getEdge(self, v1, v2):
    """ Return the edge with vertices v1 to v2, or None if not adjacent. """
    # ... Implement this (5)
    for e in self.edges():    # check every edge in the list
      if v1 in e.endpoints() and v2 in e.endpoints():    # based on undirected graph
        return e
    return None   # if cannot cannot find, return None

  def getVertexByValue(self, e):
    """ Return the vertex that has element of value e. """
    # ... Implement this (6)
    for v in self.vertices():   # check every vertex in the list
      if v.element() == e:
        return v
    return None   # if cannot cannot find, return None
    
  def incidentEdges(self, v):
    """ Return a collection of all edges that are incident to vertex v in the graph. """
    # ... Implement this (7)
    incident_of_v = []    # make temp list for saving incident on v
    for e in self.edges():
      if e.isIncident(v):         # if the e is incident on v,
        incident_of_v.append(e)   # save the e to the list
    return incident_of_v

  def print(self):
    """ Print the edge list with the format:
    """
    print("Edge List:" )
    for e in self.edges():
      print(e)
    print()
    print("Vertex List:")
    for v in self.vertices():
      print(v)
    print()

  def insert_vertex(self, x=None):
    """Insert and return a new Vertex with element x."""
    v = Vertex(x)
    self._vertices.append(v)
    return v
      
  def insert_edge(self, u, v, x=None):
    """Insert and return a new Edge from u to v with auxiliary element x.

    Raise a ValueError if u and v are not vertices of the graph.
    Raise a ValueError if u and v are already adjacent.
    """
    if self.getEdge(u, v) is not None:      # includes error checking
      raise ValueError('u and v are already adjacent')
    e = Edge(u, v, x)
    self._edges.append(e)
  
  def is_connected(self):
    """Check whether the graph is connected or not.
    If every vertex is VISITED after DFS, it means connected. 
    If not, it is not connected.
    """
    
    DFS(self)   # do DFS first
    for v in self._vertices:
      if v.getLabel() != "VISITED":   # if any vertex is not visited,
        return False                # return False
    return True

def DFS(g, v = None, DFS_e_lst = []):
  # Implement the depth-first search algorithm from the class notes.
  # Collect the discovered edges that form the DFS tree of 'g' and return the collection
  # ... Implement this (8)
  if not v: v = g.vertices()[0]   # if this method called at the first time,
  w = None
  v.setLabel("VISITED")
  
  for e in g.incidentEdges(v):
    if e.getLabel() == "UNEXPLORED":
      w = e.opposite(v)
      if w.getLabel() == "UNEXPLORED":
        e.setLabel("DISCOVERY")
        DFS_e_lst.append(e)
        DFS(g, w)
      else:
        e.setLabel("BACK")
  
  if v == g.vertices()[0]:    # return the edge list only one time (if the DFS ends)
    return DFS_e_lst
  return
  
#-- Main method
v_elements = ["A","B","C","D","E"]
g = Graph()
for v in range(5):
  g.insert_vertex(v_elements[v])
  
g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("B"))
g.insert_edge(g.getVertexByValue("A"),g.getVertexByValue("C"))
g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("C"))
g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("D"))
g.insert_edge(g.getVertexByValue("B"),g.getVertexByValue("E"))
g.insert_edge(g.getVertexByValue("C"),g.getVertexByValue("D"))
g.insert_edge(g.getVertexByValue("C"),g.getVertexByValue("E"))

# Print all edges
print("Edges:", g.edgeCount())
for e in g.edges():
  print(e)
print()

# Print all vertices
print("Vertices:", g.vertexCount())
for v in g.vertices():
  print(v)
print()

# Print the actual graph (in matrix form)
print("=============== Before DFS ===============")
g.print()
print("==========================================\n")


#Call DFS on g, to get the discovery edges
discovery = DFS(g)
print("DFS edges:")
for e in discovery:
  print(e)
print()

# Print the actual graph again after DFS (in matrix form)
print("=============== After DFS ===============")
g.print()
print("==========================================\n")

# Determine whether the graph is connected
# ... Implement this (9)
print("Graph is connected:", g.is_connected())
