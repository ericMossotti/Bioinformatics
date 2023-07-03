# For reading FastQ formatted files

# I am slightly modifying the geneReader function, 
# mainly the 'if not line [ 0 ] . . . ' part

def geneReader_Q ( filename ) :
    
    # splitlines() with default args makes removing newlines simple and fast
    
    with open ( filename, "r" ) as f :
        
        data = f.read ().splitlines ()    
    
    # File is automatically closed after leaving the scope of "with . . ."
    
    """
    
    We want to skip 4 lines, starting at the 2nd line, "1". 
    
    We then skip 4 lines to get to the next line containing the desired 
    base sequence data.
    
    """
    
    # [ start : end : step ]        
    
    seqdata = data [ 1 :  : 4 ]
        
    return seqdata