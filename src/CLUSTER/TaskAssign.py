'''task assignment for object
'''

import Generate_Data as my_mat
import math

class TaskAssignment:
    def __init__(self, N_mobj, N_task, dim=2, method=None):
        self.N_mobj = N_mobj
        self.N_task = N_task
        self.dim = dim
        self.method = method

    def _spawn(self, map_size):
        ''' spawn randomized data
        first N_mobj data are actuators' coordinate
        '''
        rand = my_mat.Generate_Coordinates(self.N_mobj + self.N_task, self.dim)
        return rand

    def _cluster(self, cor_mat):
        ''' clustering of coordinate data
        '''
        cluster = [[] for i in range(self.N_mobj)]
        average_allocate_quantity =  math.floor(self.N_task/self.N_mobj)
        for i in range(self.N_mobj):
            cluster[i].append(cor_mat[i])
            for j in range(average_allocate_quantity):
                idx = average_allocate_quantity*i + j
                cluster[i].append(cor_mat[idx])
        # deal with rest data
        if self.N_mobj * average_allocate_quantity < self.N_task:
            for i in range(self.N_mobj + self.N_mobj*average_allocate_quantity, self.N_mobj+self.N_task):
                cluster[0].append(cor_mat[i])
        return cluster