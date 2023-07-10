# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:22:58 2023

@author: ecmos
"""
from collections import defaultdict

# Starting with an empty set object, we will then add every k-mer association to it

def kmerExtractor ( read, k ) :

    kmerDict = defaultdict ( set )

    """ 
    k mer = 30 
    len read = 100
    
    100 - 30 + 1 = 71 
    
    range of 1 : 71 
    
    """
    # len ( read ) - k + 1

    for i in range ( 0, len ( read ) - k + 1 ) :
    
        # We use the add method because we are dealing with a set, 
        # not a list.
        
        """
        for every l
        
        """
    
        kmerDict[i].add ( read [ i : i + k ] )
    
    
    return kmerDict