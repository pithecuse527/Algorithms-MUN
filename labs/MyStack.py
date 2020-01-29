##
##  MyStack.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 27/01/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Basic stack calss (Implementation from COMP2002 stack ADT)
##

#!/usr/bin/python

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) is 0 :
            return True

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
