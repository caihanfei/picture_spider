#coding:utf-8;
import os;
allfile = [];
def dirList(path):
    filelist = os.listdir(path);
    for filename in filelist:
        fpath = os.path.join(path,filename);#把路径和文件合并
        if os.path.isdir(fpath):
            dirList(fpath);
        allfile.append(fpath);
    return allfile;
print dirList('E:\java');
print len(allfile);
print '飞';


#os.walk()遍历目录方法
for path,dir,filelist in os.walk('E:\java'):
    for filename in filelist:
        print os.path.join(path,filename);
    
