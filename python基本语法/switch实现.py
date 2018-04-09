#coding:utf-8
from __future__ import division;
def jiafa(x,y):
    return x+y;

def jianfa(x,y):
    return x-y;

def chufa(x,y):
    return x/y;

def chengfa(x,y):
    return x*y;

def operator(x,o,y):
    if o == "+":
        return jiafa(x,y);
    elif o == "-":
        return jianfa(x,y);
    elif o == "*":
        return chengfa(x,y);
    elif o == "/":
        return chufa(x,y);
        
item = operator(5,'+',3);
print item;

operator1 = {"+":jiafa,"-":jianfa,"*":chengfa,"/":chufa};
def f(x,o,y):
    print operator1[o](x,y);
f(6,'*',9);
