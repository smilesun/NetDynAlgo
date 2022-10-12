########################################################
# Project in course "Dynamics of Socila Influence Networks"
#
# (c)
# Xudong Sun
# Adrian Wiltz
########################################################

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import networkx as nx
import warnings

########################################################
# Function Definitions

# Graph generation
def generate_erdos_reny_graph(n,p,seed=2022,max_attempts=100):
    """
    Parameters:
    n - number of nodes
    p - edge probability
    seed - seed for random number generation
    max_attempts - maximum number of attempts to find a strongly connencted graph
    Return:
    adj_matrix - adjacency matrix as 2d numpy matrix
    G - networkx reny erdos graph
    G_is_strongly_connected - boolean
    Description:
    Raises a warning if within max_attempts no strongly connected graph could be found with given specifications.
    """

    G_is_strongly_connected = False
    for i in range(max_attempts):
        G = nx.gnp_random_graph(n, p, seed=seed, directed=True)
        if nx.is_strongly_connected(G):
            G_is_strongly_connected = True
            break
    
    # throw exception if now strongly connected graph was found
    if not G_is_strongly_connected:
        warnings.warn("No strongly conected erdos reny graph could be determined.")

    adj_matrix = (nx.adjacency_matrix(G, weight="None")).todense()

    return adj_matrix, G, G_is_strongly_connected

#TODO needs to be implemented
def generate_karate_club_graph():
    pass

# Compute Laplian

def row_stochastic_adj_matrix(adj_matrix):
    """
    Desription:
    Normalizes the rows of adjacency matrix adj_matrix and outputs a row staochastic version of adj_matrix
    """
    row_sums = adj_matrix.sum(axis=1)
    row_stochastic_adj_matrix = adj_matrix / row_sums
    return row_stochastic_adj_matrix

def calc_Laplacian(row_stochastic_adj_matrix):
    """
    Inputs:
    row_stochastic_adj_matrix
    Output:
    Laplacian
    """
    L = np.eye(len(row_stochastic_adj_matrix)) - row_stochastic_adj_matrix
    return L

# Opinion Dynamics

def stubborn_extremists(t,x,L,n):
    """
    Description:
    Implements dynamics of the model with stubborn extremists
    Inputs:
    t - time
    x - state
    L - Laplacian
    n - number of states
    Return:
    x_dot
    """
    x_dot = -(np.eye(n) - np.diag(np.square(x))) @ L @ x
    return x_dot

def stubborn_positives(t,x,L,n):
    """
    Description:
    Implements dynamics of the model with stubborn positives
    Inputs:
    t - time
    x - state
    L - Laplacian
    n - number of states
    Return:
    x_dot
    """
    x_dot = -0.5*(np.eye(n) - np.diag(x)) @ L @ x
    return x_dot

def stubborn_neutrals(t,x,L,n):
    """
    Description:
    Implements dynamics of the model with stubborn neutrals
    Inputs:
    t - time
    x - state
    L - Laplacian
    n - number of states
    Return:
    x_dot
    """
    x_dot = -np.diag(np.squares(x)) @ L @ x
    return x_dot

########################################################
# Main Script

n = 200 # number of agents

x0 = np.zeros(n)    # initiale opinions

# generate graph
adj_matrix_erdos_reny, G_erdos_reny, G_erdos_reny_is_strongly_connected = generate_erdos_reny_graph(n,0.25)

adj_matrix_erdos_reny_norm = row_stochastic_adj_matrix(adj_matrix_erdos_reny)
L_erdos_reny = calc_Laplacian(adj_matrix_erdos_reny_norm)

# Simulation
# Solve ode with scipy.integrate.solve_ivp (https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp)

# simulate reny erdos
tspan = (0,100)
sol = sp.integrate.solve_ivp(fun=lambda t, y: stubborn_extremists(t,y,L_erdos_reny,n), t_span=tspan, y0=x0, vectorized=True, dense_output=True, t_eval=np.linspace(tspan[0],tspan[1],1000))

#TODO complement code with KArate Club; visualization; verification of theoretic results and finding some further interesting scenarios :)