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

np.random.seed(0)


# Karate
adj_matrix_karate = gen_adj_karate_club()
mat_laplacian = calc_Laplacian(adj_matrix_karate)
n = mat_laplacian.shape[0]

x0 = np.transpose(np.random.rand(n, 1)).squeeze()    # initiale opinions  @FIXME: have a class to test different initial opinions



mat_traj_agents_steps = simulate(mat_laplacian, fun_ode_rhs=stubborn_extremists, row_vec_x0=x0)

# TODO visualization; verification of theoretic results and finding some further interesting scenarios :)
plt.figure()
plt.plot(mat_traj_agents_steps.T)
# plt.show()   this will avoid figure to be saved
plt.savefig("fig_karate_stubborn_extremists.pdf", format='pdf')
