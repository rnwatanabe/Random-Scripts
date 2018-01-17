'''
Performs the regression of an artificial neural network of 2 layers and one output having the matrix of features p, given the class vector y. It uses the function tanh as the activation function of the first layer and a sigmoid at the second layer (output layer).

Inputs
  - p - matrix of regressors or features
  
  - y - vector of classes
  
  - n_nodes - int with the number of nodes of the first layer of the network. Defaults to 4.
  
  - num_iterations - int with the number of iterations performed. Defaults to 10000.
  
  - learning_rate - float with the rate of feature coefficients update. Defaults to 0.001.
  
Outputs
  - beta1 - matrix of the coefficients of the first layer
  
  - beta2 - vector of the coefficients of the output layer
  
  - b - float of the constant of the output layer.
'''

def NN2layer(p, y, n_nodes = 4, num_iterations = 10000, learning_rate = 0.001):
    if p.ndim == 2:
        p = p.reshape(p.shape[0],p.shape[1],1)
        y = y.reshape(y.shape[0], 1)    
    beta1 = np.random.randn(p.shape[1],n_nodes,p.shape[2])*0.001
    beta2 = np.random.randn(n_nodes, 1, p.shape[2])*0.001
    b = np.random.randn(1, p.shape[2])*0.001
    m = p.shape[0]
    for j in range(y.shape[1]):
        yj = y[:,j].reshape(m,1)
        for i in range(num_iterations):
            z1 = p[:,:,j].dot(beta1[:,:,j])
            a1 = np.tanh(z1)
            z2 = a1.dot(beta2[:,:,j]) + b[:,j]
            a2 = 1/(1+np.exp(-z2))
            dJdbeta2 = 1/m * (a1.T).dot(a2-yj)
            dJdbeta1 = 1/m * (p[:,:,j].T).dot(np.multiply((a2-yj).dot(beta2[:,:,j].T),1-a1**2))
            dJdb = np.mean(np.multiply((a2-yj).dot(beta2[:,:,j].T),1-a1**2))
            beta1[:,:,j] = beta1[:,:,j] - learning_rate * dJdbeta1
            beta2[:,:,j] = beta2[:,:,j] - learning_rate * dJdbeta2
            b[:,j] = b[:,j] - learning_rate * dJdb
    return beta1, beta2, b
