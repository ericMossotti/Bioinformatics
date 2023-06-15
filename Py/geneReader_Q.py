# For reading FastQ files

# I am slightly modifying the geneReader function, mainly the 'if not line [ 0 ] . . . ' part

def geneReader_Q ( filename ) :
    
    genome = ''
    
    with open ( filename, 'r' ) as f :
                    
        lines = f.readlines ()
            
    desireds = lines [ 1 : : 4 ]   
    
    return desireds
            
