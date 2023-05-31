def unawareNaive ( p, t ) :
    
    occurrences = []
        
    # Range is the length of the strand minus the length of the pattern, 
    # plus 1 to account for range starting at 0, but len starting at 1. 
    
    for i in range ( len ( t ) - len ( p ) + 1 ) :  # loop over alignments
        
        match = True
        
        for j in range ( len ( p ) ) :  # loop over characters
            
            if t [ i + j ] != p [ j ] :  # compare characters
                
                match = False
                
                break
                
        if match:
            
            occurrences.append ( i )  # all chars matched; record
            
    return occurrences