##
##  TopTen.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 18/01/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Returning top ten integers from given list
##  

#!/usr/bin/python
import random

def bubbleSort(lst):
    # basic bubble sort
    # time complexity -> O(n^2)
    
    for i in range(len(lst) - 1):
        for j in range(1, len(lst) - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]


def returnTopTenList(lst):
    # find 10 largest integers from the list
    # sort first and take out the 10 integers from the list
    
    bubbleSort(lst)
    top_lst = lst[-10:]
    
    return top_lst
    

if __name__ == "__main__":
    lst = []
    n = int(input("how long do u want to make for the list? "))
    
    # randomly make n integers
    if n > 10:
        for i in range(n):
            lst.append(random.randint(1,100))
            
        print("This is the original random list -> " + str(lst))

        # after calling returnTopTenList(), the original list will be ordered
        top_lst = returnTopTenList(lst)
        print("This is the top list -> " + str(top_lst))
        
    else:
        print("list must be longer than 10")
