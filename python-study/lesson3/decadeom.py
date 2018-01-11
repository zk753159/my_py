#!/usr/bin/python
#encoding:utf-8
"""
@zhangkaiaki
"""
import time
def log(func):
    def wrapper(*args,**kwargs):
        print("~" * 40)
        start = time.clock()
        res = func(*args,**kwargs)
        end = time.clock()
        print("calling",func.__name__,args,kwargs)
        print("start at",start,"end at",end)
        return res
    return wrapper

#@log
#def f(x,y):
#    return x+y

def logex(name):
    def log(func):
        def wrapper(*args,**kwargs):
            print("~" * 40)
            start = time.clock()
            res = func(*args,**kwargs)
            end = time.clock()
            print(name,"calling",func.__name__,args,kwargs)
            print("start at",start,"end at",end)
            return res
        return wrapper
    return log

@logex("tom")
def g(x,y):
    return x*y
#print(f(10,20))
print(g(10,20))
