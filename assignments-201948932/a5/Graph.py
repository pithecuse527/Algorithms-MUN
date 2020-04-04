#!/usr/bin/python3

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
  __slots__ = '_edges', '_vertices'

  def __init__(self):
    self._edges    = []
    self._vertices = []

  #-- Public methods
  def edges(self):
    """ Return all edges of the graph. """
    # ... Implement this (1)
    return [] #replace to your one code

  def edgeCount(self):
    """ Return the number of edges in the graph. """
    # ... Implement this (2)
    return [] #replace to your one code

  def vertices(self):
    """ Return all vertices of the graph. """
    # ... Implement this (3)
    return [] #replace to your one code

  def vertexCount(self):
    """ Return the number of vertices in the graph. """
    # ... Implement this (4)
    return [] #replace to your one code

  def getEdge(self, v1, v2):
    """ Return the edge with vertices v1 to v2, or None if not adjacent. """
    # ... Implement this (5)
    return None #replace to your one code

  def getVertexByValue(self, e):
    """ Return the vertex that has element of value e. """
    # ... Implement this (6)
    return None #replace to your one code
  def incidentEdges(self, v):
    """ Return a collection of all edges that are incident to vertex v in the graph. """
    # ... Implement this (7)
    return [] #replace to your one code

  def print(self):
    """ Print the edge list with the format:
    """
    print("Edge List:" )
    for e in self.edges():
      print(e)
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
    
def DFS(g):
  # Implement the depth-first search algorithm from the class notes.
  # Collect the discovered edges that form the DFS tree of 'g' and return the collection
  # ... Implement this (8)
  return [] #replace to your one code


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
g.print()
print()

# Call DFS on g, to get the discovery edges
discovery = DFS(g)
print("DFS edges:")
for e in discovery:
  print(e)
print()

# Determine whether the graph is connected
# ... Implement this (9)
print("Graph is connected:", False) #replace to your one code
