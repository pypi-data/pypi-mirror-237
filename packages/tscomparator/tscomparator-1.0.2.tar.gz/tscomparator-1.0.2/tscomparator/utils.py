import numpy as np
from typing import *
from scipy.interpolate import interp1d


def interpolate(array, length):
    array_length = len(array)
    return interp1d(np.arange(0, array_length), array)(np.linspace(0.0, array_length-1, length))

def euclidean_distance(I: np.array, J: np.array, r: Optional[float] = None) -> float:
    '''
    Computes the euclidean distance between two arrays.
    '''
    if r == None:
        return np.linalg.norm(I-J)
    else:
        sum = 0
        for i in range(len(I)):
            sum += (I[i]-J[i])**2
            if sum > r:
                return np.inf
        return sum**0.5
    
def argmin(args: list) -> int:
    '''
    Returns the index of the minimum element in the list.
    '''
    min_index = 0
    for i in range(1, len(args)):
        if args[i] < args[min_index]:
            min_index = i
    return min_index

def squared_distance(i: float, j: float) -> float:
    '''
    Computes the squared distance between two floats.
    '''
    return (i-j)**2

def absolute_distance(i: float, j: float) -> float:
    '''
    Computes the squared distance between two floats.
    '''
    return abs(i-j)

def z_normalize(I: np.array) -> np.array:
    '''
    '''
    return (I-np.mean(I))/np.std(I)

def z(i: float, mu: float, sigma: float) -> float:
    '''
    '''
    return (i-mu)/sigma

def rank_indices(query: np.array) -> list[int]:
    '''
    Z-normalizes the query, and ranks each Qi according to absolute value.
    '''
    pass
