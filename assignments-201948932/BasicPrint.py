##
##  BasicPrint.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 08/01/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Basic short Python3 program
##  

import sys
import re


def doPrint(name, stuID):
    print("Hello World,")
    print("My name is " + name + " and my student ID is " + stuID + ".")


if __name__ == "__main__":
    name = "HONGGEUN JI"
    stuID = "201948932"
    l = len(sys.argv)

    if l in [2, 3] :     # if user input argv elements, and only provide two elements,
        if l is 2 :
            print("Type error! Please provide your name and student ID at the same time.")
            quit()     

        if not sys.argv[1].isalpha() or not sys.argv[2].isnumeric():
            print("Type error! Only letters a-z allowed for name and only numbers 0-9 allowed for student ID.")
            quit()
        
        name = sys.argv[1]
        stuID = sys.argv[2]
    
    elif len(sys.argv) != 1 :
        print("Please provide your name and student number corretly.")
        quit()
    
    doPrint(name, stuID)
    
