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
        self._size = 0      # the actual size of the queue
        self._front = 0     # the front of the queue
    
    def __len__(self):
        """Return the number of elements in the scope"""
        return self._size
        
    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue
        Raise Empty exception if the queue is empty"""
        try:
            f = self._data[self._front]
        except:
            if self.is_empty():
                print("Queue is empty!")
            else:
                print("There is a problem with your queue...")
        else:
            return f
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO)
        Raise Empty exception if the queue is empty"""
        try:
            d = self._data[self._front]
        except:
            if self.is_empty():
                print("Queue is empty!")
            else:
                print("There is a problem with your queue...")
        else:
            self._data[self._front] = None
            self._front = (self._front + 1) % ArrayQueue.DEFAULT_CAPACITY
            self._size -= 1
            return d
            
    def enqueue(self, e):
        """Add an element to the back of queue"""
        try:
            self._data[self._front + self._size] = e            # try the normal enqueue process
        except IndexError:
            if self._size == len(self._data):                   # if the queue needs more space, double it
                self._resize(2 * ArrayQueue.DEFAULT_CAPACITY)
            self._data[(self._front + self._size) % len(self._data)] = e    # try the circular queue enqueue process
                                                                            # this will implement anyway whether the queue is expanded or not
        except:
            raise("There is a problem with your queue...")
        self._size += 1
            
    def _resize(self, cap):                 # assume cap >= len(self)
        """Resize to a new list of capacity >- len(self)
        And realign the elements to a new list"""
        old = self._data                    # keep track of existing list
        self._data = [None] * cap           # allocate list with new capacity
        walk = self._front

        for k in range(self._size):         # only consider existing elements
            self._data[k] = old[walk]       # intentionally shift indices
            walk = (1 + walk) % len(old)    # use old size as modulus
        self._front = 0                     # front has been realigned
        