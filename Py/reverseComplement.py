def reverseComplement ( s ) :
    
    # Complete dictionary of all complementary base pairs relationships in DNA.
    
    complement = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N' }
    
    t = ''
    
    for base in s :
        
        t = complement [ base ] + t
        
    return t