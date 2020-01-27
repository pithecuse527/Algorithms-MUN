##
##  DuplicateStk.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 27/01/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Revise the given stack list that has same two adjacent value.
##  

#!/usr/bin/python

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
         
    def makeDoubleDouble(self):
        pass


if __name__ == "__main__":
    stk_lst = Stack()
    stk_lst.makeDoubleDouble()
    