import numpy as np
from utils import *
from dynamic_time_warping import *
from bounding import *

def similarity_search(Q: np.array, C: list[np.array], window: int) -> int:
    '''
    This function takes a query array to search against a list of arrays. It 
    returns the index of the nearest array.
    '''
    bsf = np.inf, count = 0
    Q = z_normalize(Q)
    while count < len(C):
        i = count%window


def DTW_query(q, C, w = 0, set_length = False):

    if type(q) is not np.ndarray:
        q = np.array(q, dtype = np.float64)

    if set_length != False:

        if type(set_length) in [int]:
            C = np.array([interpolate(c, set_length) for c in C])

        else:
            raise TypeError('set_length must be an int')
        
    elif type(C) is not np.ndarray:
        C = np.array(C, dtype = np.float64)

    elif any(np.diff(list(map(len, C))) != 0):
        raise ValueError('''All series must be of the same length. If you wish to query against a list of series of 
                         different lengths, set set_length to the desired length of the series.''')

    w = set_window(q, C[0], w = w)

    best_so_far = np.inf
    best_index = None
    wedge = DTW_wedge(C, w = w)

    for i in range(len(C)):
        lb = LB_Keogh_DTW(q, wedge, r = best_so_far)
        if lb > best_so_far:
            continue
        dist = dtw(q, C[i], w = w, r = best_so_far)
        if dist < best_so_far:
            best_so_far = dist
            best_index = i

    return best_index

def pairwise_argmin(C):
    '''
    '''
    pass

def time_series_search(series, window = 'auto'):
    '''
    '''
    pass