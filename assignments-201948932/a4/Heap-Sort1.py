##
##  Heap-Sort1.py
##  Assignment-201948932
##  
##  Created by Hong Geun Ji on 23/03/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Geun Ji. All rights reserved.
##
##  Heapifying the given unsorted array (Max heap)
##  

#!/usr/bin/python

def downHeap(arr, st_pnt):
    """ Downheap from the given key parameter
    arr := array needs to be heapify
    st_pnt := starting point for heapify (i.e. (n-1)//2 )
    """
    
    # base case
    if st_pnt < 0:      # if the given starting point for the downheap is lower then root point,
        return arr
    
    # downHeap for one subtree
    stop = False
    n = len(arr)                        # length of the array
    walker = st_pnt                     # walker for subtree
    while not stop:
        # running indices
        left_child = walker * 2 + 1         # left child var
        right_child = walker * 2 + 2        # right child var
        
        # These process will cover every cases (i.e. no child, only one child)
        if left_child >= n or not arr[left_child]:     # if the left child index is bigger than n and the value is not exist,
            left_child = walker         # stay starting point
            stop = True                 # stop going down
        if right_child >= n or not arr[right_child]:     # if the right child index is bigger than n and the value is not exist,
            right_child = walker        # stay starting point
            stop = True                 # stop going down
        
        # setting target to swap
        target = left_child
        if arr[left_child] < arr[right_child]:
            target = right_child
        
        # if they needs to be swapped, swap and walk down
        if arr[walker] < arr[target]:
            arr[walker], arr[target] = arr[target], arr[walker]
            walker = target    
        else:
            stop = True
    
    # move to next subtree
    downHeap(arr, st_pnt-1)
    
if __name__ == '__main__':
    tmp= [89,29,23,36,48,94,13,27,70,76,37,42,58]
    
    downHeap(tmp, 6)
    print(tmp)
