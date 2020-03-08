import random

class CircularDoublyLinkedList:
  """A circular doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, prev, next):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._start = None
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------
  
  def _first_insert(self, e):
    """First insertion of the circular list"""
    self._start = self._Node(e, None, None)
    self._start._prev = self._start
    self._start._next = self._start
    self._size += 1

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element
    
  #-------------------------- public utilities --------------------------
  
  # todo:
    # starter and tail is not same!! -> usually we think tail is next or prev of the start node
    # consider using _insert_between method for insertBeforeHeader() and insertAtEnd()
    # can the tail changed by the methods? if so, the insertBeforeHeader method and insertAtEnd is same. ->
  
  def insertBeforeHeader(self, e):
    """Create new node and add it before the header(_start)."""
    if self.is_empty():   # if this is the first insert method call,
      print("As you do not have any start node yet, the given element will be a start node.")
      self._first_insert(e)
      return
    
    try:    # if there is more than one nodes,
      self._insert_between(e, self._start._prev, self._start)
    except:
      print("insertion unsuccessful...")
      return

  def insertAtEnd(self, e):
    """Create new node and add it at the end.
    This method task is same as insertBeforeHeader()
    The tail will be changed since we put the given element to the end"""
    self.insertBeforeHeader(e)

  def displayForward(self):
    """Display all nodes (forward) from the Circular list. Starting from the head to the end."""
    if self.is_empty():
      print("Nothing to print...")
      return
    
    walk = self._start._next      # starting from the head
    
    print(self._start._element)   # print the start element first
    while walk is not self._start:
      print(walk._element)
      walk = walk._next
    
  def displayBackward(self):
    """Display all nodes (backward) from the Circular list. Starting from the end to the head."""
    if self.is_empty():
      print("Nothing to print...")
      return
    
    walk = self._start._prev  # starting from the end
    
    while walk is not self._start:
      print(walk._element)
      walk = walk._prev
    print(self._start._element)   # print the start element at the last

if __name__ == '__main__':
  cirLink = CircularDoublyLinkedList()
  cirLink.insertBeforeHeader(1)
  cirLink.insertBeforeHeader(2)
  cirLink.insertBeforeHeader(3)
  cirLink.insertBeforeHeader(4)
  cirLink.insertBeforeHeader(5)
  
  print("This is forward display starting from the head.")
  cirLink.displayForward()
  print()
  print("This is backward display starting from next to the head.")
  cirLink.displayBackward()
  print()
  print()

  # ===== other sample by using user's input ===== #
  cirLink2 = CircularDoublyLinkedList()
  n = int(input("How many elements do you want to put inside the circular list? "))
  
  # randomly make n integers
  if n >= 1:
      for i in range(n):
          cirLink2.insertAtEnd(random.randint(1,20))
  
  print("This is forward display starting from the head.")
  cirLink2.displayForward()
  print()
  print("This is backward display starting from prev to the head.")
  cirLink2.displayBackward()
