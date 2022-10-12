"""
########################################################
# Project in course "Dynamics of Socila Influence Networks"
#
# (c)
# Adrian Wiltz
# Xudong Sun
########################################################
"""
import numpy as np


def row_stochastic_adj_matrix(adj_matrix):
    """
    Desription:
    Normalizes the rows of adjacency matrix adj_matrix and outputs a row staochastic version of adj_matrix
    """
    row_sums = adj_matrix.sum(axis=1)
    row_stochastic_adj_matrix = adj_matrix / row_sums
    return row_stochastic_adj_matrix

def _calc_Laplacian(row_stochastic_adj_matrix):
    """
    Inputs:
    row_stochastic_adj_matrix
    Output:
    Laplacian
    """
    L = np.eye(len(row_stochastic_adj_matrix)) - row_stochastic_adj_matrix
    return L

def calc_Laplacian(adj_matrix):
    adj_normalized = row_stochastic_adj_matrix(adj_matrix)
    return _calc_Laplacian(adj_normalized)
