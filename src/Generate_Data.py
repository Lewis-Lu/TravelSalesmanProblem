import numpy as np

def Generate_Data_Directed(n):
    '''
    Randomly generate directed data
    '''
    res = []
    for i in range(n):
        row = np.random.random_sample([n])
        row[i] = 0.0
        res.append(row)
    return res


def Generate_Data_Undirected(n):
    '''
    Randomly generate undirected map
    '''
    res = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            rand = np.random.randint(1,10,size=1)
            res[i][j] = rand
            res[j][i] = res[i][j]
    return res


def Generate_Coordinates(n, dim):
    ''' Randomly generate coordinates

    '''
    res = np.zeros((n,dim))
    for i in range(n):
        for j in range(dim):
            rand_val = 100 * np.random.random_sample()
            res[i][j] = rand_val
    return res


# if __name__ == "__main__":
#     ans = Generate_Coordinates(4,2)
#     print(ans)