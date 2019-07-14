'''
__author__ = "Hong Lu"
__email__ = "hl2358@cornell.edu"
__copyright__ = "Copyright 2019, Hong Lu"
'''

import sys

'''DP method to handle TSP problem
     
'''
class TSP_DP:
    ''' TSP_DP CLASS
    '''
    # class variables
    INIT_VAL = -1
    
    def __init__(self, N, dim, coordination_map, mat, dp, path):
        self.N = N
        self.dim = dim
        self.coordination_map = coordination_map
        self.mat = mat
        self.dp = dp # initialize dp with INIT_VAL
        self.path = path # use path to store path 
        
    # class functions
    def TSP_DP(self, s, Vertex):
        '''Dynamic Programming Method
        
        s = current position
        Vertex = set of positions (use binary to represent)
        
        transition function: dp[cur][V] = min(TSP_DP(i, Vertex-{i}) + dist[s][i])
        '''
        # 
        # use memorization
        #
        if Vertex == ((1<<self.N)-1):
            return self.mat[s][0]
        
        if self.dp[s][Vertex] != self.INIT_VAL:
            return self.dp[s][Vertex]
        #
        # begin of for loop
        # 
        res = sys.maxsize
        for i in range(self.N): # considering position i, every possible minimal pathes to s
            if 0 == (Vertex & (1 << i)): # i is not visited
                Vertex_update = (Vertex | (1 << i))
                tmp = self.TSP_DP(i,Vertex_update) + self.mat[i][s]
                if tmp < res:
                    res = min(tmp, res)
                    self.dp[s][Vertex] = res
        #
        # end of for loop
        #
        return self.dp[s][Vertex]