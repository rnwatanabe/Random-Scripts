def corrMatrix(x, normalize = True):
    '''
    corrMatrix(x, normalize = True)
    
    Create a correlation matrix C = (x-\mu(x))(x-\mu(x))^T
    
    Inputs:
        
        -- x: The numpy array with the signals that will form the
        correlation matrix. Each line of the array is a signal and each column
        is a sample of the signal.
        
        -- normalize: boolean to indicate if a normalization of each signal must
        be performed. The normalization is by the Euclidean norm of each of the
        signals. The default is true. 
        
    Output:
        
        -- corr: numpy array with the correlation matrix.
    '''
    
    x = x - np.mean(x, axis = 1, keepdims = True)
    
    if normalize:        
        xDirections = x/np.linalg.norm(x, axis=1, keepdims=True)
    else:
        xDirections = 1*x
        
    corr = xDirections@xDirections.T
    
    return corr
