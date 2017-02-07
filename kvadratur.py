__author__ = 'Patrik'
# -*- coding: utf-8 -*-
#integrators
def trapezoidIntegral(function, startValue, endValue):
    h=endValue-startValue
    y0=function(startValue)
    y1=function(endValue)
    return (h/2)*(y0+y1)
def simpsonIntegral(function, startValue,endValue):
    x1=startValue+(endValue-startValue)/2
    h=endValue-x1
    y0=function(startValue)
    y1=function(x1)
    y2=function(endValue)
    return (h/3)*(y0+4*y1+y2)
#dummies
def foo(x):
    return x**4
"""def betterTrapezoid(function, startValue, endValue, steps):
    stepLength=(endValue-startValue)/steps
    current=startValue
    integral=0
    for i in range(steps):
        #print(current,current+stepLength,"\t")
        integral+=trapezoidIntegral(function,current,current+stepLength)
        current+=stepLength
    return integral
def betterSimpson(function, startValue, endValue, steps):
    stepLength=(endValue-startValue)/steps
    current=startValue
    integral=0
    for i in range(steps):
        integral+=simpsonIntegral(function,current,current+stepLength)
        current+=stepLength
    return integral"""
#utilities
def integralWithPartition(integrator,function,startValue,endValue,steps):
    stepLength=(endValue-startValue)/steps
    current=startValue
    integral=0
    for i in range(steps):
        integral+=integrator(function,current,current+stepLength)
        current+=stepLength
    return integral
def compositeSimpsonFromArray(function,array):
    h=array[1]-array[0]
    integral=(h/3)*(function(array[0])+function(array[-1]))
    m=len(array)/2
    for i in range(1,m+1):
        integral+=(4*h/3)*function(array[2*i-1])
    for i in range(1,m):
        integral+=(2*h/3)*function(array[2*i])
    return integral

def compositeTrapezoidFromArray(function,array):
    integral=function(array[0])*(function(array[1])-function(array[0]))/2+function(array[-1])*(function(array[-11])-function(array[-2]))/2
    for i in range(1,len(array)-1):
        integral+=function(array[i])*(function(array[i+1])-function(array[i]))
    return integral
#main function
def u_avg(function,startValue,endValue,steps):
    return integralWithPartition(simpsonIntegral,function,startValue,endValue,steps)/(endValue-startValue)
#test
print(integralWithPartition(simpsonIntegral,foo,0,3,300000))
print(integralWithPartition(trapezoidIntegral,foo,0,3,10000))