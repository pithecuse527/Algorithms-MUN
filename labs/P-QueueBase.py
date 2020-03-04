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

class PriorityQueueBase:
    """Abstract base calss for a priority queue"""
    
    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def getKey(self):
            return self._key
        
        def getVal(self):
            return self._value
            
        def __lt__(self, other):
            return self._key < other._key   # compare items based on their keys
    
    def __init__(self):
        """Create a new empty Priority Queue"""
        self._data = []
        self.last_idx = -1
        
    def isEmpty(self):                 # concrete method assuming abstract len
        """Return True if the priority queue is empty"""
        return len(self._data) == 0
    
    def _rearrange(self, p):
        """Rearrange the elements in the data from p to last index and pop the last"""
        for p in range(self.last_idx - 1):     # O(n)
            self._data[p], self._data[p+1] = self._data[p+1], self._data[p]
        self._data.pop()


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""
        
    def _find_min_idx(self):        # nonpublic
        """Return Position of item with minimun key"""
        if self.isEmpty():
            print('Priority queue is empty')
            return None
            
        small = self._data[0]
        walk = 1
        
        while walk < self.last_idx:          # O(n)
            if self._data[walk] < self._data[small]:
                small = walk
        return small
    
    def add(self, key, value):
        """Add a key-value pair (unsorted order)"""
        self._data[self.last_idx] = self._Item(key, value)
        self.last_idx += 1
    
    def min_(self):
        """Return but do not remove (k,v) tuple with minimun key"""
        item = self._data[self._find_min_index()]
        return (item._key, item._value)
    
    def remove_min(self):
        """Remove and return (k,v) tuple with minimun key"""
        p = self._find_min_index()
        item = self._data[p]
        
        self._rearrange(p)
        self.last_idx -= 1
        
        return (item._key, item._value)
