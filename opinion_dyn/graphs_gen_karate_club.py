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
import numpy as np

def gen_adj_karate_club():
    graph = nx.karate_club_graph()
    arr_w = nx.adj_matrix(graph.to_directed()).toarray()
    return arr_w

