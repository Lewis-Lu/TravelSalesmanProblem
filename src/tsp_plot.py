'''TSP plotting section

'''
import MapInfo as mi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot(cor_matrix, specific=None, color='b', default_color='r'):
    '''plot function
    cor_matrix: coordination matrix
    '''
    mat = list(np.transpose(cor_matrix))
    fig = plt.figure()

    if specific != None:
        if len(mat) == 2:
            carrier_x = [mat[0][i] for i in range(0, specific)]
            carrier_y = [mat[1][i] for i in range(0, specific)]
            task_x = [mat[0][i] for i in range(specific, len(mat[0]))]
            task_y = [mat[1][i] for i in range(specific, len(mat[0]))]
            plt.plot(carrier_x, carrier_y, default_color+'D')
            plt.plot(task_x, task_y, color+'o')
            plt.xlabel('x(m)')
            plt.ylabel('y(m)')
            plt.grid(False)
            plt.show()
        else:
            carrier_x = [mat[0][i] for i in range(0, specific)]
            carrier_y = [mat[1][i] for i in range(0, specific)]
            carrier_z = [mat[2][i] for i in range(0, specific)]
            task_x = [mat[0][i] for i in range(specific, len(mat[0]))]
            task_y = [mat[1][i] for i in range(specific, len(mat[0]))]
            task_z = [mat[2][i] for i in range(specific, len(mat[0]))]
            ax = Axes3D(fig)
            ax.scatter(carrier_x, carrier_y, carrier_z, c=color)
            ax.scatter(task_x, task_y, task_z, c=default_color)
            ax.set_xlabel('x (m)')
            ax.set_ylabel('y (m)')
            ax.set_zlabel('z (m)')
            plt.show()
    else:
        if len(mat) == 2:
            x = mat[0]
            y = mat[1]
            plt.plot(x, y,'ro')
            plt.axis([0, mi._get_global_value('map_size'), 0, mi._get_global_value('map_size')])
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

    plt.axis([0, mi._get_global_value('map_size'), 0, mi._get_global_value('map_size')])
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
    plt.grid(True)
    plt.show()

def plot_cluster_3D(cluster, color=['silver','olive','tomato','linen','purple','y'], color_centroid='b'):
    
    fig = plt.figure()
    ax = Axes3D(fig)
    count = 0
    for i in range(len(cluster)):
        for j in cluster[i]:
            if count == 0:
                ax.scatter(j[0], j[1], j[2], c=color[i], marker='*')
            ax.scatter(j[0], j[1], j[2], c=color[i])
        count = 0
    
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')
    plt.show()

