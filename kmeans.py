def kmeans(x, k, maxiter = 10, tensor = np.zeros((1))):
    '''
    clusters = kmeans(x, k, maxiter = 10, tensor = np.zeros((1)))
    
    Inputs: 
    - x: numpy array with one element per line. It can have many columns.
    - k: integer with the number of clusters
    - maxiter: number of iterations to find the cluster. Default is 10 iterations.
    - tensor: numpy array with the metric tensor of the vector space. Default is the identity matrix.
    
    Outputs:
    - clusters: list with the length equal to the number of clusters. Each element 
        of the list contains a numpy array with the indices of the elements of x that are
        in the respective cluster.      
    '''
    import numpy as np
    
    if tensor.all() == 0:
        tensor = np.eye(len(x))
    
    clusters = list(np.arange(k))
          
    for j in range(len(x)):
        chooseCluster = np.random.rand(1)
        for i in range(k):
            if (chooseCluster > i/k and chooseCluster <= (i+1)/k):
                if (not np.iterable(clusters[i])):
                    clusters[i] = np.array([j])
                else:
                    clusters[i] = np.append(clusters[i], j)
        
    for w in range(maxiter):
        means = np.zeros((k,x.shape[1]))
        for i in range(k):
            means[i,:] = np.mean(x[clusters[i],:], axis = 0)
           
        newClusters = list(np.arange(k))
        for j in range(len(x)):
            distance = np.zeros((k))
            for i in range(k):
                distance[i] = tensorNorm(x[j,:] - means[i,:], tensor)
            chosenCluster = np.argmin(distance)
            if (not np.iterable(newClusters[chosenCluster])):
                newClusters[chosenCluster] = np.array([j])
            else:
                newClusters[chosenCluster]  = np.append(newClusters[chosenCluster] , j)
        clusters = newClusters
    
    
    return clusters
