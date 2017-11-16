'''
Implements the MFROLS algorithm (see page 97 from Billings, SA (2013)).

% written by: Renato Naville Watanabe 

% beta = mfrols(p, y, pho, s)
% Inputs:

%   p: matrix of floats, is the matrix of candidate terms.
%   y: vector of floats, output signal.
%   pho: float, stop criteria.
%   s: integer, iteration step of the mfrols algorithm.

% Output:

%   beta: vector of floats, coefficients of the chosen terms.

% Globals:


%   l: vector of integers, indices of the chosen terms.
%   err: vector of floats, the error reduction ratio of each chosen term.
%   ESR: float, the sum of the individual error reduction ratios.
%   A: matrix of floats, auxiliary matrix in the orthogonalization process. 
%   q: matrix of floats, matrix with each column being the terms orthogonalized by the Gram-Schmidt process.
%   g: vector of floats, auxiliary vector in the orthogonalization process.
%   M0:	integer, number of chosen terms.
'''

def mfrols(p, y, pho, s):
    import numpy as np
    

    global l
    global err
    global ESR
    global A
    global q 
    global g 
    global M0

    M = np.shape(p)[1]
    L = np.shape(p)[2]
    gs= np.zeros((L,M))
    ERR=np.zeros((L,M))
    qs=np.zeros_like(p)

    for j in range(L):
        sigma = np.transpose(y[:,j])@y[:,j]
        for m in range(M):
            if np.max(m*np.ones_like(l)==l)==0:
                ## The Gram-Schmidt method was implemented in a modified way, as shown in Rice, JR(1966)
                qs[:,m,j] = p[:,m,j]
                for r in range(s):
                    qs[:,m,j] = qs[:,m,j] - (np.transpose(np.squeeze(q[:,r,j]))@qs[:,m,j])/(np.transpose(np.squeeze(q[:,r,j]))@np.squeeze(q[:,r,j]))*np.squeeze(q[:,r,j])
                gs[j,m] = (np.transpose(y[:,j])@np.squeeze(qs[:,m,j]))/(np.transpose(np.squeeze(qs[:,m,j]))@np.squeeze(qs[:,m,j]))
                ERR[j,m] = (gs[j,m]**2)*(np.transpose(np.squeeze(qs[:,m,j]))@np.squeeze(qs[:,m,j]))/sigma
            else:
                ERR[j,m]=0   

    ## global variables assignment

    ERR_m = np.mean(ERR, 0)
    l[s] = np.nonzero(ERR_m == np.max(ERR_m))[0]
    err[s] = ERR_m[int(l[s])]
    for j in range(L):
        for r in  range(s-1):
            A[r, s, j] = (np.transpose(q[:,r,j])@p[:,int(l[s]),j])/(np.transpose(q[:,r,j])@q[:,r,j])    
        A[s, s, j] = 1
        q[:, s,j] = qs[:,int(l[s]),j]
        g[j,s] = gs[j,int(l[s])]    

    ESR = ESR - err[s]   

    ## recursive call 

    if (err[s] >= pho and s < M-1):
        s += 1
        del qs 
        del gs
        beta = mfrols(p, y, pho, s)
    else:
        M0 = s
        s += 1
        beta = np.empty((M0,L))
        for j in range(L):
            print(M0)
            beta[:,j] = np.linalg.inv(np.squeeze(A[0:M0,0:M0,j]))@np.transpose(g[j,0:M0])
            
    return beta  
