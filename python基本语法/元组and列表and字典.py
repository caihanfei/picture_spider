# coding:utf-8
str1 = 'abcdef';
str2 = 'caihanfei';
print str1;
print str1[1:4];#//bcd
print str1[::2];#ace
print len(str1);#求长度
print str1+str2;
print str1*5;#重复
print 'cai' in str2;#判断字符是否在字符串中
str3 = '123456';
print max(str3);
print min(str3);
str4 = '1234567';
print cmp(str3, str4);#前者长度大于后者返回1，等于返回0，小于返回-1

#############元组数据类型 不能修改
# coding:utf-8
t = ("蔡汉飞",18,"长沙","湖南商学院");
print t;
print t[0];
print type(t);
name,age,city,school = t;
t1 = (2,);#单个元素元组后需要加逗号
print name,age,city,school;


#############列表数据类型
#列表是可变类型数据

listmilo = ['彭露','19','娄底','湖南女子学院'];
print type(listmilo);
print listmilo[0]; 
list = ['aaa'];#定义单个元素不要加逗号
listmilo[1] = 20;
listmilo.append('女');#添加一个值
print listmilo[4];
listmilo.remove(listmilo[1]);#删除一个值
listmilo.remove('娄底');


##########字典数据类型 无序
dic = {0:0,1:1,2:2};
print dic[0];
dic1 = {'name':'David','age':26,'sex':'man'}
print dic1['name'];
dic2 = {name:'rose',age:16,'sex':'woman'};
print dic2['sex'];

print dic1;

#遍历
for k in dic1:
    print k,dic1[k];
    

dic1['tel'] = '15580010951';
print dic1;
dic1.pop('tel');#删除
print dic1;
#dic1.clear(); #清楚字典所有元素
#del dic1;#删除整个字典
print dic1.items();#返回键值对元组列表
print dic1.keys();#返回所有key
print dic1.values();#返回所有valus