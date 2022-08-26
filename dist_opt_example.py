# Adapted from Prof A.O.
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from fun_abs import l1grad, l1gradvec

n = 5
G = nx.star_graph(n)
A = nx.to_numpy_array(G)

def gen_interact_mat_from_adjacency(A):
    W = (1/(2*n))*A
    W[0][0] = 0.5
    for node in range(1, n+1):
        W[node][node] = 1-1/(2*n)  # fill value at diagonal element
    return W


W = gen_interact_mat_from_adjacency(A)

# gen stochastic matrix done

print(W)

x = np.zeros(n+1)  # initial value of parameter

vec_a = np.array([1, 2, 3.7, 3.7, 5, 6])  # each node has different function
step = 0.001
iters = 10000

for i in range(iters):
    # Note that each component of $x$ is being updated in distributed way
    # they are written together due to we assume synchronized update
    x = W @ x - step*l1gradvec(x, vec_a)  # @ means matrix multiplication
    print("parameter at each node: (consensus)", x)
