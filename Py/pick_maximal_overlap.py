# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:18:41 2023

"""

from itertools import permutations
from Py.overlap import overlap


""""This is a helper function for the greedy_scs() function"""

def pick_maximal_overlap ( reads, k ) :
    
    """ Return a pair of reads from the list with a
        maximal suffix/prefix overlap >= k.  Returns
        overlap length 0 if there are no such overlaps."""
        
    reada, readb = None, None
    
    best_olen = 0
    
    for a, b in permutations ( reads, 2 ) :
        
        olen = overlap ( a, b, min_length = k )
        
        if olen > best_olen :
            
            reada, readb = a, b
            
            best_olen = olen
            
    return reada, readb, best_olen
