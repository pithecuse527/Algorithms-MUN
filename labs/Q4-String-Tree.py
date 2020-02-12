##
##  Q4-String-Tree.py
##  labs-201948932
##  
##  Created by Hong Geun Ji on 12/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Questioin4 - Print and compute the value of string and height
##

#!/usr/bin/python

from MyTreeNode import TreeNode

def maxDepth(node, depth=0):
    
    depth_hold = depth
    node.setHeight(depth_hold)
    
    if len(node.getChildren()) == 0:        # if it is leaf
        return depth_hold

    # Compute the depth of each subtree 
    children_depth = []
    for i in node.getChildren():
        children_depth.append( maxDepth(i, depth_hold+1) )
    
    # Use the larger one
    # return max(children_depth)
    

def printValHeight(node):
    
    if node == None:
        return
    
    print(node.getHeight(), node.getVal())
    
    for i in node.getChildren():
        printValHeight(i)
    
if __name__ == "__main__":
    
    # ---------- setting the tree from l4 ---------- #
    n1 = TreeNode("Samuel")
    n2 = TreeNode("Charles")
    n3 = TreeNode("Chesley")
    n4 = TreeNode("Allan")
    n5 = TreeNode("Betty")
    n6 = TreeNode("Andrew")
    n7 = TreeNode("George")
    n8 = TreeNode("Hal")
    n9 = TreeNode("Linda")
    n10 = TreeNode("Paul")
    n11 = TreeNode("Keith")
    n12 = TreeNode("Susan")
    n13 = TreeNode("Robert")
    n14 = TreeNode("Marie")
    n15 = TreeNode("Peter")
    
    n1.setChildren([n2,n3,n4])
    n2.setChildren([n5,n6])
    n3.setChildren([n7,n8,n9])
    n5.setChildren([n10,n11,n12,n13])
    n8.setChildren([n14,n15])
    # ---------- setting the tree from l4 ---------- #
    maxDepth(n1)
    print(printValHeight(n1))
    