# -*- coding: utf-8 -*-
import numpy as np
import math
import time
start_time=time.time()
PI = 3.14159265359


#dummies
def fDummyDoubleDerivated(x):
    return (math.exp(x))*(64*PI*PI*math.cos(8*PI*x)+16*PI*math.sin(8*PI*x)-math.cos(8*PI*x))

def f1(x,sigma):
    my = 2
    return math.exp(-((x-my)**2)/(sigma**2))

def fDummy(x):
    return math.exp(x)*math.cos(8*math.pi*x)

#Beregning av Ci:
def iDivisor(xArray, i):
    Ci = 1
    for k in range(N):
        if k != i:
            Ci *= (xArray[i]-xArray[k])
    return Ci

#Dobbelderivasjon
def negativeDoubleDerivator(i, x, xArray):
    doubleDerivate = 0
    for n in range(N):
        if (n != i): #Hopper over en stor iterasjonsløkke
            for m in range(N):
                if (m != i and m != n):
                    product = 1
                    for p in range(N):
                        if (p != i and p != m and p != n):
                            product *= (x-xArray[p])
                    doubleDerivate += product
    return -doubleDerivate

def spectral_laplace_lhs(xArray,iDivisorArray):
#    N = len(xArray)
#    a,b = xArray[0],xArray[N-1]
    A = np.zeros((N,N))
    A[0][0],A[N-1][N-1] = 1,1 #Her settes første og siste verdi i matrisen til 1
    #print("A før fylling: \n",A)
    for x in range(1,N-1): #Her er x kun en indeks
        for i in range(N):
#            A[x][i] = second_deriv(x,i,xArray,N) #n=x er indeks
            A[x][i] = negativeDoubleDerivator(i, xArray[x], xArray) #Gir feil på
            A[x][i] /= iDivisorArray[i]                               #type 10^64
#            A[x][i] = NDDLagrange(N,xArray,x,i) #Gammel løsning, deler på 0
    #print("A ferdig utfylt: \n",A)
    return A

def spectral_laplace_rhs(xArray,f,ua,ub,sigma):
#    N = len(x)
#    a,b = x[0],x[N-1]
    B = np.zeros(N)
    B[0],B[N-1] = ua, ub
    for i in range (1,N-1): #Her har jeg endret fra N-2 til N-1 onsdag 8. feb
        B[i] = f(xArray[i],sigma)
    #print ("B-matrise: \n",B)
    return B

def Lagrange(x, xArray,i):
    product = 1
    for p in range(N):
        if (p != i):
            product *= (xArray[x]-xArray[p])
    return product


def spectral_laplace(xArray,f,ua,ub,sigma):
    B = spectral_laplace_rhs(xArray,f,ua,ub,sigma) #Lager og printer matrise B
    U = np.linalg.solve(A,B) # solve the system. Gir oss løsningen U
    #print("Linalg sin losning av U-verdier:", U) #
    L = np.zeros((N,N))
    L[0][0],L[N-1][N-1] = 1,1
    for n in range(1,N-1):
        for i in range(N):
            L[n][i] = Lagrange(n,xArray,i) #Feilen var: xArray[i] i stedet for x
            L[n][i] /= iDivisorArray[i]
    #print ("L-matrise: \n",L) #
    fValuesComputedUsingU = np.dot(L,U)
    #print("fValuesComputedUsingU: \n",fValuesComputedUsingU) #
    return fValuesComputedUsingU

#Integrators
def trapezoidIntegralFromArray(fValueArray,xArray,startIndex,endIndex):
    h=xArray[endIndex]-xArray[startIndex]
    y0=fValueArray[startIndex]
    y1=fValueArray[endIndex]
    return (h/2)*(y0+y1)
#util
def compositeIntegralFromTwoArrays(integrator,fValueArray,xArray):
    integral=0
    for i in range(len(xArray)-1):
        integral+=integrator(fValueArray,xArray,i,i+1)
    return integral
#main
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
    #print("integral:",temp)
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
        #print("start: ",sigmaMin,"end: ",sigmaMax)
        nSigma=(sigmaMin+sigmaMax)/2
        temp=u_avg(nSigma,xArray)
        #print("integral:",temp)
        iter+=1
    if iter==itermax:
        print("no results found")
        return 0
    else:
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
#print("x: ",x_cheby)
end_time=time.time()
print("time spent:",end_time-start_time)