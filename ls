'''
Perform the least squares

Inputs

  - p - matrix of regressors or features
  
  - y - vector of output
'''

import numpy as np
from numpy import random
from numpy import linalg

def ls(p,y):
    py = np.transpose(p).dot(y)
    covP = np.linalg.inv(np.transpose(p).dot(p))
    return covP.dot(py)
