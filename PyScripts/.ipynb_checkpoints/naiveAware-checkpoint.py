from reverseComplement import reverseComplement

def naiveAware ( p, t ) :
    
    occurrences = []
    
    rc_t = reverseComplement ( t )
    
    rc_p = reverseComplement ( p )
    
    # Range is the length of the strand minus the length of the pattern, 
    # plus 1 to account for range starting at 0, but len starting at 1. 
    
    for i in range ( len ( t ) - len ( p ) + 1 ) :  # loop over alignments
        
        match = True
        
        for j in range ( len ( p ) ) :  # loop over characters
            
            if t [ i + j ] != p [ j ] :  # compare characters
                
                match = False
                
                break
                
        # So now we test the reverse complement, 
        # thus making this function 'strand aware'. 
                
        if not match :
            
            match = True
            
            for j in range ( len ( p ) ) :
                
                # We do the same as above, 
                # but simply use the reverse complement of the pattern
                # to compare with the original strand.
                
                if t [ i + j ] != rc_p [ j ] :
                    
                    match = False
                    
                    break
                    
        if match:
            
            occurrences.append ( i )  # all chars matched; record
            
    return occurrences