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

from MyTreeNode import TreeNode

def numOfNodes(root, val):
    """Count all nodes from the given general tree (recursive algorithm)"""
    cnt_hold = 1     # count for itself and it's child (start from counting itself)
    
    if not root:    # if the parameter is leaf's child (which is None)
        return 0
    
    if len(root.getChildren()) == 0:        # if it is leaf
        return 1
    
    for i in root.getChildren():
        cnt_hold += numOfNodes(i, i.getVal())
    
    return cnt_hold


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    
    n1.setChildren([n2, n3])
    n2.setChildren([n4, n5])
    n5.setChildren([n6, n7])
    
    print(numOfNodes(n1, n1.getVal()))
