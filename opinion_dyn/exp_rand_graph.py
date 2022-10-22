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
from ode_rhs import stubborn_positives
from ode_rhs import stubborn_neutrals
from simulate import simulate

np.random.seed(0)

##################################Experiment 1

n = 20 # number of agents only for random graph generation

x0 = np.transpose(np.random.rand(n, 1)).squeeze()    # initiale opinions  @FIXME: have a class to test different initial opinions
x0 = 2*(x0-0.5)  # change from [0, 1] uniform to [-1, 1] uniform

x0[0:4] = 1

# random graph graph
adj_matrix_erdos_reny, G_erdos_reny, G_erdos_reny_is_strongly_connected = generate_erdos_reny_graph(n,0.25)

L_erdos_reny = calc_Laplacian(adj_matrix_erdos_reny)

sol = simulate(L_erdos_reny, fun_ode_rhs=stubborn_neutrals, row_vec_x0=x0, tspan=[0,500], num_grids=500)

# Simulation
# Solve ode with scipy.integrate.solve_ivp (https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp)
colors = plt.cm.RdPu(np.linspace(0.3,1,n))
plt.figure()    
for i in range(n):
    plt.plot(sol.t,sol.y[i],color=colors[i])
plt.xlabel('time t')
plt.ylabel('x')
plt.show()
# plt.savefig("fig_rand_stubborn_extremists.pdf", format='pdf')

