from PyScripts.kmer_index import Index

def approximate_match_idx ( p, t, n ) : # approximate match functin but with indexing
    
    # For n = 2, p = pattern of length 24
    #
    # Segment length is len ( p ): = 24, divided by ( n + 1 ): 2 + 1 = 3. 
    #
    # segment_length = int ( 24 / 3 ) = 8
    
    segment_length = int ( len ( p ) / ( n + 1 ) )
    
    # Creates an unordered list or set object.
    
    all_matches = set ( )
    
    p_idx = Index ( t, segment_length ) # pattern indexing of the file by x-mers
    
    idx_hits = 0 # index hits
    
    # The range from 0 to number of errors allowed + 1 to account for len starting at 1 instead of 0, like range.
    
    for i in range ( n + 1 ) :
        
        # 'start' is the iterator value times the segment length, so we iterate by 8, aka, 8-mers in this context.
        #
        # i = 0, then start = 0 * 8 = 0
        #
        # i = 1, start = 1 * 8 = 8
        #
        # start = 16 
        #
        # ... = 24
        #
        # ...
    
        start = i * segment_length
        
        # 'end' is the smallest returnable value, which is the length of the pattern 'p'.
        ##
        # i = 0, then i + 1 * segment_length
        #
        # 0 + 1 = 1 + 24 = 25, 
        #
        # but the lowest value is the 'key' in the min () function, which is 24
        #
        # so end = 24 where i = 0. 
        ##
        # for i = 1, 
        #
        # end = minimum of ( 2 * 24, > 24 ) 
        #
        # end = 48, so the 'key' rule for lowest acceptable value is not required from i = 1 and on. 
        ##
        # for i = 2,
        #
        # end = min ( 3 * 24 ) = 72
        #
        # end = 72
        
 
        end = min ( ( i + 1 ) * segment_length, len ( p ) ) 
        
        # 'matches' processes our pattern, likewise, by 8, so will start at the length 0 and 
        #
        # So we are going in chunks of 24, which is the length of the pattern.
        #
        # 'end' begins at 24 while 'start' begins at 0. 
        
        matches = p_idx.query ( p [ start : end ] )
                            
        idx_hits += len ( matches )

        for m in matches : 
                   
            if m < start or m - start + len ( p ) > len ( t ) :
                
                continue
                
            mismatches = 0
            
            for j in range ( 0, start ) :
                
                if not p [ j ] == t [ m - start + j ] :
                    
                    mismatches += 1
                    
                    if mismatches >= n :
                        
                        break
                        
            for j in range ( end, len ( p ) ) :
            
                if not p [ j ] == t [ m - start + j ] :
                    
                    mismatches += 1
                    
                    if mismatches > n :
                        
                        break
                        
            if mismatches <= n :
                
                all_matches.add ( m - start ) 
                
    return idx_hits