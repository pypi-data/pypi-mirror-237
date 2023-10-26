import numpy as np
from utils import *
from bounding import LB_Keogh_DTW, DTW_wedge

def dtw_matrix(I, J, w = 0, r = np.inf):
    
    n, m = len(I), len(J)
    w = set_window(I, J, w = w)

    # Constructing the matrix
    cum_sum = np.ones((n+1, m+1))*np.inf
    cum_sum[0, 0] = 0

    # Filling the matrix with the cumulative sum of the squared distances
    for i in range(1, n+1):
        for j in range(max([1, i-w]), min([m, i+w])+1):
            cost = (I[i-1] - J[j-1])**2
            cum_sum[i, j] = cost + min([cum_sum[i-1, j], cum_sum[i, j-1], cum_sum[i-1, j-1]])

            # Early abandoning condition
            if cum_sum[i, j] > r:
                return cum_sum
            
    return cum_sum

def dtw_path(matrix):
    i = matrix.shape[0] - 1
    j = matrix.shape[1] - 1
    path = []
    while i != 0 and j != 0:
        path.append((i - 1, j - 1))
        min_index = argmin([matrix[i-1, j-1], matrix[i-1, j], matrix[i, j-1]])
        if min_index == 0:
            i -= 1
            j -= 1
        elif min_index == 1:
            i -= 1
        else:
            j -= 1
    return path

def dtw(I, J, w = None, r = np.inf):
    '''
    Computes the dynamic time warping distance between two arrays. The window parameter
    is used to limit the search space of the algorithm.
    '''
    if type(I) is not np.ndarray:
        I = np.array(I, dtype = np.float64)
    if type(J) is not np.ndarray:
        J = np.array(J, dtype = np.float64)
    w = set_window(I, J, w = w)
    return dtw_matrix(I, J, w = w, r = r)[-1, -1]

def set_window(I, J, w = None):

    n, m = len(I), len(J)    
    if w == None:
        return max([n, m])
    elif type(w) is int:
        return w
    elif type(w) is float:
        return int(max([n, m])*w)
    else:
        raise TypeError('window must be an int or float')