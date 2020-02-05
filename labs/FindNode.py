##
##  FindNode.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 04/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Finding second-to-last node in a singly linked list
##

#!/usr/bin/python

import MyNode
        
def find(head):
    tracer = head
    tracer_behind = None
    
    while(tracer.getNext()):
        tracer_behind = tracer
        tracer = tracer.getNext()
    
    return (tracer_behind.getElement(), tracer.getElement())

if __name__ == "__main__":
    
    n1 = MyNode.Node(2)
    n2 = MyNode.Node(3)
    n3 = MyNode.Node(4)
    
    n1.setNext(n2)
    n2.setNext(n3)
    
    print(find(n1))
    