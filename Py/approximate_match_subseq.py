from Py.subSequenceIdx import SubSeqIndex

def approximate_match_subseq ( p, t, n, ival ) :
    

    # For n = 2, p = pattern of length 24
    #
    # Segment length is len ( p ): = 24, divided by ( n + 1 ): 2 + 1 = 3. 
    #
    # segment_length = int ( 24 / 3 ) = 8

    segment_length = int ( len ( p ) / ( n + 1 ) )

    # Creates an unordered list or set object.

    all_matches = set ( )

    # pattern indexing of the file by x-mers
    
    p_subs = SubSeqIndex ( t, segment_length, ival ) 

    sub_hits = 0 # subseq hits

    # The range from 0 to number of errors allowed + 1 to account for len
    #
    # starting at 1 instead of 0, like range.

    for i in range ( n + 1 ) :

        # 'start' is the iterator value times the segment length, so we iterate
        #
        # by 8, aka, 8-mers in this context.
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
        
        start = i

        matches = p_subs.query ( p [ start : ] )
         
        for m in matches : 
            
            sub_hits += 1

            if m < start or m - start + len ( p ) > len ( t ) :

                continue

            mismatches = 0
            
            for j in range ( 0, len ( p ) ) :

                if not p [ j ] == t [ m - start + j ] :

                    mismatches += 1

                    if mismatches >= n :

                        break

            if mismatches <= n :

                all_matches.add ( m - start ) 

    return list ( all_matches ), sub_hits

