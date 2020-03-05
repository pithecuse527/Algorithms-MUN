##
##  P-QueueBase.py
##  labs-201948932
##  
##  Created by Hong Geun Ji on 04/03/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Basic class for priority queue
##

import random

class PriorityQueueBase:
    """Abstract base calss for a priority queue"""
    
    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value', '_next'
        
        def __init__(self, k, v, n=None):
            self._key = k
            self._value = v
            self._next = n
        
        def __lt__(self, other):
            return self._key < other._key   # compare items based on their keys
    
        # getters
        def getKey(self):
            return self._key
        
        def getVal(self):
            return self._value
        
        def getNext(self):
            return self._next
        
        def setNext(self, n):
            self._next = n
    
    def __init__(self):
        """Create a head of Priority Queue"""
        self._head = None
        self._tail = None
        
    def isEmpty(self):                 # concrete method assuming abstract len
        """Return True if the priority queue is empty"""
        return self._head is None
    
    def printKeyVal(self):
        """Print all the keys and values from the P-Queue"""
        if self.isEmpty():
            print("priority queue is empty")
            return None
            
        walk = self._head
        
        while walk:
            print(str(walk.getKey())+" "+str(walk.getVal()))
            walk = walk.getNext()


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""
    
    def _findMin(self):         # nonpublic
        """Return the item with minimum key"""
        if self.isEmpty():
            print("priority queue is empty")
            return None
        
        small = self._head
        walk = small.getNext()
        
        while walk:
            if walk.getKey() < small.getKey():
                small = walk
            walk = walk.getNext()
        
        return small
        
    def add(self, k, v):
        """Add a key-value pair (unsorted order)"""
        if self.isEmpty():
            self._head = self._Item(k, v)
            self._tail = self._head
            return
        
        self._tail.setNext(self._Item(k, v))
        self._tail = self._tail.getNext()
    
    def min_(self):
        """Return but do not remove (k,v) tuple with minimun key"""
        item = self._findMin()
        return (item.getKey(), item.getVal())
    
    def removeMin(self):        # O(n)
        """Remove and return (k,v) tuple with minimun key"""
        if self.isEmpty():
            print("priority queue is empty")
            return None
        
        item = self._findMin()
        k = item._key
        v = item._value
        
        if not(self._head is self._tail):
            walk = self._head
            while True:
                if not walk.getNext() or walk.getNext() is item:
                    self._tail = walk
                    break
                # if walk is None or walk.getNext() is item:  break
                walk = walk.getNext()
            walk.setNext(item.getNext())
            
            item = None         # let the garbage collector do the work
        
        else:
            self._head = None
        
        return (k, v)


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""
        
    def add(self, k, v):        # O(n)
        """Add a key-value pair (unsorted order)"""
        if self.isEmpty():
            self._head = self._Item(k, v)
            self._tail = self._head
            return
        
        item = self._Item(k, v)
        
        walk = self._head
        while walk.getNext():
            if walk.getNext().getVal() >= item.getVal():    break
            walk = walk.getNext()
           
        item.setNext(walk.getNext())
        walk.setNext(item)
    
    def min_(self):
        """Return but do not remove (k,v) tuple with minimun key"""
        item = self._head
        k = item.getKey()
        v = item.getVal()
        
        return (k, v)
    
    def removeMin(self):
        """Remove and return (k,v) tuple with minimun key"""
        if self.isEmpty():
            print("priority queue is empty")
            return None
        
        item = self._head
        self._head = item.getNext()
        item.setNext(None)
        
        k = item.getKey()
        v = item.getVal()
        item = None         # let the garbage collector do the work
        
        return (k, v)
