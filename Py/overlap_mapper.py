# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:04:47 2023

@author: ecmos
"""

"""

1. Build a dictionary of reads. 

   Split all your reads into blocks of k incrementing by a step
   of one along the read. 
   
2.  Run a loop of read 1 against a second loop of read 2.

    Make sure you put in an if statement so that
    read1 does not equal read2. 
    
3. If the condition is passed check that  the last 
   three letters of read1 are anywhere in the dict[read2], 
   that is, the set of k-splits of the read.
   
4. If one is found in the set, call the overlap function 
   on read1 and read 2, for k. 
   Store the olen in the olaps dict as before. 



"""

from itertools import permutations

from Py.overlap import overlap

from Py.kmerExtractor import kmerExtractor

from collections import defaultdict


def naive_overlap_map ( reads, k ) :
    
    
    kmerDict = defaultdict ( set )
    
    for read in reads :    
        
        kmerDict [ read ] = kmerExtractor ( read, k )
        
        

    
    # Initializing the dictionary. 
    
    olaps = { }

         
    
    
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
        
        # for a's length-k suffix, finds all reads with that suffix
    
        if olen > 0 :
            
            olaps [ ( a, b ) ] = olen
            
            '''
            
            Adds the tuple, ( a, b ), to the dictionary as a key. Then it 
            assigns to the tuple key a numerical value, olen.
            
            '''
            
    return olaps