##
##  MyTreeNode.py
##  labs-201948932
##  
##  Created by Hong Geun Ji on 12/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Basic node class for tree
##

class TreeNode():
    """The basic node class for the general tree"""
    def __init__(self, val=None, children=[], height=0):
        self._val = val
        self._children = children
        self._height = height

    def getChildren(self):
        return self._children

    def getVal(self):
        return self._val
        
    def setChildren(self, children):
        self._children = children
    
    def setHeight(self, height):
        self._height = height
    