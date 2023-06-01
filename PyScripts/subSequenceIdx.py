import bisect
   
class SubSeqIndex ( object ) :
    
    """ Holds a subsequence index for a text T """
    
    def __init__ ( self, t, k, ival ) :
        
        """ Create index from all subsequences consisting of k characters
            spaced ival positions apart.  E.g., SubseqIndex ( "ATAT", 2, 2 )
            extracts ( "AA", 0 ) and ( "TT", 1 ). """
                
        self.k = k  # num characters per subsequence extracted
        
        self.ival = ival  # interval spacing; 1=adjacent, 2=every other, etc
        
        self.index = []
        
        # 'span' function returns the beginning and ending index as a tuple. 
        #
        # By using '+', we are updating the tuple. 
        #
        # for k = 8, ival = 0, 
        # span = 1 + 0 
        # . . . = 1
        
        self.span = 1 + ival * ( k - 1 )
        
        for i in range ( len ( t ) - self.span + 1 ) :  # for each subseq
            
            # Returning an appended index. 
            # 
            # Performs slicing operation on the appended index of the text 't'.  
            #
            # Iterates over i. 
            #
            # '[ i : i + self.span . . .'  gives the range
            #
            # '. . . : ival ]' gives the interval
            
            self.index.append ( ( t [ i : i + self.span : ival ], i ) )  
            
            # Returning a sorted index. 
            
            # Alphabetize by subseq so that the binary search works correctly
            
        self.index.sort ()  
    
    def query ( self, p ) :
        
        """ Return index hits for first subseq of p """
        
        # query with first subseq
        
        subseq = p [ : self.span : self.ival ]  
        
        # 'Self.index' is a sorted index list, '(subseq, -1)' 
        #
        # is the element, the end character of subseq pattern. 
        
        i = bisect.bisect_left ( self.index, ( subseq, -1 ) )  # binary search
        
        hits = []
        
        
        while i < len ( self.index ) :  # collect matching index entries            
            
            if self.index [ i ] [ 0 ] != subseq :
                
                break
                
            hits.append ( self.index [ i ] [ 1 ] )
            
            i += 1
            
        return hits