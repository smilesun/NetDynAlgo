"""
########################################################
# Project in course "Dynamics of Socila Influence Networks"
#
# (c)
# Xudong Sun
# Adrian Wiltz
########################################################
"""
import networkx as nx
import warnings


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


