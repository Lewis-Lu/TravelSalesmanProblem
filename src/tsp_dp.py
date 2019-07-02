__author__ = "Hong Lu"
__email__ = "hl2358@cornell.edu"
__copyright__ = "Copyright 2019, Hong Lu"

import sys
import Generate_Data as my_mat
import numpy as np
import time

'''DP method to handle TSP problem
     
'''
INIT_VAL = -1

N = 10 # quantity of positions

mat = my_mat.Generate_Data_Undirected(N) # position map

# use dp arrays to memorization
dp = np.ones((N, 2**N))*INIT_VAL # initialize dp with INIT_VAL
# use path to store path 
path = np.zeros((N, 2**N))


def TSP_DP(s, Vertex):
    '''Dynamic Programming Method
    
    s = current position
    Vertex = set of positions (use binary to represent)
    
    transition function: dp[cur][V] = min(TSP_DP(i, Vertex-{i}) + dist[s][i])
    '''
    # 
    # use memorization
    #
    if Vertex == ((1<<N)-1):
        return mat[s][0]
    
    if dp[s][Vertex] != INIT_VAL:
        return dp[s][Vertex]

    res = sys.maxsize
    for i in range(N): # considering position i, every possible minimal pathes to s
        if 0 == (Vertex & (1 << i)): # i is not visited
            Vertex_update = (Vertex | (1 << i))
            tmp = TSP_DP(i,Vertex_update) + mat[i][s]
            if tmp < res:
                res = min(tmp, res)
                dp[s][Vertex] = res
                
    return dp[s][Vertex]

if __name__ == "__main__":
    '''main function
    
    '''
    # 
    # for test
    # N = 5
    # mat = [
    #     [0, 4, 1, 3, 5],
    #     [4, 0, 8, 7, 3],
    #     [1, 8, 0, 5, 1],
    #     [3, 7, 5, 0, 1],
    #     [5, 3, 1, 1, 0]
    # ]
    for i in range(N):
        dp[i][0] = mat[i][0]
    #
    print("Dist:", end='\n')
    for i in mat:
        print(i, end='\n')
    #
    print("Path:", end='\n')
    for i in path:
        print(i, end='\n')
    start = time.time()
    ans = TSP_DP(0,1)
    finish = time.time()
    print("cost = ", ans, '\t', "time =", finish-start, end='\n')
    
