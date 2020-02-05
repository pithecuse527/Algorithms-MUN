##
##  LinkedStack.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 04/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Basic stack implementation by using linked list
##

#!/usr/bin/python

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""
    
    #-------------------- nested _Node class -------------------- #
    
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node"""
        __slots__ = '_element', '_next'     # streamline memory usage
        
        def __init__(self, element, next):  # initialize node's fields
            self._element = element         # reference to user's element
            self._next = next               # reference to next node
            
    #-------------------- nested _Node class -------------------- #
    
    def __init__(self):
        """Create an empty stack."""
        self._head = None                   # reference to the head node
        self._size = 0                      # reference of stack elements
        
    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack
        Raise Empty exception if the stack is empty"""
        try:
            t = self._head._element
        except:
            if self.is_empty():
                print("Stack is empty!")
            else:
                print("There is a problem with your stack...")
        else:
            return t
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e. LIFO)
        Raise Empty exception if the stack is empty"""
        try:
            p = self._head._element
        except:
            if self.is_empty():
                print("Stack is empty!")
            else:
                print("There is a problem with your stack...")
        else:
            self._head = self._head._next
            self._size -= 1
            return p
