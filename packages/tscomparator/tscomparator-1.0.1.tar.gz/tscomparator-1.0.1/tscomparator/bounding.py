import numpy as np
from utils import *
from scipy.interpolate import interp1d

def match_lengths(I, J):

    i_length, j_length = len(I), len(J)

    # Interpolating the longer of the two time series down to the length of the smaller one
    if i_length < j_length:
        J = interp1d(np.arange(0, j_length), J)(np.linspace(0.0, j_length-1, i_length))
    elif i_length > j_length:
        I = interp1d(np.arange(0, i_length), I)(np.linspace(0.0, i_length-1, j_length))
    return I, J


def LB_Keogh_squared_distances(q, C, r = np.inf):
    '''
    Computes the lower bound of two sequences being compared. The lower bound consists of 
    the sum of the distances of the first points of each series, and the last points of 
    each series.
    '''

    q, C = match_lengths(q, C)

    # Computing the lower bound
    sum = 0
    for i in range(len(q)):
        U = np.min(C[:,i])
        L = np.max(C[:,i])
        if q[i] < L:
            sum += (q[i] - L)**2
        elif q[i] > U:
            sum += (q[i] - U)**2
        if sum > r:
            return sum
    return sum


def euclidean_wedge(C): 
    '''
    Computes the wedge of a series. The wedge is the difference between the first and last
    points of the series.
    '''
    if np.any(np.diff(list(map(len, C)))!=0):
        raise ValueError('All series must be of the same length.')
    
    return np.min(C, axis = 0), np.max(C, axis = 0)

def DTW_wedge(C, w = 0):

    if np.any(np.diff(list(map(len, C)))!=0):
        raise ValueError('All series must be of the same length.')
    
    L, U = np.min(C, axis = 0), np.max(C, axis = 0)
    lower, upper = [],[]

    for i in range(len(C[0])):
        l = max(0, i-w)
        u = min(len(U), i+w+1)

        lower.append(min(L[l:u]))
        upper.append(max(U[l:u]))
    return np.array(lower), np.array(upper)

def LB_Keogh_DTW(q, wedge, r = np.inf):

    L, U = wedge[0], wedge[1]

    sum = 0
    for i in range(len(q)):
        if q[i] < L[i]:
            sum += (L[i] - q[i])**2
        elif q[i] > U[i]:
            sum += (q[i] - U[i])**2
        if sum > r:
            return sum
    return sum