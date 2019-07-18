''' k-means method
'''

import time
import sys
import random
import math
import matplotlib.pyplot as plt

N = 200
# space need to be persistent
PointsNearestCenter = [0 for i in range(N)] # need to keep this information for judgement


class Point:
    def __init__(self, coordinate):
        '''
        coordinate: [x,y]
        '''
        self.coordinate = coordinate
        self.dim = len(coordinate)
    
    def __repr__(self):
        return str(self.coordinate)

class Cluster:
    ''' a set of Point-class objectives
    '''
    def __init__(self, Points):
        if len(Points) == 0:
            raise Exception("Err: empty cluster")
        
        self.Points = Points
        self.point_dim = len(Points[0].coordinate)

        for P in Points:
            if P.dim != self.point_dim:
                raise Exception("Err: cluster's points' dimensions not the same")
        
        self.centroid = self.calculateCentroid()
    
    def calculateCentroid(self):
        '''find cluster centroid
        '''

        num_points = len(self.Points)
        
        # extract coordinate data of points
        coordinates = [P.coordinate for P in self.Points]
        coordinates_transpose = list(map(list, zip(*coordinates)))
        coordinates_centroid = [math.fsum(i)/num_points for i in coordinates_transpose]
        return Point(coordinates_centroid)

class K_means:
    def __init__(self, k, Points, initial):
        self.k = k
        self.Points =  Points
        self.initial = initial

    def Kmeans(self):
        ''' simple Kmeans
        k: divide into k clusters
        Points: list of Point(class object)
        '''
        if len(self.Points) == 0: # assert Points is not empty
            raise Exception("Err: Points is empty.")

        # get points coordinate
        points = [P.coordinate for P in self.Points]

        # store clusters' centroid trajectory
        centroid_traj = [ [] for i in range(self.k)]

        for i in range(len(self.initial)):
            centroid_traj[i].append(self.initial[i])

        # assignment
        Set_Clusters, converge = self.KmeansAssignment(points, self.initial)

        for i in range(len(Set_Clusters)):
            centroid_traj[i].append(Set_Clusters[i].centroid.coordinate)

        # iterate until algo converges
        count = 0
        while converge == 0:
            # recalculate new virtual cluster centroid
            centroids = self.CalculateCentroid(Set_Clusters)
            
            #assignment
            Set_Clusters, converge = self.KmeansAssignment(points, centroids)
            
            #save traj
            for i in range(len(Set_Clusters)):
                centroid_traj[i].append(Set_Clusters[i].centroid.coordinate)
            
            count += 1
            

        print("k-means converges afer ",count, "iterations", end='\n')
        
        return Set_Clusters, centroid_traj

    def CalculateCentroid(self, Set_Clusters):

        centroid = [[] for i in range(self.k)]

        for i in range(self.k):
            Points = Set_Clusters[i].Points
            n_points = len(Points)
            points = [p.coordinate for p in Points]
            transpose = list(map(list, zip(*points)))
            sum_x = sum(transpose[0])
            sum_y = sum(transpose[1])
            c = [sum_x/n_points, sum_y/n_points]
            centroid[i] = c
        return centroid

    def KmeansAssignment(self, points, centroids):
        # k-cluster centroids
        k = self.k
        # number of points
        n_points = len(points)
        # k clusters
        clusters = [[] for i in range(k)]
        
        converge_flag = 1

        for i in range(len(points)):
            p = points[i]
            p_all_dist = []
            for c in centroids:
                d = sum([(a-b)**2 for a, b in zip(p, c)])
                p_all_dist.append(d)
            index = p_all_dist.index(min(p_all_dist))
            # judge whether point has changed cluster?
            if index != PointsNearestCenter[i]: 
                # update index
                PointsNearestCenter[i] = index
                converge_flag = 0 # have not converge yet

        for i in range(n_points):
            cluster_index = PointsNearestCenter[i]
            point = points[i]

            # assign point to closet c-centered cluster 
            clusters[cluster_index].append(Point(point))
    
        Set_Cluster = []
        for c in clusters:
            Set_Cluster.append(Cluster(c))

        return Set_Cluster, converge_flag

def PointGen(dim, lower, upper):
    ''' Generate 
    '''
    p = Point([random.uniform(lower, upper) for i in range(dim)])
    return p

def Plot(Set_Cluster, traj):
    color = ["m", "c", "g", "y", "b", "crimson", "silver", "orangered", "tomato", "pink"]
    mark = ["v", "^", "1", "2", "p", "*", "x", "X", "D", "h"]
    
    n_cluster = len(Set_Cluster)

    for i in range(n_cluster):
        c = Set_Cluster[i] # c is Cluster objective
        coords = [p.coordinate for p in c.Points]
        centroid = c.centroid.coordinate
        # plot points
        for t in coords:
            plt.plot([t[0], centroid[0]], [t[1], centroid[1]], c=color[i], marker=mark[i])
        # plt.plot(centroid[0], centroid[1], c=color[i], marker='d')

    
    # number of clusters
    k = len(traj)

    for i in range(k):
        t = traj[i]
        transpose = list(map(list, zip(*t)))
        plt.plot(transpose[0], transpose[1], 'g--')

    plt.show()


def main():
    dim = 2
    lb = 0
    ub = 100
    

    # initialization randomly generate k centers
    k = 4
    initial_centroids_1 = [[random.uniform(0,100) for i in range(dim)] for j in range(k)]
    
    # 
    # initial test
    #
    # k = 3
    # initial_centroids_2 = [
    #     [100, 0],
    #     [0, 0],
    #     [0, 100]
    # ]

    # generate Points
    Points = [PointGen(dim, lb, ub) for i in range(N)]

    for i in range(10):
        handle = K_means(k, Points, initial_centroids_1)
        result, traj = handle.Kmeans()
        Plot(result, traj)


if __name__ == "__main__":
    main()
