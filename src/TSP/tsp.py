'''
__author__ = "Hong Lu"
__email__ = "hl2358@cornell.edu"
__copyright__ = "Copyright 2019, Hong Lu"
'''

import sys
import copy
import time

'''
    n*n Random generated data (zero in diagonal)
    Naive way to solve TSP problem
    Time cmplx : O(n!)
'''

# global parameters

exp = {}
path = []

class TSP:
    def __init__(self, n, matrix): # matrix = cost mat
        self.n = n
        self.matrix = matrix
        # dp
        self._INIT_VAL = -1 # for dp usage
        self.dp = [[self._INIT_VAL for i in range(2**n)] for i in range(n)]
        for i in range(n):
            self.dp[i][0] = self.matrix[i][0]
        
        self.parent = [[self._INIT_VAL for i in range(2**n)] for i in range(n)]

    def TSP_NAIVE(self):
        '''TSP function
        n < 12 is appreciated

        param n: represent n*n matrix
        param matrix: Cost Mat
        '''

        t = time.time()
        # recursively call Get_minimum
        visit = [i for i in range(1,self.n)]
        COST = self.Get_minimum(0, visit, self.matrix)
        duration = time.time() - t

        # print("Task Quantity:", self.n, " Opt Time(s) =", duration, end='\n') # output optimization duration

        # Critical Path
        C_PATH = []
        C_PATH.append(0) # add start point to path
        head = path.pop() # pop up first path buffer, get indexed
        C_PATH.append(head[1][0])
        # just to find n-2 times
        for i in range(self.n - 2):
            for j in path:
                if j[0] == tuple(head[1]):
                    head = j
                    C_PATH.append(head[1][0])
                    break
                if i == self.n-3:
                    C_PATH.append(head[1][1][0])
                    break
        C_PATH.append(0)
        return C_PATH, duration, COST


    def Get_minimum(self, s, Vertex, mat):
        '''
            input(s, {Vertex})

            Recursively get minimal value (s, {v1, v2, v3, ... })
            base case = (s , {v}) return value in matrix
        
        '''
        #
        # base case of dp 
        #
        if(len(Vertex) == 1):
            return mat[s][Vertex[0]] + mat[Vertex[0]][0] # here we define 0 as the start point
        #
        # prepare variables
        # 
        values = []
        all_min = []
        # 
        # do Vertex.size()'s computation in one iteration
        # total time cmplx is n!
        # 
        for i in Vertex:
            # calculate value respectively
            # for example
            #                  (a, {b, c, d})
            #                 /       |      \
            #         (b,{c,d})   (c,{b,d})   (d,{b,c})
            #        /  \            / \           /   \    
            # (c,{d}) (d,{c})  (b,{d}) (d,{b})  (b,{c}) (c,{b})
            #   |        |        |       |        |       |
            #   a        a        a       a        a       a
            set_tmp = copy.deepcopy(list(Vertex)) # have a copy of {Vertex}, convert to list
            set_tmp.remove(i)
            # call Get_minimum for smaller Vertex
            res = self.Get_minimum(i, set_tmp, mat)
            all_min.append([i,tuple(set_tmp)])
            values.append(mat[s][i] + res)

        MIN_COST = min(values)
        exp[s, tuple(Vertex)] = MIN_COST
        path.append(((s,tuple(Vertex)),tuple(all_min[values.index(MIN_COST)])))
        #
        # return the minimum cost of (s, {Vertex})
        #
        return MIN_COST

    
    def TSP_DP(self):
        '''TSP_DP
        n < 21 is appreciated
        '''
        # do not have to change it
        cur_node = 0
        Visited = 1
        
        # calculate minimum cost
        start = time.time()
        res = self.TSP_DynamicProgramming(cur_node, Visited)
        end = time.time()
        duration = end - start
        
        # get the path
        parent = self.parent
        
        path = [0]
        while True:
            cur_node = parent[cur_node][Visited]
            if cur_node == -1: break
            path.append(cur_node)
            Visited = Visited | (1<<cur_node)
        path.append(0)

        return path, duration, res

    
    def TSP_DynamicProgramming(self, s, Visited):
        '''Dynamic Programming Method
        
        s = current position
        Vertex = set of positions (use binary to represent)
        
        transition function: dp[cur][V] = min(TSP_DP(i, Vertex-{i}) + dist[s][i])
        '''
        #
        #  base case
        # at point s, all vertices have been visited once
        if Visited == ((1<<self.n)-1):
            return self.matrix[s][0]
        
        if self.dp[s][Visited] != self._INIT_VAL: # using memorization
            return self.dp[s][Visited]
        #
        # begin of for loop
        # 
        res = sys.maxsize
        for i in range(self.n): # considering position i, every possible minimal path to s
            
            if 0 == (Visited & (1 << i)): # i is not visited
                Visited_update = (Visited | (1 << i))
                tmp = self.TSP_DynamicProgramming(i, Visited_update) + self.matrix[i][s]
                if tmp < res: #every update, we should store the path
                    res = min(tmp, res) # write in this form
                    self.dp[s][Visited] = res
                    self.parent[s][Visited] = i
        #
        # end of for loop
        #
        return self.dp[s][Visited]
        
