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
#main function
def u_avg(function,startValue,endValue,steps):
    return integralWithPartition(simpsonIntegral,function,startValue,endValue,steps)/(endValue-startValue)
#test
print(integralWithPartition(simpsonIntegral,foo,0,3,5))
print(integralWithPartition(trapezoidIntegral,foo,0,3,50))
