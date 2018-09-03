# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 21:55:38 2018

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
    
    def __init__(self,id,name):
        self.ID = id
        self.NAME =  name
        
    @staticmethod
    def getPeopleByParents(mother,father):
        print(mother,father)
        return Chinese(2,'dasheng')
    
    @classmethod
    def getPeopleBySibling(cls,sibling):
        print(sibling)
        return cls(3,'qitian')

class Jilin(Chinese):
    pass
        
    
dasheng = Chinese.getPeopleByParents('mother','father')

bajie = Chinese.getPeopleBySibling('sis')

Jilin.getPeopleByParents('aaa','bbb')
Jilin.getPeopleBySibling('brother')
print(Jilin.getPeopleBySibling('ddd').__dict__)
    
    