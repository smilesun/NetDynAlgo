########################################################
# Project in course "Dynamics of Socila Influence Networks"
#
# (c)
# Adrian Wiltz
# Xudong Sun
########################################################

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from graphs_gen import generate_erdos_reny_graph
from matrix_graph import calc_Laplacian
from ode_rhs import stubborn_extremists

# Main Script

n = 200 # number of agents

x0 = np.zeros(n)    # initiale opinions  @FIXME: have a class to test different initial opinions

# generate graph
adj_matrix_erdos_reny, G_erdos_reny, G_erdos_reny_is_strongly_connected = generate_erdos_reny_graph(n,0.25)

L_erdos_reny = calc_Laplacian(adj_matrix_erdos_reny)

# Simulation
# Solve ode with scipy.integrate.solve_ivp (https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp)

# simulate reny erdos
tspan = (0,100)
sol = sp.integrate.solve_ivp(fun=lambda t, y: stubborn_extremists(t,y,L_erdos_reny,n), t_span=tspan, y0=x0, vectorized=True, dense_output=True, t_eval=np.linspace(tspan[0],tspan[1],1000))

#TODO complement code with KArate Club; visualization; verification of theoretic results and finding some further interesting scenarios :)
