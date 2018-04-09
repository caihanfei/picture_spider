#coding:utf-8
import socket;
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);#创建对象 ip4，tcp
s.bind(('127.0.0.1',5200));#绑定到主机上5200端口
s.listen(10)#监听 可以有十个客户端

while True:
    conn,addr = s.accept();#获得对象和客户端的ip地址和端口号
    print conn,addr;