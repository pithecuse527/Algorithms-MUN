##
##  Q3-Num-of-Nodes.py
##  labs-201948932
##  
##  Created by Hong Geun Ji on 12/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Questioin2 - Counting the number of nodes in a general tree
##

#!/usr/bin/python

class TreeNode():
    """The basic node class for the general tree"""
    def __init__(self, val=None, l_child=None, r_child=None):
        self._val = val
        self._l_child = l_child
        self._r_child = r_child
        self._children = []

    def getChildren(self):
        return self._children

    def getVal(self):
        return self._val
        
    def setChildren(self, l_child, r_child):
        self._l_child = l_child
        self._r_child = r_child
        self._children = [l_child, r_child]


def numOfNodes(root, val=None, cnt=1):
    """Count all nodes from the given general tree (recursive algorithm)"""
    if not root:    # if the parameter is leaf's child (which is None)
        return 0
    
    if len(root.getChildren()) == 0:        # if it is leaf
        return 1
    
    for i in root.getChildren():
        cnt += numOfNodes(i, i.getVal(), cnt)
    
    return cnt


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    
    n1.setChildren(n2, n3)
    n2.setChildren(n4, n5)
    
    print(numOfNodes(n1, n1.getVal()))
