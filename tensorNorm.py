def tensorNorm(x, T):
    '''
    norm = tensorNorm(x, T)
    
    Performs a dot product for non-orthogonal vector spaces.
    
    Inputs:
        -- x: the vector to have the norm computed.
            
        -- T: the tensor matrix of the vector space.

    Output:
        
        -- norm: the norm of the vector x.
    
    '''
    import numpy as np
    
    norm  = 0
    for i in range(len(x)):
        for j in range(len(x)): 
            norm = norm + x[i]*x[j]*T[i,j]
    
    norm  = np.sqrt(norm)
    
    return norm
