##
##  ReadHTML.py
##  Assignment-201948932
##  
##  Created by Hong Guen Ji on 08/02/20
##  VIM - Vi IMproved 8.0
##  Copyright © 2020 Hong Guen Ji. All rights reserved.
##
##  Reading HTML file (tag with attributes)
##  

#!/usr/bin/python

import urllib.request
import os
import array_stack

def is_matched_html(raw):
    """Definded in COMP 2002 materials
    """
    
    S = array_stack.ArrayStack()
    j = raw.find('<')                   # find first '<' character (if any)
    
    while j != -1:
        k = raw.find('>', j+1)          # find next '>' character from the first '<'
        
        if k == -1:
            return False                # invalid tag (since we cannot find any corresponding tag)
        tag = raw[j+1:k]                # strip away the tags < >
        
        
        # -------------------- this is the original version from the material -------------------- #
        # if not tag.startswith('/'):     # means it is opening tag
        #     S.push(tag)                 # what data gonna putted in? (reference of list or the string?)
        # else:                           # means it is closing tag
        #     if S.is_empty():            
        #         return False            # nothing to match with
        #     #if tag[1:] != S.pop():      
        #         return False            # mismatched delimiter
        # ---------------------------------------------------------------------------------------- #
        
        
        # -------------------- this is the modified version -------------------- #
        if tag.startswith('/'):         # if it is closing tag
            if S.is_empty():
                return False            # nothing to match with

            if tag[1:] != S.pop():
                return False            # mismatched delimiter
            
        else:                           # if it is not a closing tag (opening tag)
            tmp = tag.split(" ")        # split elements by the space (as the tag attributes usually distinguished by the space)
            tmp = tmp[0]                # and save the 0'th element which is the tag name only
            S.push(tmp)                 # push the tag name only (except attributes)
        # --------------------------------------------------------------------- #
        
        j = raw.find('<', k+1)          # find next '<' character (if any)
        
    return S.is_empty()                 # were all opening tags matched?


if __name__ == '__main__':

    fp = urllib.request.urlopen("file://" + os.getcwd() + "/htmlsample.html")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    
    print(is_matched_html(mystr))
