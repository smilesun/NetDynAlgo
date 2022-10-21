"""
########################################################
# Project in course "Dynamics of Socila Influence Networks"
#
# (c)
# Adrian Wiltz
# Xudong Sun
########################################################
We use @ to denote matrix multiplication in this code
"""
import numpy as np


def stubborn_extremists(t,x,L,num_agents):
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
    x_dot = -(np.eye(num_agents) - np.diag(np.square(x))) @ L @ x
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
