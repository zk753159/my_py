# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 14:50:02 2018

@author: xiaojuan
"""

class Property(object):
    def __init__(self,propname,datatype,default = None):
        self._name = '_' + propname + '_'
        self._type = datatype
        self._default = default if default else self._type
        
    def __get__(self,instance,owner):
        return getattr(instance,self._name,self._default)
        
    def __set__(self,instance,value):
        if not isinstance(value,self._type):
            raise TypeError('Type Error,must be %s type' % self._type,)
        setattr(instance,self._name,value)
        
        
class Chinese(object):
    ID = Property('id',int)
    NAME = Property('name',str)

dasheng = Chinese()
print(dasheng.__dict__)
print(dasheng.ID)
print(dasheng.NAME)

dasheng.ID = 1
dasheng.NAME = 'dasheng'

print(dasheng.__dict__)
print(dasheng.ID)
print(dasheng.NAME)
            
        
    