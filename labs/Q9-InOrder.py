##
##  Q9-InOrder.py
##  labs-201948932
##  
##  Created by Hong Geun Ji on 12/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  in-order traversal of a binary tree in linear time (non-recursive)
##

#!/usr/bin/python

from MyStack2 import ArrayStack
from MyBinTreeNode import TreeNode

def inOrder(node):
    
    stk = ArrayStack()
    current = node
    
    while True:
        if current:
            stk.push(current)
            current = current.getLChild()
        
        elif (not stk.is_empty()):
            current = stk.pop()
            print(current.getVal())
            current = current.getRChild()
        
        else:
            break


if __name__ == "__main__":
    
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    
    n1.setLChild(n2)
    n1.setRChild(n3)
    n2.setLChild(n4)
    n2.setRChild(n5)
    n5.setLChild(n6)
    n5.setRChild(n7)
    
    inOrder(n1)
    