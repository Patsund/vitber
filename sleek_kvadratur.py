__author__ = 'Patrik'
# -*- coding: utf-8 -*-
#Integrators
def trapezoidIntegralFromArray(fValueArray,xArray,startIndex,endIndex):
    h=xArray[endIndex]-xArray[startIndex]
    y0=fValueArray[startIndex]
    y1=fValueArray[endIndex]
    return (h/2)*(y0+y1)
#dummies
def foo(x):
    return x**3
#util
def compositeIntegralFromTwoArrays(integrator,fValueArray,xArray):
    integral=0
    for i in range(len(xArray)-1):
        integral+=integrator(fValueArray,xArray,i,i+1)
    return integral
#main
def u_avg(fValueArray,xArray):
    return compositeIntegralFromTwoArrays(trapezoidIntegralFromArray,fValueArray,xArray)/(xArray[-1]-xArray[0])
#test
xArr=[1,1.5,1.75,1.8,2,2.5,2.66,3]
valArr=[]
for i in range(len(xArr)):
    valArr.append(foo(xArr[i]))
print(u_avg(valArr,xArr))