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
    """LIFO Stack implementation using a Python list as underlying storage."""
    
    def __init__(self):
        """Create an empty stack"""
        self.data = []
