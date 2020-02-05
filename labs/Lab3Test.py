##
##  FindNode.py
##  labs-201948932
##  
##  Created by Hong Guen Ji on 04/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Codes for lab3 (MUN COMP 2002)
##

#!/usr/bin/python

import MyNode
        
        
def find(head):
    """Find two node
    One is the trail and the other one is the node behind the trail"""
    tracer = head
    tracer_behind = None
    
    while(tracer.getNext()):
        tracer_behind = tracer
        tracer = tracer.getNext()
    
    return (tracer_behind.getElement(), tracer.getElement())
    
    
def connectList(L, M):
    """Connect the linked list L and M"""
    tracer = L
    
    while(tracer.getNext()):
        tracer = tracer.getNext()
    
    tracer.setNext() = M
    
    return L
 
    
def countCircularLinkedList(head):
    """Count the number of nodes in a circularly linked list"""
    tracer = head
    count = 0
    
    while(tracer.getNext != head):
        tracer = tracer.getNext()
        count += 1
    
    return count


if __name__ == "__main__":
    
    n1 = MyNode.Node(2)
    n2 = MyNode.Node(3)
    n3 = MyNode.Node(4)
    
    n1.setNext(n2)
    n2.setNext(n3)
    
    print(find(n1))
    