##
##  Postfix.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 08/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Calculating postfix notation
##  

#!/usr/bin/python

import array_stack

def calculatePostfix(formula):
    stk = array_stack.ArrayStack()
    
    p_notation = formula.split(" ")     # split elements by the space
    
    # walk through the formula and calculate
    # if the user did not input a postfix notation, raise
    for walker in p_notation:
        # if the walker meets operator, pop two element and push the calculation result
        
        if walker == '+':
            tmp = stk.pop()
            try:
                stk.push(stk.pop() + tmp)
            except:
                print("your formula seems not a postfix notation")
                return None
            
        elif walker == '-':
            tmp = stk.pop()
            try:
                stk.push(stk.pop() - tmp)
            except:
                print("your formula seems not a postfix notation")
                return None
            
        elif walker == '*':
            tmp = stk.pop()
            try:
                stk.push(stk.pop() * tmp)
            except:
                print("your formula seems not a postfix notation")
                return None
            
        elif walker == '/':
            tmp = stk.pop()
            if tmp == float(0):     # if the function tries divide by 0
                print("division by 0 is impossible")
                return None
                
            try:
                stk.push(stk.pop() / tmp)
            except:
                print("your formula seems not a postfix notation")
                return None
        
        elif walker.isnumeric():        # if number, push it
            stk.push(float(walker))
        
        # if the string contains except the operands and operators,
        else:
            print("wrong data!")
            return None
        
    return stk
            

if __name__ == "__main__":
    
    #todo1 : how to check whether this is postfix or not
    formula = input("Type only the postfix notation (please type space for distinguish) ")    # take the notation
    stk = calculatePostfix(formula)
    
    if stk:
        stk.disp()
    else:
        print("something's wrong...")
