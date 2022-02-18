def bootstrap(x, ci=0.95, N=1000):
  '''
  Input: 
    x: the data, where the rows are each sample and the columns are the time
    ci: the confidence interval level, from 0 to 1
    N: number of repetitions the bootstrap will perform
  Output: CI of ci. The lower and upper limits for each column are given.

  example:
    x = np.random.randn(50, 12)*5+40 #generating data
    CI = bootstrap(x) # computing the confidence intervals
    plt.plot(x.T) # plot of all the curves
    plt.plot(x.mean(axis=0), linewidth=5) # plot of the mean of all curves
    plt.plot(CI[0,:], 'r--', linewidth=4) # plot of the lower boundary of the confidence interval
    plt.plot(CI[1,:], 'r--', linewidth=4) # plot of the upper boundary of the confidence interval


  '''
  nrows = x.shape[0]
  ncols = x.shape[1]
  M = np.zeros((N, ncols))
  for i in range(N):
    samples = np.random.randint(0,nrows, nrows//2)
    M[i,:] = x[samples,:].mean(axis=0)
  CI = np.zeros((2, ncols))
  CI[0,:] = np.quantile(M,(1-ci)/2, axis=0)
  CI[1,:] = np.quantile(M,ci/2+0.5, axis=0)
  return CI
