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
from ode_rhs import stubborn_neutrals
from ode_rhs import stubborn_positives
from simulate import simulate

np.random.seed(0)


# Karate
adj_matrix_karate = gen_adj_karate_club()
mat_laplacian = calc_Laplacian(adj_matrix_karate).T
n = mat_laplacian.shape[0]

x0 = np.transpose(np.random.rand(n, 1)).squeeze()    
# x0 = 2*(x0-0.5)  # convert the [0, 1] uniform distribution to [-1, 1]

x0[0:5]= 1
# x0[0:2]= 1
# x0[3:5]=-1


sol = simulate(mat_laplacian, fun_ode_rhs=stubborn_neutrals, row_vec_x0=x0, tspan=[0,10000], num_grids=5000)

# Simulation
# Solve ode with scipy.integrate.solve_ivp (https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp)
colors = plt.cm.RdPu(np.linspace(0.3,0.8,n))
plt.figure()    
for i in range(n):
    plt.plot(sol.t,sol.y[i],color=colors[i])
plt.xlabel('time t')
plt.ylabel('x')
plt.show()
# plt.savefig("fig_rand_stubborn_extremists.pdf", format='pdf')

