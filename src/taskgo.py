from matplotlib import pyplot as plt
import Cluster.Kmeans as km
import TSP.tsp as tsp
import math

def LoadData(filename, category='tsplib'):
    root = 'src/TestBench/'+category+'/'
    with open(root+filename,'r') as f:
        if f == None:
            raise IOError("cannot open file")
        buffer = f.readlines() # buffer is list 
        _data_segment_head = 6
        coords = []
        for i in range(_data_segment_head, len(buffer)-1):
            _str_split = buffer[i].split()
            coords.append([float(_str_split[1]), float(_str_split[2])])
        return coords   

def Coords2Cost(coords):
    N = len(coords)
    cost = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            x_bias = coords[i][0] - coords[j][0]
            y_bias = coords[i][1] - coords[j][1]
            res = math.sqrt(x_bias**2 + y_bias**2)
            cost[i][j] = res
            cost[j][i] = cost[i][j]
    return cost


def Plot_2D(coords):
    transpose = list(map(list, zip(*coords)))
    x = transpose[0]
    y = transpose[1]
    plt.axis("equal")
    plt.scatter(x, y, marker='o', c='', edgecolors='b')

def main():
    '''main()

    for test 
    
    '''
    # # data for test
    # coords = [
    #     [0,0],
    #     [1,0],
    #     [0,1],
    #     [1,1]
    # ]
    coords = LoadData("pcb1173.tsp")
    coords = coords[:11]
    cost = Coords2Cost(coords)
    res = tsp.TSP(len(coords), cost).TSP_NAIVE()
    print(res, end='\n')
    res = tsp.TSP(len(coords), cost).TSP_DP()
    print(res, end='\n')

if __name__ == "__main__":
    main()