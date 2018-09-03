# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:02:07 2018

@author: xiaojuan
"""
#从上面的例子可以看出，这连个是python中的可变参数，*args表示任意多个无名参数，是tulpe,**kwargs表示关键值参数，是dict

def foo(*args,**kwargs):
    print('args = ',args)
    print('kwargs = ',kwargs)
    print('-----------------------')
    
    
    
if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4,a=1,b=2,c=3)
    foo('a',1,None,a=1,b='2',c=3)
    
