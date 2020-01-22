##
##  ReverseArr.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 19/01/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Reversing Integers for given array
##  

def reverse(lst):
    n = len(lst)
    
    for i in range(n // 2):
        lst[i], lst[n-1-i] = lst[n-1-i], lst[i]

if __name__ == "__main__":
    lst = [1,2,3,4,5,6]
    reverse(lst)
    print(lst)
        
