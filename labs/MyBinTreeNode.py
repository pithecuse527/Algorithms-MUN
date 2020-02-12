##
##  MyBinTreeNode.py
##  labs-201948932
##  
##  Created by Hong Geun Ji on 12/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Basic node class for binary tree
##

class TreeNode():
    """The basic node class for the general tree"""
    def __init__(self, val=None, l_child=None, r_child=None):
        self._val = val
        self._l_child = l_child
        self._r_child = r_child

    def getLChild(self):
        return self._l_child
    
    def setLChild(self, l_child):
        self._l_child = l_child
        
    def getRChild(self):
        return self._r_child
    
    def setRChild(self, r_child):
        self._r_child = r_child

    def getVal(self):
        return self._val
