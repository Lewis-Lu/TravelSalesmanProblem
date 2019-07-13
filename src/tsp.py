__author__ = "Hong Lu"
__email__ = "hl2358@cornell.edu"
__copyright__ = "Copyright 2019, Hong Lu"

import sys
import copy
import Generate_Data as my_mat
import time
import tsp_plot as tplt

'''
    n*n Random generated data (zero in diagonal)
    Naive way to solve TSP problem
    Time cmplx : O(n!)
'''

# global parameters

exp = {}
path = []
call = 0

def TSP(n, matrix):
    '''
    TSP function
    param n: represent n*n matrix
    param matrix: Cost Mat
    '''

    t = time.time()
    # recursively call Get_minimum
    visit = [i for i in range(1,n)]
    COST = Get_minimum(0, visit, matrix)
    duration = time.time() - t

    print("Task Quantity:",N," Opt Time(s) =", duration, end='\n') # output optimization duration

    # Critical Path
    C_PATH = []
    C_PATH.append(0) # add start point to path
    head = path.pop() # pop up first path buffer, get indexed
    C_PATH.append(head[1][0])
    # just to find n-2 times
    for i in range(n-2):
        for j in path:
            if j[0] == tuple(head[1]):
                head = j
                C_PATH.append(head[1][0])
                break
            if i == n-3:
                C_PATH.append(head[1][1][0])
                break
    return C_PATH, duration, COST


def Get_minimum(s, Vertex, mat):
    '''
        input(s, {Vertex})

        Recursively get minimal value (s, {v1, v2, v3, ... })
        base case = (s , {v}) return value in matrix
    '''
    # base case of dp 
    if(len(Vertex) == 1):
        global call
        call += 1
        return mat[s][Vertex[0]]

    # prepare variables
    values = []
    all_min = []
    # 
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
        res = Get_minimum(i, set_tmp, mat)
        all_min.append([i,tuple(set_tmp)])
        values.append(mat[s][i] + res)
        
    #
    # out of for-loop        
    # 
    MIN_COST = min(values)
    #
    # store the 
    #
    exp[s, tuple(Vertex)] = MIN_COST
    path.append(((s,tuple(Vertex)),tuple(all_min[values.index(MIN_COST)])))
    #
    # return the minimum cost of (s, {Vertex})
    #
    return MIN_COST


def Path_Verification(p, mat):
    ans = []
    for i in range(len(p)-1):
        ans.append(mat[p[i]][p[i+1]])
    return sum(ans)    
    
if __name__ == "__main__":
    #
    # FOR RANDOMLY GENERATED MATRIX
    # 
    N = 5
    dim = 2
    coordinates = my_mat.Generate_Coordinates(N, dim)
    mat = my_mat.Calculate_Cost(coordinates)
    for i in mat:
        print(i)
    print(end='\n')
    #
    # FOR TEST
    # 
    # N = 4
    # mat = [
    #     [0,1,6,2],
    #     [5,0,1,1],
    #     [6,4,0,1],
    #     [1,3,2,0]
    # ]
    #
    # FOR SHOW COST MAP
    #
    # for i in mat:
    #     print(i)
    # print('\n')
    arrangement, time, C = TSP(N, mat)
    cost = Path_Verification(arrangement, mat)
    arr = copy.deepcopy(arrangement)
    last = arr.pop()
    arrangement.append(0)
    cost += mat[last][0]
    print("COST:", cost, end='\n')
    print("Task Arrangement:", arrangement, end='\n')
    
    tplt.plot_path_2D(coordinates, 0, arrangement)

    sys.exit(0)

