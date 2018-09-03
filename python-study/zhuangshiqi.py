# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 22:57:32 2018

@author: xiaojuan
"""

import time

def log(func):
    def wrapper(*args,**kwargs):
        print('-' * 40)
        start = time.clock()
        res = func(*args,**kwargs)
        end = time.clock()
        print('calling',func.__name__,args,kwargs)
        print('start at ',start,' end at ',end)
        return res
    return wrapper
    
@log
def f(x,y):
    return x+y
  
#print(f(3,4))


log(f(3,4))    
    
        