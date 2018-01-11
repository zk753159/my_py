#!/usr/bin/python
#encoding:utf-8
"""
@zhangkaiaki
"""

y = range(6,9)

for (index,value) in enumerate(y):
    print(index,value)

z = range(-10,10)
print(sorted(z,key=abs))
