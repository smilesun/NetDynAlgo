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

def simulate(mat_laplacian, fun_ode_rhs):
    tspan = (0,100)
    n = mat_laplacian.shape[0]
    x0 = np.zeros(n)    # @FIXME: have a class to test different initial opinions
    sol = sp.integrate.solve_ivp(fun=lambda t, y: fun_ode_rhs(t, y, mat_laplacian,n),
                                t_span=tspan,
                                y0=x0,
                                vectorized=True,
                                dense_output=True,
                                t_eval=np.linspace(tspan[0],tspan[1],1000))
