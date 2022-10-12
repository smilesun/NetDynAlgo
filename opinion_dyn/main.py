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
from graphs_gen import generate_erdos_reny_graph
from graphs_gen_karate_club import gen_adj_karate_club
from matrix_graph import calc_Laplacian
from ode_rhs import stubborn_extremists
from simulate import simulate


n = 200 # number of agents

x0 = np.zeros(n)    # initiale opinions  @FIXME: have a class to test different initial opinions

# random graph graph
adj_matrix_erdos_reny, G_erdos_reny, G_erdos_reny_is_strongly_connected = generate_erdos_reny_graph(n,0.25)

L_erdos_reny = calc_Laplacian(adj_matrix_erdos_reny)

# Simulation
# Solve ode with scipy.integrate.solve_ivp (https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp)

simulate(L_erdos_reny, fun_ode_rhs=stubborn_extremists)

# Karate
adj_matrix_karate = gen_adj_karate_club()
mat_laplacian = calc_Laplacian(adj_matrix_karate)

simulate(mat_laplacian, fun_ode_rhs=stubborn_extremists)

# TODO visualization; verification of theoretic results and finding some further interesting scenarios :)
