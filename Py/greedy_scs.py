# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 14:25:07 2023

"""

from Py.pick_maximal_overlap import pick_maximal_overlap


def greedy_scs ( reads, k ) :
    
    """ Greedy shortest-common-superstring merge.
        Repeat until no edges (overlaps of length >= k)
        remain. """
        
    read_a, read_b, olen = pick_maximal_overlap ( reads, k )
    
    
    while olen > 0 :
        
        reads . remove ( read_a )
        
        reads . remove ( read_b )
        
        
        # Found the two reads in our set with the best overlap
        # Replaced those reads with the overlap read.
        # We keep doing until there is only one read left, our scs.
        
        reads . append ( read_a + read_b [ olen : ] )
        
        read_a, read_b, olen = pick_maximal_overlap ( reads, k )
        
    # We concatenate the reads data without further overlaps to our scs.
    
    return '' . join ( reads )
