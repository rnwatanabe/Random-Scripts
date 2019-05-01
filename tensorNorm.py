def tensorNorm(x, T = np.zeros((1))):
    '''
    norm = tensorNorm(x, T)
    
    Computes the Euclidean norm of a the vector x for non-orthogonal vector spaces.
    
    Inputs:
        -- x: the vector to have the norm computed.
            
        -- T: the metric tensor of the vector space.

    Output:
        
        -- norm: the norm of the vector x.
    
    '''
    import numpy as np
    
    if T.all() == 0:
        T = np.eye(len(x))
    
    norm  = 0
    for i in range(len(x)):
        for j in range(len(x)): 
            norm = norm + x[i]*x[j]*T[i,j]
    
    norm  = np.sqrt(norm)
    
    return norm
