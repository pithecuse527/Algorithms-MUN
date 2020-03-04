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
