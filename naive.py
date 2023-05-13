from reverseComplement import reverseComplement

def naive ( p, t ) :
    
    occurrences = []
    
    rc_t = reverseComplement ( t )
    
    rc_p = reverseComplement ( p )
    
    for i in range ( len ( t ) - len ( p ) + 1 ) :  # loop over alignments
        
        match = True
        
        for j in range ( len ( p ) ) :  # loop over characters
            
            if t [ i + j ] != p [ j ] and rc_t [ i + j ] != p :  # compare characters
                
                match = False
                
                break
                
        if match:
            
            occurrences.append ( i )  # all chars matched; record
            
    return occurrences