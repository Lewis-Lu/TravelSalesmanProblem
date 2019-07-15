'''task assignment for object
'''

import Generate_Data as my_mat

class TaskAssignment:
    def __init__(self, N_mobj, N_task, dim=2, method=None):
        self.N_mobj = N_mobj
        self.N_task = N_task
        self.dim = dim
        self.method = method

    def _spawn(self, map_size):
        rand = my_mat.Generate_Coordinates(self.N_mobj + self.N_task, self.dim)
        return rand

