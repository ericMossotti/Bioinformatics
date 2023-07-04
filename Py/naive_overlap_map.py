# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 10:57:52 2023

"""

from itertools import permutations

from Py.overlap import overlap


def naive_overlap_map ( reads, k ) :
    
    
    olaps = { }     # Initializing the dictionary. 
    
    
    for a, b in permutations ( reads, 2 ) :
        
        '''
        
        The number of consecutive characters from each pair of reads, a and b,
        that overlap. Minimum overlap length is specified. So we can go over 
        but not under that amount. The "2" means we are looking at 
        "pairs" of reads.
        
        '''
        
        # Calculates the overlap length with the overlap () function.
        
        olen = overlap ( a, b, min_length = k )
        
        '''
        
        If olen matches criteria for an overlap, then it assigns the key or
        overlapping strings 'a' and 'b' to the value of the overlap length, 
        olen.
        
        '''
        
        # a's length-k suffix, find all reads that have that suffix
    
        if olen > 0 :
            
            olaps [ ( a, b ) ] = olen
            
            '''
            
            Adds the tuple, ( a, b ), to the dictionary as a key. Then it 
            assigns to the tuple key a numerical value, olen.
            
            '''
            
    return olaps