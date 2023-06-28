# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:16:16 2023

"""

import numpy as np


def editDistance ( x, y ) :
    
    # Setting an empty matrix.
    
    D = [ ]
    D1 = [ ]
    
    # Range covers the offset row plus the length of the pattern
    
    for i in range ( len ( x ) + 1 ) :
        
        # Initializes the dimensions of the matrix with 0s. 
        
        D.append ( [ 0 ] * ( len ( y ) + 1 ) )
        
    D1 = D
    
    zeroMatrix = np.matrix ( D )

    zeroMatrix = zeroMatrix.view ( ) 
    
   # print ( '2d matrix with 0s: ' % zeroMatrix ) # for a clean view of the matrix
        
    # Initializes first row and column of the matrix
    
    for i in range ( len ( x ) + 1 ) :
        
        D [ i ] [ 0 ] = i
        
    for i in range ( len ( y ) + 1 ) :
        
        D [ 0 ] [ i ] = i
        
        
    # Fills in the rest of the matrix rows and columns.
    #
    # Starts at  row 1. 
    
    for i in range ( 1, len ( x ) + 1 ) : # goes by row
        
        
        for j in range ( 1, len ( y ) + 1 ) : # goes by column, starts at column 1
            
            distHor = D [ i ] [ j - 1 ] + 1 # value that is left adjacent to the current value, plus 1 is the penalty for character skipping
            
            distVer = D [ i - 1 ] [ j ] + 1 # value that is up adjacent to the current value, plus 1 is the penalty for character skipping
            
            if x [ i - 1 ] == y [ j - 1 ] : # edit distance does not further increase if there is a match
                
                distDiag = D [ i - 1 ] [ j - 1 ] # diagonal distance from current values to the above-left adjacent value. 
                
                # if matches, does not incur penalty
                
                
                
            else :
                
                distDiag = D [ i - 1 ] [ j - 1 ] + 1 # otherwise diagonal distance value increases by 1
                
                
                
            D [ i ] [ j ] = min ( distHor, distVer, distDiag ) # takes the minimum edit distance of the 3 possible values
        
    # Edit distance is the value in the bottom right corner of the matrix, D.
    
    return D, D1, zeroMatrix
    #return D [ -1 ] [ -1 ]
