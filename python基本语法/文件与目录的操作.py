#coding:utf-8
import scrapy
fo = open('/java/javalist.txt','r+');#r模式不可写，r+模式可写可读 但是覆盖原文件

# print fo.read();
fo.write('hello,python');
fo.close();

# print fo.read();关闭了所以无法读取

f1 = file('/java/javalist.txt');
print f1.read();
f1.close();

fnew = open('/java/new.txt','w');#w形式删除原文件 ，文件不存在直接创建
fnew.write('hello world \ni am caihanfei');
fnew.close();

fnew = open('/java/new.txt','a+');#a模式不会覆盖原文件
# print fnew.read();
fnew.write('\nabc');
fnew.close();

print "蔡汉飞";

#文件对象

f0 = open('/java/new.txt');
s1 = f0.readline();#每次读取一行
f0.close();
print s1;

ff = open('/java/new.txt');
print ff.readlines();#把每行内容作为列表输出
ff.close();


f0 = open('/java/new.txt','a+');
l = ['\none\n','two\n','three\n'];
f0.writelines(l);#写入多行;
f0.close();

f1 = open('/java/new.txt','r+');
print f1.read();
f1.seek(0,0);#把指针传递回最开始
print f1.read();
f1.seek(0,2);#把指针传递回结尾
f1.write('xiaolulu');
f1.flush();#刷新缓存 可以不用关闭文件就看到文件实时内容
f1.seek(0,0);
print f1.read();
f1.close();








