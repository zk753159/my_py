#!/usr/bin/python
#encoding:utf-8
"""
@zhangkaiaki
"""
import sys
x = input(u'请输入名字：'.encode(sys.stdout.encoding))
f = open('2.txt','w')
f.write(x.decode(sys.stdin.encoding).encode('utf-8'))
f.close()