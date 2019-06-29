import numpy as np

def Generate_Data(n):
    '''
    Randomly generating data
    '''
    res = []
    for i in range(n):
        row = np.random.random_sample([n])
        row[i] = 0.0
        res.append(row)
    return res