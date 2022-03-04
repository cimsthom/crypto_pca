import numpy as np

def unique(list1):
 
    # initialize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def complete_cases(array):
    N,T = array.shape
    indx = np.zeros(N)
    for i in range(N):
        if np.isnan(array[i, :]).sum() == 0:
            indx[i]=True
    return indx


def non_negative_prices(array):
    N,T = array.shape
    indx = np.zeros(N)
    for i in range(N):
        if np.where(array[i, :]<0)[0].sum() == 0:
            indx[i]=True
    return indx