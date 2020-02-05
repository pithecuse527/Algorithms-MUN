##
##  LinkedQueue.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 04/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Basic queue implementation by using linked list
##

#!/usr/bin/python

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage"""
    
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
        self._tail = None                   # reference to the tail node
        self._size = 0                      # reference of stack elements
        
    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0
        
    def first(self):
        """Return (but do not remove) the element at the front of the queue
        Raise Empty exception if the stack is empty"""
        try:
            f = self._head._element     # front aligned with head of list
        except:
            if self.is_empty():
                print("Queue is empty!")
            else:
                print("There is a problem with your queue...")
        else:
            return f

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO)
        Raise Empty exception if the stack is empty"""
        try:
            d = self._head._element
        except:
            if self.is_empty():
                print("Queue is empty!")
            else:
                print("There is a problem with your queue...")
        else:
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():         # special case as queue is empty
                self._tail = None
            return d
            
    def enqueue(self):
        """Add an element to the back of queue"""
        newest = self._Node(e, None)
        
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        