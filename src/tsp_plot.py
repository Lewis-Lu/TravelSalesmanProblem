'''TSP plotting section

'''
import MapInfo as mi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot(cor_matrix):
    '''plot function
    cor_matrix: coordination matrix
    '''
    mat = list(np.transpose(cor_matrix))
    fig = plt.figure()
    if len(mat) == 2:
        x = mat[0]
        y = mat[1]
        plt.plot(x, y,'ro')
        plt.axis([0, mi.map_size, 0, mi.map_size])
        plt.xlabel('x(m)')
        plt.ylabel('y(m)')
        plt.grid(True)
        plt.show()
    else:
        x = mat[0]
        y = mat[1]
        z = mat[2]
        ax = Axes3D(fig)
        ax.scatter(x, y, z, c='r')
        ax.set_xlabel('x (m)')
        ax.set_ylabel('y (m)')
        ax.set_zlabel('z (m)')
        
        plt.show()

def plot_path_2D(cor_matrix, init, sequence):
    '''plot_path_2D
    cor_matrix: coordination matrixexit
    init: initialization waypoint
    sequence: visit sequence
    '''
    
    for i in range(len(sequence)-1):
        if i == init:
            plt.plot(cor_matrix[sequence[i]][0],cor_matrix[sequence[i]][1],'rd', markersize='12')
        x = [cor_matrix[sequence[i]][0], cor_matrix[sequence[i+1]][0]]
        y = [cor_matrix[sequence[i]][1], cor_matrix[sequence[i+1]][1]]
        plt.plot(x, y, 'og--')

    plt.axis([0, mi.map_size, 0, mi.map_size])
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.grid(True)
    plt.show()
