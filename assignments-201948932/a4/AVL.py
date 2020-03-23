#!/usr/bin/python3

class AVL:
  """Binary search tree based on 'BTNode's."""
  __slots__ = 'root'

  #-------------------------- nested BTNode class --------------------------
  class _BTNode:
    """ Lightweight, nonpublic class for storing a BTNode. """
    __slots__ = 'element', 'left', 'right', 'parent', 'height'

    def __init__(self, element, left = None, right = None, parent = None):
      self.element = element
      self.left    = left
      self.right   = right
      self.parent  = parent
      self.height  = -1

    def hasLeft(self):
      """ Returns whether this node has a left child. """
      return self.left != None

    def hasRight(self):
      """ Returns whether this node has a right child. """
      return self.right != None
      
    def left_height(self):
      """ Returns the height of left subtree. """
      return self.left.height if self.left is not None else -1

    def right_height(self):
      """ Returns the height of right subtree. """
      return self.right.height if self.right is not None else -1
      
    def __lt__(self, other):
      """ Return True if other is a BTNode and this node is less than other. """
      return type(other) is type(self) and self.element < other.element

    def __gt__(self, other):
      """ Return True if other is a BTNode and this node is greater than other. """
      return type(other) is type(self) and self.element > other.element

    def __eq__(self, other):
      """ Return True if other is a BTNode and this node is equal to the other. """
      return type(other) is type(self) and self.element == other.element

  #-- c'tor
  def __init__(self):
    self.root = None


  #-- Public methods
  def insert(self, element):
    """ Insert element into the AVL, keeping the AVL property. """
    def _insertNode(root, node):
      if root == None or root == node:    # Overwrite if already present
        root = node
      else:
        if node < root:  # Go left
          if root.hasLeft():
            _insertNode(root.left, node)
          else:
            root.left = node
            node.parent = root
        else:            # Go right
          if root.hasRight():
            _insertNode(root.right, node)
          else:
            root.right = node
            node.parent = root

    # Create node to insert
    node = self._BTNode(element)

    if self.root == None:   # Special case for when tree is empty
      self.root = node
    else:
      _insertNode(self.root, node)
      self._rebalance(node)# This method should be implemented by you
      
  def _subtree_last_position(self, p):
    """Return Node of last item in subtree rooted at p."""
    walk = p
    while walk.right is not None:                # keepwalking right
      walk = walk.right
    return walk

  def _replace(self, node, e):
    """Replace the element at node p with e, and return old element."""
    old = node.element
    node.element = e
    return old
    
  def _delete(self, node):
    """Delete node and keep AVL."""
    child = node.left if node.left else node.right  # might be None
    if child is not None:
      child.parent = node.parent   # child's grandparent becomes parent
    if node is self.root:
      self.root = child             # child becomes root
    else:
      parent = node.parent
      if node is parent.left:
        parent.left = child
      else:
        parent.right = child
    node.parent = node              # convention for deprecated node
    return node.element

  def delete(self, p):
    """Remove the item at given Node."""
    if p is None:
      return None
    replacement = p
    if p.left and p.right:           # p has two children
      replacement = self._subtree_last_position(p.left)
      self._replace(p, replacement.element)
      p =  replacement
      # now p has at most one child
    parent = p.parent
    self._delete(p)
    self._rebalance(parent)               # This method should be implemented by you
        
      
  def _subtree_search(self, p, k):
    """Return Note of p's subtree having key k, or last node searched."""
    
    if k == p.element:                                   # found match
      return p
    elif k < p.element:                                  # search left subtree
      if p.left is not None:
        return self._subtree_search(p.left, k)
      else:
        return None
    else:                                              # search right subtree
      if p.right is not None:
        return self._subtree_search(p.right, k)
      else:
        return None
    
  
  def search(self,element):
    """Return position with key k, or else neighbor (or None if empty)."""
    if self.root==None:
      return None
    else:
      p = self._subtree_search(self.root, element)
      return p

  def print(self):
    """ Print tree (node and weight) using inorder traversal. """
    def _print_inOrder(root):
      if root != None:
        _print_inOrder(root.left)
        print([root.element,root.height], end=' ')
        _print_inOrder(root.right)
        
    def _print_preOrder(root):
      if root != None:
        print([root.element,root.height], end=' ')
        _print_preOrder(root.left)
        _print_preOrder(root.right)

    print("In-order: ");
    _print_inOrder(self.root)
    print();
    print("Pre-order: ");
    _print_preOrder(self.root)
    print();
    
#-------implement _rebalance methods. You may look at the code from the textbook for clarification, but you must modify to adapt to this code. ----
  def _rebalance(self, p):
    pass #this is just for place holder, it should be replaced by your own code
    

#-- Main method
tree = AVL()
tree.insert(50)
tree.insert(60)
tree.insert(70)
tree.print()
tree.insert(55)
tree.insert(52)
tree.print()
print(tree.root.element)
#tree.delete(tree.search(55))
tree.delete(tree.search(70))
tree.print()


