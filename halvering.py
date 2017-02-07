__author__ = 'Patrik'
# -*- coding: utf-8 -*-
#main function
def bisection(function,finalValue,startValue,endValue,tol):
    negative=False
    if function(startValue)-function(endValue)>0:
        negative=True
    c=(startValue+endValue)/2
    temp=function(c)
    N=0
    NMAX=100
    while abs(temp-finalValue)>tol and N<NMAX:
        if negative:
            if temp-finalValue<0:
                endValue=c
            else:
                startValue=c
        else:
            if temp-finalValue>0:
                endValue=c
            else:
                startValue=c
        print("start: ",startValue,"end: ",endValue)
        c=(startValue+endValue)/2
        temp=function(c)
        N+=1
    if N==NMAX:
        print("no results found")
        return 0
    else:
        return temp
#test
def foo(x):
    return x
print(bisection(foo,3,0,7,0.000001))