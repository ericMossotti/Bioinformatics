def match ( s1, s2 ) :
    
    if not len(s1) == len(s2):
        
        return False
    
    for i in range(len(s1)):
        
        if not s1[i] == s2[i]:
            
            return False
        
    return True