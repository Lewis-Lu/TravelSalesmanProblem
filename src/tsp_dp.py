__author__ = "Hong Lu"
__email__ = "hl2358@cornell.edu"
__copyright__ = "Copyright 2019, Hong Lu"

import sys
import Generate_Data as my_mat
import numpy as np

'''
    DP method to handle TSP problem
     
'''
INIT_VAL = -1

N = 5 # quantity of positions

mat = my_mat.Generate_Data_Undirected(N) # position map

# use dp arrays to memorization
dp = np.ones((N, 2**N))*INIT_VAL # initialize dp with INIT_VAL


def TSP_DP(s, Vertex):
    '''
    Dynamic Programming Method
    s = current position
    Vertex = set of positions (use binary to represent)
    
    transition function: dp[cur][V] = min(TSP_DP(i, Vertex-{i}) + dist[s][i])
    '''
    #
    # use memorization
    #
    if dp[s][Vertex] != INIT_VAL:
        return dp[s][Vertex]
    #
    # base case
    # 
    if Vertex == (1 << N):
        return mat[s][0]
    path_sum = sys.maxsize
    for i in range(N):
        min_val = TSP_DP(i, Vertex-{i})
        tmp = min_val + mat[s][i]
        if tmp < path_sum:
            path_sum = tmp

    dp[s][Vertex] = path_sum

if __name__ == "__main__":
    for i in range(N):
        dp[i][0] = mat[i][0]