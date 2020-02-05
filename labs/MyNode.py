##
##  MyNode.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 03/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Basic node class with getter and setter
##

#!/usr/bin/python

class Node:
    """Lightweight, public class for storing a singly linked node"""
    __slots__ = '_element', '_next'     # streamline memory usage
    
    def __init__(self, element = None, next = None):  # initialize node's fields
        self._element = element         # reference to user's element
        self._next = next               # reference to next node
    
    def getNext(self):
        return self._next
    
    def setNext(self, next):
        self._next = next
    
    def getElement(self):
        return self._element
        
    def setElement(self, element):
        self._element = element


class DoublyNode:
    """Lightweight, public class for storing a doubly linked node"""
    __slots__ = '_element', '_left', '_right'     # streamline memory usage
    
    def __init__(self, element = None, left = None, right = None):  # initialize node's fields
        self._element = element         # reference to user's element
        self._left = left               # reference to left node
        self._right = right             # reference to right node
    
    def getLeft(self):
        return self._left
    
    def setLeft(self, left):
        self._left = left
    
    def getRight(self):
        return self._right
    
    def setRight(self, right):
        self._right = right
        
    def getElement(self):
        return self._element
        
    def setElement(self, element):
        self._element = element
