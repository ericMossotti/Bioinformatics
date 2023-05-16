# For reading FastQ files

# I am slightly modifying the geneReader function, mainly the 'if not line [ 0 ] . . . ' part

def geneReader_Q ( filename ) :
    
    genome = ''
    
    with open ( filename, 'r' ) as f :
        
        # for line in f :
            
        lines = f.readlines ()
            
    desireds = lines [ 1::4 ]   
    
    return desireds
            
            
            
            
            # Ignoring the following common line symbols present in FastQ files. 
            
            # This ignores the lines starting with three particular symbols. 
            
            
            
            
            # if line [ 0 ] == 'A' or line [ 0 ] == 'C' or line [ 0 ] == 'G' or line [ 0 ] == 'T' or line [ 0 ] == 'N'  :
             #   
             #   
             #   genome += line.rstrip()
                
    #return genome
