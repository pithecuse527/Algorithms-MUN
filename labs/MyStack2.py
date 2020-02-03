##
##  MyStack2.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 03/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Basic stack calss (Implementation from COMP2002 stack ADT)
##

#!/usr/bin/python

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""
    
    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack"""
        self._data.append(e)        # new item stored at end of list
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty"""
        try:
            t = self._data[-1]
        except:
            print("Stack is empty!")
            # raise
        else:
            return t
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e. LIFO)
        Raise Empty exception if the stack is empty"""
        
        try:
            p = self._data.pop()
        except:
            print("Stack is empty!")
            # raise
        else:
            return p
