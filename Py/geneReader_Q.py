# For reading FastQ files

# I am slightly modifying the geneReader function, mainly the 'if not line [ 0 ] . . . ' part

def geneReader_Q ( filename ) :
    
    
    with open ( filename, 'r' ) as f :
                    
        lines = f.readlines ()
        
    # only lines 2 and 3 will be read, skip everything else.
            
    desireds = lines [ 1 : : 4 ]   
    
    return desireds
            
