#coding:utf-8
import copy;
a = [1,2,3,'b','a','c'];
 
b = a;
 
print b;
 
a.append('d');
 

print "%s,%s" %(id(a),id(b));#a，b地址相同
#通过拷贝使改变b的同时不改变a
c = [1,2,3,['a','b','c']];
print c;

d = copy.copy(c);#浅拷贝
print d;
print "%s,%s" %(id(c),id(d));#c,d地址不同

#浅拷贝单个元素的地址仍然相同，深拷贝则不同
print "%s,%s" %(id(c[0]),id(d[0]));

e = copy.deepcopy(c);#深拷贝
print e;
print "%s,%s" %(id(c[0]),id(e[0]));
print "%s,%s" %(id(c[3]),id(e[3]));


