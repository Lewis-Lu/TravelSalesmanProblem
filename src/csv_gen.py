import csv
import numpy as np
import MapInfo as mi



def Generate_Coordinates(n, dim, filename='../kmeans_yinyang/YinYang-K-Means/data_file.csv'):
    ''' Randomly generate coordinates
        n: waypoints quantity
        dim: dimension of coordinate
    '''
    res = np.zeros((n,dim))
    for i in range(n):
        for j in range(dim):
            rand_val = 100*np.random.random_sample()
            res[i][j] = rand_val
    np.savetxt(filename, res, delimiter=',')

if __name__ == "__main__":
    Generate_Coordinates(50, 2)
