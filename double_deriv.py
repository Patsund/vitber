# -*- coding: utf-8 -*-
from math import *
def foo(x):
    return x**27
def differentiate(f,value,tol):
    return (f(value+tol)-2*f(value)+f(value-tol))/tol**2
print(differentiate(foo,1,1e-6))