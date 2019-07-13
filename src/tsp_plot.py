'''TSP plotting section

'''
import MapInfo as mi
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot(cor_matrix):
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
