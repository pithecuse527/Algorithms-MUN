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

import random

def makeDoubleDouble(stk_lst):
    # make stack list has two duplicate adjacent elements
    
    tmp_stk_lst = Stack()
    
    while not stk_lst.isEmpty():
        tmp_stk_lst.push(stk_lst.pop())
    
    while not tmp_stk_lst.isEmpty():
        stk_lst.push(tmp_stk_lst.peek())
        stk_lst.push(tmp_stk_lst.pop())
        

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


if __name__ == "__main__":
    stk_lst = Stack()
    
    for i in range(10):
        stk_lst.push(random.randint(1,50))
    
    print(stk_lst.items)
    makeDoubleDouble(stk_lst)
    print(stk_lst.items)
