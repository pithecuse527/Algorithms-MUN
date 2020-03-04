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
            
        def __lt__(self, other):
            return self._key < other._key   # compare items based on their keys
    
    def __init__(self):
        """Create a new empty Priority Queue"""
        self._data = []
        self._data_len = 0
        
    def is_empty(self):                 # concrete method assuming abstract len
        """Return True if the priority queue is empty"""
        return len(self._data) == 0
    
    def _rearrange(self, p):
        """Rearrange the elements in the data"""
        for p in range(self._data_len - 1):     # O(n)
            self._data[p], self._data[p+1] = self._data[p+1], self._data[p]

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""
        
    def _find_min_index(self):        # nonpublic
        """Return Position of item with minimun key"""
        if self.is_empty():
            print('Priority queue is empty')
            return None
            
        small = self._data[0]
        walk = 1
        
        while walk < self._data_len:          # O(n)
            if self._data[walk] < self._data[small]:
                small = walk
        return small
    
    def add(self, key, value):
        """Add a key-value pair (unsorted order)"""
        self._data[self._data_len] = self._Item(key, value)
        self._data_len += 1
    
    def min_(self):
        """Return but do not remove (k,v) tuple with minimun key"""
        item = self._data[self._find_min_index()]
        return (item._key, item._value)
    
    def remove_min(self):
        """Remove and return (k,v) tuple with minimun key"""
        p = self._find_min_index()
        item = self._data[p]
        
        self._rearrange(p)
        self._data_len -= 1
        
        return (item._key, item._value)
