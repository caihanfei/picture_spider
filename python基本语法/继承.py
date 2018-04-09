#coding:utf-8;
class Animal():
    name = '动物'; 

class Man():
    name = '人类';
    def say(self):
        print '会说话';

class Chinese(Animal,Man):
    def __init__(self,name,age):#如果自己定义了构造方法，父类构造方法不会再调用
        self.name = name;
        self.age = age;
    def say(self):
        print '%s 会说中文 %d ' %(self.name,self.age);


caihanfei = Chinese('caihanfei',18);
caihanfei.say();
        