# coding:utf-8
# !python
import re;

s = 'abc';

s = r'abc'; #字符串前加r构建正则表达式

print re.findall(s,'abcaaaaabcaa' );

st = 'top tip tap twp tep';
res = r't[oi]p';#o或者i
ris = r't[^oi]p';#取反
print re.findall(res,st);
print re.findall(ris,st);


hello = 'hello world,hello girl';

r = r'^hello';#匹配行首为hello $为匹配行尾

print re.findall(r, hello);

r1 = r'\^abc';#转义字符
abc = 'wgwgw^abcssgsgdw';
print re.findall(r1, abc);

#?标识存在一次或不存在  +标识存在一次或多次 *表示不存在或者存在多次
phonenumber = r'^010-?\d{8}$';#匹配北京电话号码

tel = re.compile(phonenumber); #创建编译对象
print tel;
print tel.findall('010-12659678');

name_re = re.compile(r'caihanfei',re.I);#大小写都可以匹配

print name_re.findall('caihanfei');
print name_re.findall('CAIHANFEI');


saaa = """hhsdj dskj hello src=csvt yes
jdjsds src=123 yes jdsa yes
src=2234 src=python yes kas yes
hello src=caihanfei yes jjsewg
""";
print saaa;

r1 = r"hello src=(.+) yes";#加括号后返回口号内的

src = re.compile(r1);
print src.findall(saaa);












