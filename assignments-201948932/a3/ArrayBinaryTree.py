class ArrayBinaryTree:
  """ Array based binary tree implementation, root starts 1
  """
  # ----some methods may help----
  def _parentIdex(self, j):
    return (j-1) // 2

  def _leftIdex(self, j):
    return 2*j
  
  def _rightIdex(self, j):
    return 2*j + 1

  # todo1:
    # are these methods are baed on complete binary tree??
  def _hasLeft(self, j):
    return self._leftIdex(j) <= self._size     # index beyond end of list?
  
  def _hasRight(self, j):
    return self._rightIdex(j) <= self._size    # index beyond end of list?

  def _childrenIdex(self,idx):
    return [self._leftIdex(idx),self._rightIdex(idx)]
    
  def __init__(self):
    self._data = [None] * 10
    self._size = 0                         # the number of nodes
    self._root = 1                         # root starts index 1
  
  def size(self):
    return self._size

  def isEmpty(self):
    return self._size == 0
  
  def root(self):
    return self._data[self._root]

  def parent(self,idx):
    """return parentNone if there is not parent (root)"""
    return None if idx == 1 else self._data[int(idx/2)]

  def children(self,idx):
    """ return a [left, right]"""
    return [self.left(idx),self.right(idx)]

  def left(self,idx):
    """ return the position that represents the left child of idx, or None if
    idx has no left child """
    if not self._hasLeft(idx):
      print("There is no left child...")
      return None
    
    return self._leftIdex(idx)

  def right(self,idx):
    """ return the position that represents the right child of idx, or None if
    idx has no right child """
    if not self._hasRight(idx):
      print("There is no right child...")
      return None
    
    return self._rightIdex(idx)

  def isInternal(self,idx):
    """ check whether the given idx node is internal or not """
    return self._hasLeft(idx) or self._hasRight(idx)

  def isExternal(self,idx):
    """ check whether the given idx node is external or not """
    return not (self._hasLeft(idx) or self._hasRight(idx))
  
  def setRoot(self,v):
    """ set the value of root """
    cur = self._root
    
    if self._data[cur] == None:   #if the root does not exist
      print("The root node does not exist")
      return None
    self._data[cur] = v
    return cur

  def setLeft(self,cur,v):
    """set the left node value."""
    #make sure to check whether the current, the child exist
    
    # if the given index's node is root or exist, and has left child,
    if (cur == self._root or self.parent(cur)) and self._hasLeft(cur):
      self._data[self._leftIdex(cur)] = v
    else:
      print("There is no left child node or the given index's node is not exist")

  def setRight(self,cur,v):
    """set the right node value."""
    #make sure to check whether the current, the child exist
    
    # if the given index's node is root or exist, and has right child,
    if (cur == self._root or self.parent(cur)) and self._hasRight(cur):
      self._data[self._rightIdex(cur)] = v
    else:
      print("There is no right child node or the given index's node is not exist")

  def insertRoot(self, v):
    if not self._data[self._root] == None:
      print("The root node already exists")
      return None
    self._data[self._root] = v
    self._size += 1
    return 1

  def insertLeft(self,cur,v):
    """recursively insert to the left node. Increase the array size if needed."""
    #make sure to check whether the current, the child exist; if the child exist, recursively go left
    #also check the array space, expand it if needed using _resize method
    
    if (cur == self._root or self.parent(cur)) and not self._hasLeft(cur):    # base case
        if self._leftIdex(cur) >= self._size:  self._resize(self._size * 2)    # if the list needs more size,
        self._data[self._leftIdex(cur)] = v
        self._size += 1
        
    self.insertLeft(self._leftIdex(cur), v)

  def insertRight(self,cur,v):
    """insert to the right node. Increase the array size if needed."""
    #make sure to check whether the current, the child exist; if the child exist, recursively go right
    #also check the array space, expand it if needed using _resize method
    
    if (cur == self._root or self.parent(cur)) and not self._hasRight(cur):    # base case
      if self._rightIdex(cur) >= self._size:  self._resize(self._size * 2)    # if the list needs more size,
      self._data[self._rightIdex(cur)] = v
      self._size += 1
          
    self.insertRight(self._rightIdex(cur), v)

  def inOrder(self):
    """Print an inorder iteration of nodes in the tree."""
    if not self.isEmpty():
      for p in self._subtree_inorder(self._root):
        print(p)
  
  def _subtree_inorder(self, p):
    """Generate an inorder iteration of nodes in subtree rooted at p."""
    if self._hasLeft(p):          # if left child exists, traverse its subtree
      for other in self._subtree_inorder(self._leftIdex(p)):
        yield other
    yield self._data[p]            # visit p between its subtrees
    if self._hasRight(p):         # if right child exists, traverse its subtree
      for other in self._subtree_inorder(self._rightIdex(p)):
        yield other

  def preOrder(self):
    """Print a preorder of nodes in the tree."""
    if not self.isEmpty():
      for p in self._subtree_preorder(self._root):  # start recursion
        print(p)

  def _subtree_preorder(self, p):
    """Generate a preorder iteration of positions in subtree rooted at p."""
    #your code goes here to replace "pass"

  def postOrder(self):
    """Print a postorder of nodes in the tree."""
    if not self.isEmpty():
      for p in self._subtree_postorder(self._root):  # start recursion
        print(p)

  def _subtree_postorder(self, p):
    """Generate a postorder iteration of node in subtree rooted at p."""
    #your code goes here to replace "pass"
  
  def printTreeArray(self):
    print(self._data)

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[k]              # intentionally shift indices

if __name__ == '__main__':
#testing code
  bt = ArrayBinaryTree()
  bt.insertRoot(1)
  bt.insertLeft(1,2)
  bt.insertRight(1,3)
  bt.insertLeft(1,4)
  bt.insertRight(2,5)
  bt.insertLeft(3,6)
  bt.insertRight(1,7)
  bt.printTreeArray()
  bt.inOrder()
  bt.postOrder()
  bt.preOrder()
  
