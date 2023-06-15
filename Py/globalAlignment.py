# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:13:56 2023
"""


def globalAlignment ( x, y ) :
    
    # Create distance matrix
    
    D = [ ]

    
    for i in range ( len ( x ) + 1 ) :
        
        D.append ( [ 0 ] * ( len ( y ) + 1 ) )

        
    # Initialize first column
    
    for i in range ( 1, len ( x ) + 1 ) :
        
        D [ i ] [ 0 ] = D [ i - 1 ] [ 0 ] + score [ alphabet.index ( x [ i - 1 ] ) ] [ -1 ]


    # Initialize first row
    
    for j in range ( 1,len ( y ) + 1 ) :
        
        D [ 0 ] [ j ] = D [ 0 ] [ j - 1 ] + score [ -1 ] [ alphabet.index ( y [ j - 1 ] ) ]

        
    # Fill rest of the matrix
    
    for i in range ( 1, len ( x ) + 1 ) :

        
        for j in range ( 1, len ( y ) + 1 ) :
            
            distHor = D [ i ] [ j - 1 ] + score [ -1 ] [ alphabet.index ( y [ j - 1 ] ) ]
            
            distVer = D [ i - 1 ] [ j ] + score [ alphabet.index ( x [ i - 1 ] ) ] [ -1 ]
            
            distDiag = D [ i - 1 ] [ j - 1 ] + score [ alphabet.index ( x [ i - 1 ] ) ] [ alphabet.index ( y [ j - 1 ] ) ]
            
            D [ i ] [ j ] = min ( distHor, distVer, distDiag )
    
    return D [ - 1 ] [ -1 ]  # return value in bottom right corner