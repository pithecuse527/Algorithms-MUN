##
##  HeapInsertion.py
##  labs-201948932
##  
##  Created by Hong Geun Ji on 04/03/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Heap Insertion basis on max-heap array
##

class HeapBase:
    """Abstract base calss for a heap"""
    
    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
            
        def __lt__(self, other):
            return self._key < other._key   # compare items based on their keys
    
    def __init__(self):
        """Create a new empty heap list"""
        self._data = []
        self._data_last = -1
        
    def _getParentIdx(self, i):
        """Calculate and return the position of the parent node"""
        if i == 0:      # if root,
            return i
        return (i-1)//2
    
    def _getLchildIdx(self, i):
        """Calculate and return the poition of the left childe node"""
        return 2 * i + 1
    
    def _getRchildIdx(self, i):
        """Calculate and return the poition of the right childe node"""
        return 2 * i + 2
    
    def add(self, k, v):
        """Add new node and arrange the three to make max-heap"""
        new_node = self._Item(k, v)
        self._data.append(new_node)
        self._data_last += 1
        curr = self._data_last
        
        if self._data_last != 0:
            par_pos = self._getParentIdx(self._data_last)
            
            while self._data[curr]._key > self._data[par_pos]._key:         # O(logn)
                # upHeap
                self._data[par_pos], self._data[curr] = self._data[curr],self._data[par_pos]
                curr = par_pos
                par_pos = self._getParentIdx(curr)
                
    def remove(self):
        """Remove the last node and arrange the tree to make max-heap"""
        
        # todo1: compare childrens' key first? --> yes
        tmp_to_return = self._data[0]
        self._data[0], self._data[self._data_last] = self._data[self._data_last], self._data[0]
        self._data_last -= 1
        
        curr = 0
        pos = 0
        while True:
            print("!"+str(curr)+"!")
            if curr >= self._data_last:
                break
            
            if self._data[self._getLchildIdx(curr)]._key >= self._data[self._getRchildIdx(curr)]._key:
                pos =  self._getLchildIdx(curr)
            else:
                pos = self._getRchildIdx(curr)
            
            if self._data[curr]._key < self._data[pos]._key:
                self._data[curr], self._data[pos] = self._data[pos], self._data[curr]
            
            curr = pos
            
        self._data.pop()
        return tmp_to_return

if __name__ == "__main__":
    lst_1 = [81, 76, 43, 63, 55, 39, 41, 7, 58, 25, 32, 9, 22, 37, 11]
    
    tmp_heap = HeapBase()
    
    for i in range(len(lst_1)):
        tmp_heap.add(lst_1[i],0)
        
    for i in range(tmp_heap._data_last):  
        print(tmp_heap._data[i]._key)
    
    tmp_heap.remove()
    for i in range(tmp_heap._data_last):  
        print(tmp_heap._data[i]._key)
    tmp_heap.remove()
    for i in range(tmp_heap._data_last):  
        print(tmp_heap._data[i]._key)
    tmp_heap.remove()
    for i in range(tmp_heap._data_last):  
        print(tmp_heap._data[i]._key)
        