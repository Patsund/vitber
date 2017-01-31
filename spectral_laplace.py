#BOLLEBOLLEBOLLE
# -*- coding: utf-8 -*-
import numpy as np
# set up the LHS (left hand side) for the spectral method for Laplace eqn
def spectral_laplace_lhs(x):
    N = len(x)
    a,b = x[0],x[N-1]
    A = np.zeros((N,N))
    # FIXIT: bestem A_ij
    return A
# set up the RHS (right hand side) for the spectral method for Laplace eqn
def spectral_laplace_rhs(x,f,ua,ub):
    N = len(x)
    a,b = x[0],x[N-1]
    B = np.zeros(N)
    # FIXIT: bestem B_i
    return B
    # set up the spectral method for Laplace eqn and solve the resulting system
def spectral_laplace(x,f,ua,ub):
    """
    Set up the spectral discretization of Laplace eqn on the interval x
    -u’’ = f; so f is the RHS of the system
    ua, ub - Dirichlet boundary conditions
    """
    #
    A = spectral_laplace_lhs(x)
    B = spectral_laplace_rhs(x,f,ua,ub)
    # solve the system
    return np.linalg.solve(A,B)
