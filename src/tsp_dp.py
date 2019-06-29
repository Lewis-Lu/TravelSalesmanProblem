__author__ = "Hong Lu"
__email__ = "hl2358@cornell.edu"
__copyright__ = "Copyright 2019, Hong Lu"

import Generate_Data as my_mat

def main():
    '''
    main function
    '''
    
    pass


def TSP_DP(c, cities):
    '''
    Dynamic Programming Method
    
    '''

    assert c not in cities,"first argument c in cities"


if __name__ == "__main__":
    N = 5
    mat = my_mat.Generate_Data(N)
    TSP_DP(1,[3,2])