########################################################
# Project in course "Dynamics of Socila Influence Networks"
#
# (c)
# Xudong Sun
# Adrian Wiltz
########################################################
import numpy as np
import scipy as sp

# Main Script

def simulate(mat_laplacian, fun_ode_rhs, row_vec_x0, tspan=[0, 100], num_grids=1000):
    """simulate.
    :param mat_laplacian:
    :param fun_ode_rhs:
    :param x0: must be a row vector
    :param tspan:
    :param num_grids:
    """
    num_agents = mat_laplacian.shape[0]
    sol = sp.integrate.solve_ivp(fun=lambda t, y: fun_ode_rhs(t, y, mat_laplacian, num_agents),
                                t_span=tspan,
                                y0=row_vec_x0,
                                vectorized=True,
                                dense_output=True,
                                t_eval=np.linspace(tspan[0],tspan[1], num_grids))
    return sol  # shape: (number of agents) \times (number of time points)
