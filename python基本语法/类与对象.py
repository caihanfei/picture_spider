#coding:utf-8;
class Ren(object):
    name = '蔡汉飞';
    weight = 120;
    moeny = '200万'
    var1 = 200;
    def run(self):
        print self.name;
        print '跑步';
        self.__lie();#私有方法可以在类中被调用
    def moenya(self):
        print '查询余额';
        print self.moeny;
        self.var1 = 100;
    def __lie(self):#函数名前加__表示私有
        print '无法访问';
    
    @classmethod
    def classfun(self):
        print '类方法';
    
    @staticmethod
    def staticfun():
        print '静态方法';
if __name__ == '__main__':
    caihanfei = Ren();
    caihanfei.run();
    caihanfei.moenya();
#     caihanfei.__lie();
#     Ren.run(); 类无法直接调用方法 需对方法进行处理
    Ren.classfun();
    Ren.staticfun();
    print caihanfei.var1;