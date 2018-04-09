#coding:utf-8
print abs(-10);#绝对值
l = [2,9,6,7,45,98,36,45,33];
print max(l);
print len(l);
print pow(2, 3);


s = "hello world";
print s.capitalize();#首字母大写

print s.replace('hello','hi');

ip ="192.168.1.123"
print ip.split('.');

def f(x):
    if x>5:
        return True;
l = range(1,10);
print filter(f,l);#过滤

print map(lambda x:x+1, range(1,5));

print reduce(lambda x,y:x*y, range(1,6));

name = ['cai','peng','xiao'];
age = [18,19,18];
tel = ['155','156','157'];

print zip(name,age,tel);