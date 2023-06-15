def naive_with_counts ( p, t ) :
    
    occurrences = []
    
    aligns = 0
    
    chars = 0
        
    # Range is the length of the strand minus the length of the pattern, 
    # plus 1 to account for range starting at 0, but len starting at 1. 
    
    for i in range ( len ( t ) - len ( p ) + 1 ) :  # loop over alignments
        
        match = True
        
        aligns += 1
        
        for j in range ( len ( p ) ) :  # loop over characters
            
            chars += 1
            
            if t [ i + j ] != p [ j ] :  # compare characters
                
                match = False
                
                break
                
        if match:
            
            occurrences.append ( i )  # all chars matched; record
            
    return occurrences, aligns, chars