'''
Performs the logistic regression of the regressors in matrix p, given the class vector y.
Inputs
  - p - matrix of regressors or features
  
  - y - vector of classes
  
  - num_iterations - int with the number of iterations performed. Defaults to 10000.
  
  - learning_rate - float with the rate of feature coefficients update. Defaults to 0.001.
  
Outputs
  - beta - vector of the coefficients  
'''

def logreg(p,y, num_iteration = 10000, learning_rate = 0.001):
    if p.ndim == 2:
        p = p.reshape(p.shape[0],p.shape[1],1)
        y = y.reshape(y.shape[0], 1)
    beta = np.zeros((p.shape[1],p.shape[2]))
    m = p.shape[0]
    for j in range(p.shape[2]):       
        for i in range(num_iteration):
            z = p[:,:,j].dot(beta[:,j])
            A = 1/(1 + np.exp(-z))
            dJdbeta = 1.0/m*p[:,:,j].T.dot(A-y[:,j])
            beta[:,j] = beta[:,j] - learning_rate * dJdbeta
    return beta
