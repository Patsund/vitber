__author__ = 'Patrik'
# -*- coding: utf-8 -*-
#integrators
def trapezoidIntegral(f, startValue, endValue):
    h=endValue-startValue
    y0=f(startValue)
    y1=f(endValue)
    return (h/2)*(y0+y1)
def simpsonIntegral(f, startValue,endValue): #funker ikke
    x1=startValue+(endValue-startValue)/2
    h=endValue-x1
    y0=f(startValue)
    y1=f(x1)
    y2=f(endValue)
    return (h/3)*(y0+4*y1+y2)
#dummies
def foo(x):
    return x**4
"""def betterTrapezoid(f, startValue, endValue, steps):
    stepLength=(endValue-startValue)/steps
    current=startValue
    integral=0
    for i in range(steps):
        #print(current,current+stepLength,"\t")
        integral+=trapezoidIntegral(f,current,current+stepLength)
        current+=stepLength
    return integral
def betterSimpson(f, startValue, endValue, steps):
    stepLength=(endValue-startValue)/steps
    current=startValue
    integral=0
    for i in range(steps):
        integral+=simpsonIntegral(f,current,current+stepLength)
        current+=stepLength
    return integral"""
#utilities
def integralWithPartition(integrator,f,startValue,endValue,steps):
    stepLength=(endValue-startValue)/steps
    current=startValue
    integral=0
    for i in range(steps):
        integral+=integrator(f,current,current+stepLength)
        current+=stepLength
    return integral
def compositeSimpsonFromArray(f,arr):
    h=arr[1]-arr[0]
    integral=(h/3)*(f(arr[0])+f(arr[-1]))
    m=len(arr)//2
    for i in range(1,m+1):
        integral+=(4*h/3)*f(arr[2*i-1])
    for i in range(1,m):
        integral+=(2*h/3)*f(arr[2*i])
    return integral
"""
def compositeTrapezoidFromArray(f,arr):
    integral=f(arr[0])*(f(arr[1])-f(arr[0]))/2+f(arr[-1])*(f(arr[-1])-f(arr[-2]))/2
    for i in range(1,len(arr)-1):
        print(i,integral)
        integral+=f(arr[i])*(f(arr[i+1])-f(arr[i]))
    return integral
def betterCompositeTrapezoidFromArray(f,arr):
    integral=0
    for i in range(len(arr)-1):
        integral+=trapezoidIntegral(f,arr[i],arr[i+1])
    return integral
def betterCompositeSimpsonFromArray(f,arr):
    integral=0
    for i in range(len(arr)-1):
        integral+=simpsonIntegral(f,arr[i],arr[i+1])
    return integral"""
def compositeIntegralFromArray(integrator,f,arr):
    integral=0
    for i in range(len(arr)-1):
        integral+=integrator(f,arr[i],arr[i+1])
    return integral
#main f
def u_avg(f,startValue,endValue,steps):
    return integralWithPartition(simpsonIntegral,f,startValue,endValue,steps)/(endValue-startValue)
#test
#print(integralWithPartition(simpsonIntegral,foo,0,3,300000))
#print(integralWithPartition(trapezoidIntegral,foo,0,3,10000))
x=[0,1,2,3]
print(compositeIntegralFromArray(simpsonIntegral,foo,x))
print(integralWithPartition(simpsonIntegral,foo,0,3,3))