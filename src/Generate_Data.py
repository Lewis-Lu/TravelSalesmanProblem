import numpy as np
import MapInfo as mi


# def Generate_Data_Directed(n):
#     '''Randomly generate directed data
#     '''
#     res = []
#     for i in range(n):
#         row = np.random.random_sample([n])
#         row[i] = 0.0
#         res.append(row)
#     return res


# def Generate_Data_Undirected(n):
#     '''Randomly generate undirected map
#     '''
#     res = np.zeros((n, n))
#     for i in range(n):
#         for j in range(i+1, n):
#             rand = np.random.randint(1,10,size=1)
#             res[i][j] = rand
#             res[j][i] = res[i][j]
#     return res


def Generate_Coordinates(n, dim):
    ''' Randomly generate coordinates
        n: waypoints quantity
        dim: dimension of coordinate
    '''
    res = np.zeros((n,dim))
    for i in range(n):
        for j in range(dim):
            rand_val = mi._get_global_value('map_size') * np.random.random_sample()
            res[i][j] = rand_val
    return res


def Calculate_Cost(cor_mat):
    ''' Calculate cost matrix
        cor_mat: coordination matrix
    '''
    if 0 == len(cor_mat):
        print("No element in coordinate matrix", end='\n')
        return None
    n = len(cor_mat) # waypoints quantity
    cor_mat = np.array(cor_mat) # convert to array
    ans = np.array(np.zeros((n, n)))
    print("calculate waypoint cost matrix...", end='\n')
    print("coordinate dim is ", len(cor_mat[0]), end='\n')
    print("waypoint number is ", n, end='\n')
    for i in range(n):
        for j in range(i+1, n):
            ans[i][j] = np.linalg.norm(np.linalg.norm(cor_mat[i] - cor_mat[j]))
            ans[j][i] = ans[i][j]
    print("waypoint cost matrix complete.", end='\n')
    return list(ans)

