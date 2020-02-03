##
##  Queue.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 03/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Basic queue calss (Implementation from COMP2002 stack ADT)
##

#!/usr/bin/python

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage"""
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        """Return the number of elements in the scope"""
        return self._size
        
    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue
        Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.__data[self._front]
        
        try:
            f = self.__data[self._front]
        except:
            if self.is_empty():
                print("Queue is empty!")
            else:
                print("There is a problem with your queue...")
        else:
            return f
    
            
    