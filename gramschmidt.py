def gramschmidt(U):
        '''
        W = gramschmidt(X)
        
        Returns orthogonalized vectors in each column of W by using the
        Gram-Schmidt method on the column vectors of the matrix X.
        
        Input:
        
                -- X: numpy array of floats with each column corresponding to a 
                vector.
        
        Output:
                -- W: numpy array of floats with each column corresponding to an 
                orthonalized vector.
        '''
        import numpy as np
        
        V = np.zeros_like(U)       
        
        
        n = U.shape[1]
              
        
        V = 1*U
        for m in range(n):
                for r in range(m):
                        V[:, [m]] = V[:, [m]] - (V[:, [r]].T@V[:, [m]])/(np.linalg.norm(V[:, [r]]))*V[:, [r]]        
                V[:,[m]] = V[:,[m]] / np.linalg.norm(V[:,m])
        return V
