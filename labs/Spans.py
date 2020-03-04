##
##  Spans.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 29/01/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Implement the algorithm spans2 from COMP2002 materials
##  

#!/usr/bin/python

import random
import MyStack

def spans(data_lst):
    # spans2 algorithms implementation
    
    A = MyStack.Stack()     # new empty tmp stack
    S = [None] * 20                  # new array of n integers
    # n = len(A.items)
    
    for i in range(len(data_lst)):
        n = len(A.items)            # needs to be keep tracked
        while n and (data_lst[A.peek()] <= data_lst[i]):
            A.pop()
            n = len(A.items)            # needs to be keep tracked
        
        if A.isEmpty():
            S[i] = i + 1
        else:
            S[i] = i - A.peek()
        
        A.push(i)

    return S

if __name__ == "__main__":
    
    data_lst = [6,3,4,7,5,1,10]
    #data_lst 
    #data_lst.items = [6,3,4,2,5,1,10]       # just for the test
    
    #spans(data_lst)
    print(spans(data_lst))
    