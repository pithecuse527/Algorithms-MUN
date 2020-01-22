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
    top_lst = returnTopTenList(lst)
    