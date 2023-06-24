# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:57:52 2023

"""

from itertools import permutations

from Py.overlap import overlap


def naive_overlap_map ( reads, k ) :
    
    
    olaps = { }     # Initializing the set. 
    
    
    for a, b in permutations ( reads, 2 ) :
        
        '''
        
        The number of consequtive characters from a and b that overlap. 
        Minimum overlap length is specified. So we can go over but not under
        that amount.
        
        '''
        
        olen = overlap ( a, b, min_length = k )
        
        
        '''
        
        If olen matches criteria for an overlap, then it assigns the key or
        overlapping strings 'a' and 'b' to the value of the overlap length, 
        olen.
        
        '''
    
        if olen > 0 :
            
            olaps [ ( a, b ) ] = olen
            
            
    return olaps