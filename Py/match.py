def match ( s1, s2 ) :
    
    # Filters out obviously mismatched strings if they aren't even the same
    # length to save time. 
    
    if not len ( s1 ) == len ( s2 ) :
        
        return False
    
    # Checks every character between strings of equal lengths.
    
    for i in range ( len ( s1 ) ) :
        
        if not s1 [ i ] == s2 [ i ] :
            
            return False
        
    return True
