##
##  FindNode.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 04/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Finding second-to-last node in a singly linked list
##

#!/usr/bin/python

class Node:
    """Lightweight, nonpublic class for storing a singly linked node"""
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
        
def find(head):
    tracer = head
    tracer_behind = None
    
    while(tracer.getNext()):
        tracer_behind = tracer
        tracer = tracer.getNext()
    
    return (tracer, tracer_behind)

if __name__ == "__main__":
