''' main.py
main execution module
'''
import TSP.tsp_dp as tspdp
import TSP.tsp as tsp
import Generate_Data as my_mat
import MapInfo as mi
import numpy as np
import time

#
# global variables set up
#
mi._init() # map global variable initialization
mi._set_global_value('map_size', 100)
map_size = mi._get_global_value('map_size')
#
# local variables set up
#
N = 10
dim = 2
coordinate_map = my_mat.Generate_Coordinates(N, dim)
mat = my_mat.Calculate_Cost(coordinate_map)
dp = np.ones((N,2**N))*tspdp.TSP_DP.INIT_VAL
for i in range(N):
    dp[i][0] = mat[i][0]
path = []

handle = tspdp.TSP_DP(N, dim, coordinate_map, mat, dp, path)

start = time.time()
ans = handle.TSP_DP(0, 1)
finish = time.time()
print("cost = ", ans, '\t', "time =", finish-start, end='\n')
