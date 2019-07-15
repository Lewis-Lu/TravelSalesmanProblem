''' main.py
main execution module
'''
import CLUSTER.TaskAssign as ta
import TSP.tsp_dp as tspdp
import TSP.tsp as tspnaive
import Generate_Data as my_mat
import tsp_plot as tplt
import MapInfo as mi
import numpy as np
import time
import sys
import copy

#
# global variables set up
#
mi._init() # map global variable initialization
mi._set_global_value('map_size', 100)
mi._set_global_value('naive_N', 10)
mi._set_global_value('dp_N', 20)
mi._set_global_value('dim', 2)
mi._set_global_value('taskpoint', 100)
mi._set_global_value('carrier', 5)

def TaskClusterAssignment():
    n_task = mi._get_global_value('taskpoint')
    n_carrier = mi._get_global_value('carrier')
    handle = ta.TaskAssignment(n_carrier, n_task, 3)
    return handle._spawn(mi._get_global_value('map_size'))

def TravelingAssignment():
    dim = mi._get_global_value('dim')
    naive_N = mi._get_global_value('naive_N')
    dp_N = mi._get_global_value('dp_N')
    map_size = mi._get_global_value('map_size')
    #
    # prompt
    #
    prompt = ">> choose which solver, (1)(naive way) (2)(dynamic programming) \n>>"
    choice = input(prompt)

    if choice == '1':
        coordinate_map = my_mat.Generate_Coordinates(naive_N, dim)
        mat = my_mat.Calculate_Cost(coordinate_map)
        # get handle
        handle = tspnaive.TSP_NAIVE(naive_N, mat)
        arrangement, time, C = handle.TSP()
        cost = handle.Path_Verification(arrangement, mat)
        arr = copy.deepcopy(arrangement)
        last = arr.pop()
        arrangement.append(0)
        cost += mat[last][0]
        print("COST:", cost, end='\n')
        print("Task Arrangement:", arrangement, end='\n')

        tplt.plot_path_2D(coordinate_map, 0, arrangement)
    elif choice == '2':
        coordinate_map = my_mat.Generate_Coordinates(dp_N, dim)
        mat = my_mat.Calculate_Cost(coordinate_map)
        dp = np.ones((dp_N, 2**dp_N))*tspdp.TSP_DP.INIT_VAL
        for i in range(dp_N):
            dp[i][0] = mat[i][0]
        path = []
        # get handle
        handle = tspdp.TSP_DP(dp_N, dim, coordinate_map, mat, dp, path)
        start = time.time()
        ans = handle.TSP_DP(0, 1)
        finish = time.time()
        print("cost = ", ans, '\t', "time =", finish-start, end='\n')

if __name__ == "__main__":

    tplt.plot(TaskClusterAssignment(), mi._get_global_value('carrier'))
