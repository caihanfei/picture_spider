#coding:utf-8
#文件查找   查找cai的个数
import re;
file = open('/java/caihanfei.txt','r');
count = 0;
for cai in file.readlines():
    number = re.findall(r'cai',cai);
    if len(number)>0:
        count = count+len(number);
print count;
file.close();

#文件替换 把fei替换成feifei
file1 = open('/java/caihanfei.txt','r');
file2 = open('/java/caihanfei2.txt','w+');
for fei in file1.readlines():
    file2.write(fei.replace('fei','feifei'));
    
file1.close();
file2.close();
