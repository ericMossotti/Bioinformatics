# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:16:16 2023

"""

def editDistance ( x, y ) :
    
    # Setting an empty set, of which, will be our matrix.
    
    D = [ ]
    
    # Range covers the offset row plus the length of the pattern
    
    for i in range ( len ( x ) + 1 ) :
        
        # Initializes the dimensions of the matrix with 
        # 0 values as placeholders. 
        
        D.append ( [ 0 ] * ( len ( y ) + 1 ) )
        
        
    # Initializes first row and column of the matrix
    
    for i in range ( len ( x ) + 1 ) :
        
        D [ i ] [ 0 ] = i
        
    # We will arbitrarily initialize the first row instead of column as 0's.
    # Could have set first column as 0 instead as it doesn't matter.
        
    for i in range ( len ( y ) + 1 ) :
        
        D [ 0 ] [ i ] = 0
        
        
    # Fills in the rest of the matrix rows and columns.
    #
    # Starts at  row 1. 
    
    for i in range ( 1, len ( x ) + 1 ) :
        
        # goes by column, starts at column 1
        
        for j in range ( 1, len ( y ) + 1 ) : 
        
        # value that is left adjacent to the current value, 
            # plus 1 is the penalty for character skipping
            
            distHor = D [ i ] [ j - 1 ] + 1 
            
            # value that is up adjacent to the current value, 
                # plus 1 is the penalty for character skipping
            
            distVer = D [ i - 1 ] [ j ] + 1
            
            # edit distance does not further increase if there is a match
            
                # basically, if matches, does not incur penalty
                
            if x [ i - 1 ] == y [ j - 1 ] : 
                
                # Diagonal up-left distance
                
                distDiag = D [ i - 1 ] [ j - 1 ] 
                
                
            # otherwise, diagonal distance value increases by 1
                
            else :
                
                distDiag = D [ i - 1 ] [ j - 1 ] + 1 
                
                
            """
            
            min () takes the minimum edit distance of the 3 possible values
            so this value will be inserted for the current iteration
            of row i, column j. 
            
            """

            D [ i ] [ j ] = min ( distHor, distVer, distDiag ) 
            
        
    # We are interested in the minimum value of the bottom row.
    
    return min ( D [ -1 ] )
