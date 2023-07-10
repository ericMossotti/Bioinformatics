# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 13:58:01 2023

"""

import itertools

from Py.overlap import overlap

def scs ( ss ) :
    
    """ Returns shortest common superstring of given strings,
        assuming no string is a strict substring of another """
        
    shortest_sup = None
    
    for ssperm in itertools.permutations ( ss ) :
        
        sup = ssperm [ 0 ]
        
        for i in range ( len ( ss ) - 1 ) :
            
            olen = overlap ( ssperm [ i ], ssperm [ i + 1 ], min_length = 1 )
            
            sup += ssperm [ i + 1 ] [ olen : ]
            
        if shortest_sup is None or len ( sup ) < len ( shortest_sup ) :
            
            shortest_sup = sup
            
    return shortest_sup