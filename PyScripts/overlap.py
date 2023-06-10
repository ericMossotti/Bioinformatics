# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:50:57 2023

"""

def overlap ( a, b, min_length = 3 ) :
    
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    
    start = 0  # start all the way at the left
    
    
    while True :
        
        # a.find() returns a positional starting value in string 'a' 
        # where string 'b' matches it. 
        
        start = a.find ( b [ : min_length ], start )  # look for b's prefix in a
        
        
        if start == -1 :  # no more occurrences to right
            
            return 0
        
        
        # found occurrence; check for full suffix/prefix match
        # startswith() returns a logical value, in this case, 
        # checks if beginning of string 'a' matches suffix of string 'b'
        
        
        if b.startswith ( a [ start : ] ) :
            
            return len ( a ) - start
        
        
        start += 1  # move just past previous match