# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:22:58 2023

@author: ecmos
"""

# Starting with an empty set object, we will then add every k-mer association to it

def kmerExtractor ( read, k ) :

    setObj = set ()

    for i in range ( 0, len ( read ) - k + 1 ) :

        # We use the add method because we are dealing with a set, 
        # not a list.

        setObj.add ( read [ i : i + k ] )
    
    return setObj