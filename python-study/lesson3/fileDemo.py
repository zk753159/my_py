#!/usr/bin/python
#encoding:utf-8
"""
@zhangkaiaki
"""
import os
def getFilesList(rootDir):
   for path,dirlist,filelist in os.walk(rootDir):
       for filename in filelist:
           yield os.path.join(path,filename)

def openFiles(fileslist):
    for filename in fileslist:
        yield (filename,open(filename))

def grep(filelist,pattern):
    for(filename,fh) in filelist:
        for line in fh:
            if pattern in line:
                yield (filename,line)


filelist = getFilesList(u"D:\\北风\\git")
files = openFiles(filelist)
lines = grep(files,u"我是小张")

for(filename,line) in lines:
    print("~"*60)
    print(filename)
    print(line)

