# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:56:52 2018

@author: xiaojuan
"""

class Chinese(object):
    nation = 'China'

    def __init__(self,id,name):
        self._id = id
        self.__name = name

    def sayHi(self,msg):
        print(self.__name,msg)
        
    #set、get方法设置属性
    def setID(self,id):
        self._id = id
        
    def getID(self):
        return self._id
        
    #属性装饰器的方式访问属性
    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
        
dasheng = Chinese(1,'dasheng')
print(dasheng.getID())

print(dasheng.name)
dasheng.name = "123"
print(dasheng.name)
    