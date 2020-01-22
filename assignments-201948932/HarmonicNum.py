##
##  HarmonicNum.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 18/01/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Calculate harmonic number by recursive algorithms
##  

#!/usr/bin/python

def harmonic(n, i=1):
    
    # basis case (if index reaches the n)
    if i == n :
        return 1 / i
    
    # add them up
    return (1 / i) + harmonic(n ,i+1)
    

if __name__ == "__main__":
    n = int(input("num? "))
    
    harmonic_num = harmonic(n)
