#coding:utf-8

import os;
os.mkdir('e');#创建文件夹
os.makedirs('aaa/b/c');#创建多级目录

os.rmdir('e');#删除目录
os.removedirs('aaa/b/c')#删除多级目录

print os.listdir('/java/swap');#查看目录下文件

print os.getcwd();#获得当前路径

os.chdir('/')#切换到根目录
print os.getcwd();
print os.listdir('.');#查看当前目录内容











