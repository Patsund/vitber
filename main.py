# -*- coding: utf-8 -*-
import numpy as np
import math
import time
start_time=time.time()
PI = 3.14159265359

def fDummyDoubleDerivated(x):
    return (math.exp(x))*(64*PI*PI*math.cos(8*PI*x)+16*PI*math.sin(8*PI*x)-math.cos(8*PI*x))

def f1(x,sigma):
    my = 2
    return math.exp(-((x-my)**2)/(sigma**2))

def fDummy(x):
    return math.exp(x)*math.cos(8*math.pi*x)

def iDivisor(xArray, i):
    Ci = 1
    for k in range(N):
        if k != i:
            Ci *= (xArray[i]-xArray[k])
    return Ci

def negativeDoubleDerivator(i, x, xArray):
    doubleDerivate = 0
    for n in range(N):
        if (n != i):
            for m in range(N):
                if (m != i and m != n):
                    product = 1
                    for p in range(N):
                        if (p != i and p != m and p != n):
                            product *= (x-xArray[p])
                    doubleDerivate += product
    return -doubleDerivate

def spectral_laplace_lhs(xArray,iDivisorArray):
    A = np.zeros((N,N))
    A[0][0],A[N-1][N-1] = 1,1
    for x in range(1,N-1):
        for i in range(N):
            A[x][i] = negativeDoubleDerivator(i, xArray[x], xArray)
            A[x][i] /= iDivisorArray[i]
    return A

def spectral_laplace_rhs(xArray,f,ua,ub,sigma):
    B = np.zeros(N)
    B[0],B[N-1] = ua, ub
    for i in range (1,N-1):
        B[i] = f(xArray[i],sigma)
    return B

def Lagrange(x, xArray,i):
    product = 1
    for p in range(N):
        if (p != i):
            product *= (xArray[x]-xArray[p])
    return product


def spectral_laplace(xArray,f,ua,ub,sigma):
    B = spectral_laplace_rhs(xArray,f,ua,ub,sigma)
    U = np.linalg.solve(A,B)
    L = np.zeros((N,N))
    L[0][0],L[N-1][N-1] = 1,1
    for n in range(1,N-1):
        for i in range(N):
            L[n][i] = Lagrange(n,xArray,i)
            L[n][i] /= iDivisorArray[i]
    fValuesComputedUsingU = np.dot(L,U)
    return fValuesComputedUsingU

def trapezoidIntegralFromArray(fValueArray,xArray,startIndex,endIndex):
    h=xArray[endIndex]-xArray[startIndex]
    y0=fValueArray[startIndex]
    y1=fValueArray[endIndex]
    return (h/2)*(y0+y1)

def compositeIntegralFromTwoArrays(integrator,fValueArray,xArray):
    integral=0
    for i in range(len(xArray)-1):
        integral+=integrator(fValueArray,xArray,i,i+1)
    return integral

def u_avg(sigma,xArray):
    fValueArray=spectral_laplace(xArray,f1,-1,1,sigma)
    return compositeIntegralFromTwoArrays(trapezoidIntegralFromArray,fValueArray,xArray)/(xArray[-1]-xArray[0])

def main(xArray):
    sigmaMin=2.3
    sigmaMax=3
    finalValue=3
    tol=1e-6
    negative=False
    if u_avg(sigmaMin,xArray)>u_avg(sigmaMax,xArray):
        negative=True
    nSigma=(sigmaMin+sigmaMax)/2
    temp=u_avg(nSigma,xArray)
    iter=0
    itermax=1000
    while abs(temp-finalValue)>tol and iter<itermax:
        if negative:
            if temp-finalValue<0:
                sigmaMax=nSigma
            else:
                sigmaMin=nSigma
        else:
            if temp-finalValue>0:
                sigmaMax=nSigma
            else:
                sigmaMin=nSigma
        nSigma=(sigmaMin+sigmaMax)/2
        temp=u_avg(nSigma,xArray)
        iter+=1
    if iter==itermax:
        print("no results found")
        return 0
    else:
        print("iter = ",iter+1)
        return nSigma
a=0
b=10
N=40
x_uniform = np.linspace(a,b,N)
x_cheby = (b+a)/2. + (a-b)/2. * np.cos(np.arange(N)*np.pi/(N-1))
iDivisorArray = np.zeros(N)
for i in range (N):
    iDivisorArray[i] = iDivisor(x_cheby, i)
A = spectral_laplace_lhs(x_cheby,iDivisorArray)
print("sigma: ",main(x_cheby))
end_time=time.time()
print("time spent:",end_time-start_time)
