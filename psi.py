def psi(spikes, binsize=1):
    '''
    PSI (population synchrony index) value as defined  in "Motor-Unit Synchronization Increases EMG Amplitude and Decreases Force Steadiness of Simulated Contractions
    Wanxiang Yao, Rew J. Fuglevand, and Roger M. Enoka, Journal of Neurophysiology 2000 83:1, 441-452"

    inputs:
    spikes - numpy array. The first column has the motor unit number and second column
    has the spikes instants, in ms.
    binsize- float number with the size of the bins, in ms. Default = 1 ms.

    outputs:
    psi - psi value 
    '''
    import numpy as np
    from numpy import histogram
    maxt = int(np.ceil(spikes[:,1].max()))
    hist, bins = histogram(spikes[:,1], bins=np.arange(0,maxt,binsize))
    nx, binsnx = histogram(hist, bins=np.arange(0, hist.max()+1))
    Nb = len(bins)
    m = spikes.shape[0]/Nb
    Nu = spikes[:,0].max()
    nindep = Nb*np.exp(-m)*(m**2)/2
    NCIindep = nindep*1
    NCI = nx[2]
    
    for x in binsnx[3:-1]:
        nindep = nindep*m/x
        NCIindep += nindep*x*(x-1)/2
        NCI += nx[x]*x*(x-1)/2

    PSI = (NCI - NCIindep)/NCIindep
    return PSI
