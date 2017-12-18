'''
Performs the least squares method

Inputs

  - p - matrix of regressors or features
  
  - y - vector of output
  
Outputs
  - beta - vector of the coefficients  
'''

import numpy as np


def ls(p,y):
    L = np.shape(p)[2]
    M = np.shape(p)[1]
    beta = np.empty((M,L))
    for i in range(L):
        py = np.transpose(p[:,:,i]).dot(y[:,i])
        covP = np.linalg.inv(np.transpose(p[:,:,i]).dot(p[:,:,i]))
        beta[:,i] =  covP.dot(py)
    return beta
