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


def gen_adj_karate_club():
    graph = nx.karate_club_graph()
    arr_w = nx.adj_matrix(graph.to_directed()).toarray()
    return arr_w

def gen_laplacian_karate_club():
    arr_w = gen_adj_karate_club()
    arr_w = normalize(arr_w, axis=1, norm='l1')
    arr_w.sum(axis=1) == 1
    arr_laplacian = np.eye(arr_w.shape[0]) - arr_w
    return arr_laplacian
