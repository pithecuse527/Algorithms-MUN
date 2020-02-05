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
    One is the trail and the other one is the node behind the trail
    O(n)"""
    tracer = head
    tracer_behind = None
    
    while(tracer.getNext()):
        tracer_behind = tracer
        tracer = tracer.getNext()
    
    return (tracer_behind.getElement(), tracer.getElement())
    
    
def connectList(L, M):
    """Connect the linked list L and M
    Find the trailer of the linked list L and make the trailer connect to
    the head of the M"""
    tracer = L
    
    while(tracer.getNext()):
        tracer = tracer.getNext()
    tracer.setNext(M)
    
    return L
 
    
def countCircularLinkedList(head):
    """Count the number of nodes in a circularly linked list"""
    tracer = head
    count = 1
    
    while(tracer.getNext() != head):
        tracer = tracer.getNext()
        count += 1
    
    return count


def countByRecursive(tracer, count = 0):
    """Count the number of nodes in a given linked list
    using recursive algorithm"""
    if not tracer.getNext():
        count += 1
        return count
        
    count += 1
    return countByRecursive(tracer.getNext(), count)
    

def findMid(head, trail):
    """Find the middle node from the doubly-linked list
    This algorithm has O(n)"""
    tracer1 = head          # tracer1 will start from the head
    tracer2 = trail         # tracer2 will start from the trial
    
    while True:
        if tracer1.getRight() == tracer2:       # if the len(list) is even and tracer1, tracer2 reaches same middle position
            break
        elif tracer1 == tracer2:                # if the len(list) is odd and tracer1, tracer2 reaches same middle position
            break
        
        tracer1 = tracer1.getRight()
        tracer2 = tracer2.getLeft()
    
    return tracer1.getElement()
    
def isSame(x, y):
    """Define whether the circular linked list x and y are in same list or not"""
    tracer = x.getNext()
    
    while tracer != x:
        if tracer is y:
            return True
        
        tracer = tracer.getNext()
    
    return False


if __name__ == "__main__":
    
    # for i in range(4):
    #     exec("n"+str(i)+"=MyNode.DoublyNode("+str(i)+")")
    
    # exec("n0.setRight(n1)")
    
    # for i in range(1,3):
    #     exec("n"+str(i)+".setRight(n"+str(i+1)+")")
    #     exec("n"+str(i)+".setLeft(n"+str(i-1)+")")
    
    # exec("n3.setLeft(n2)")
    
    # exec("print(findMid(n0,n3))")
    
    for i in range(4):
        exec("n"+str(i)+"=MyNode.Node("+str(i)+")")
    exec("n3.setNext(n0)")
    
    for i in range(3):
        exec("n"+str(i)+".setNext(n"+str(i+1)+")")

    for i in range(4):
        exec("print(n"+str(i)+".getElement())")
        
    exec("print(n3.getNext().getElement())")
    
    n5 = MyNode.Node(7)
    
    exec("print(isSame(n1,n3))")
    exec("print(countCircularLinkedList(n0))")
    