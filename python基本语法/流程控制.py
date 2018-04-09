# coding:utf-8
#if语句严格要求缩进

def fun():
    return 1;

x = int(raw_input("please input:"));
if  x>=90:
    print "A";
elif x>=80:
    print "B";
elif x>=60:
    print "C";
else:
    print "D";
     

####for循环
str = "abcde";
for a in str:
    print a,"hello world";
    

for b in [1,2,3,4,5]:
    print b,"hello world";

t = range(100);
print t;

for key in range(1,51):
    print "haha",key;
    
for key in range(1,51,2):#隔一个数
    print "heihei",key;

sum = 0;
for a in range(1,101):
    sum = sum+a;
print  sum;  

for a in range(len(str)):
    print str[a];

#遍历字典
d = {1:111,2:222,3:333,4:444};
for k,v in d.items():
    print k,v;
    pass;
    
##while循环
x = ""
while x!="q":
    print "hello";
    x = raw_input("q,for quit");

   