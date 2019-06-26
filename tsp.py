__author__ = "Hong Lu"
__email__ = "hl2358@cornell.edu"
__copyright__ = "Copyright 2019, Hong Lu"

import sys
import copy
import Generate_Data as my_mat
import time

'''
    n*n Random generated data (zero in diagonal)

'''

# global parameters
N = 10
mat = my_mat.Generate_Data(N)
exp = {}
path = []


def tsp(n, matrix):
    '''
    tsp function
    '''
    t = time.time()
    # recursively call Get_minimum
    Get_minimum(0, [i for i in range(1,n)])
    duration = time.time() - t
    
    print("Opt Time =", duration, "\n") # output optimization duration
    
    # # ouput data
    # for i in mat:
    #     print(i)
    # print("\n")
    # for i in exp:

    #     print(i, "\t", exp[i])
    # print("\n")

    # for i in path:
    #     print(i)
    # print("\n")


def Get_minimum(s, Vertex):
    '''
        input(s, {Vertex})

        Recursively get minimal value (s, {v1, v2, v3, ... })
        base case = (s , {v}) return value in matrix
    '''
    # base case of dp 
    if(len(Vertex) == 1):
        return mat[s][Vertex[0]]
    # prepare variables
    values = []
    all_min = []

    # do Vertex.size()'s computation in one iteration
    # total time cmplx is n!
    for i in Vertex:
        # calculate value respectively
        # for example
        #                  (a, {b, c, d})
        #                 /       |      \
        #         (b,{c,d})   (c,{b,d})   (d,{b,c})
        #        /  \            / \           /   \    
        # (c,{d}) (d,{c})  (b,{d}) (d,{b})  (b,{c}) (c,{b})
        set_tmp = copy.deepcopy(list(Vertex)) # have a copy of {Vertex}, convert to list
        set_tmp.remove(i)
        
        # call Get_minimum for smaller Vertex
        res = Get_minimum(i, set_tmp)
        all_min.append((s, tuple(set_tmp)))
        values.append(mat[s][i] + res)
    
    # find the minimum value
    exp[s, tuple(Vertex)] = min(values)
    min_val = min(values)
    path.append(((s, tuple(Vertex)), all_min[values.index(min_val)]))

    return min_val

if __name__ == "__main__":
   tsp(N, mat)
   sys.exit(0)
