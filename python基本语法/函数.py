# coding:utf-8

def add(a,b):
    c = a+b;
    print c;
add(1,6);
add(2,1);

def add1(a,b=6):#默认参数     默认参数必须放后面 
    c = a+b;
    print c;
add1(6);
add1(5,6);

#变量的作用域
a=55
def fun():
    a = 100;
    global y;#强制声明全局变量,如果已有全局变量，相当于对y重新赋值
    y = 21;
    print a;
fun();
print a;

#向函数传递元组和字典
t = ('name','caihanfei');
def f(name='name',age=0):
    print "%s:%s" %(name,age);
f(*t);

d = {'age':30,'name':'penglu'};#字典的key和函数形参必须一样，才可以准确传值
f(**d)#传递字典用两个*

#传多个值,冗余参数
def f1(x,*args,**kwargs):
    print x;
    print args;
    print kwargs;
f1(1);
f1(5,5,6,9,7,1);
f1(5,3,6,9,7,p=10,y=600);

#lambad匿名函数
g = lambda x,y:x+y;
print g(5,9);

sum = reduce(lambda x,y:x*y,range(1,6));
print sum;
    