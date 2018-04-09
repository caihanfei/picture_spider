#coding:utf-8;
import os;
import shutil;
import json;

del_extension = {
    '.tmp':'临时文件',
    '_mp':'临时文件_mp',
    '.log':'日志文件',
    '.gid':'临时帮助文件',
    '.chk':'磁盘检查文件',
    '.old':'临时备份文件',
    '.xlk':'Excle备份文件',
    '.bak':'临时备份文件bak',
    }
# print json.dumps(del_extension.keys(), encoding="UTF-8", ensure_ascii=False);
print json.dumps(del_extension, encoding="UTF-8", ensure_ascii=False);
 
#获取系统盘
SYS_DRIVE = os.environ['systemdrive'];
#获取用户目录
USER_PROFILE = os.environ['userprofile'];
#获取windows目录
WIN_DIR = os.environ['windir'];
 
print os.getcwd().decode('gbk').encode('utf-8');#获取当前路径 
# os.chdir('E:\\');
 
def del_dir_or_file(root):
    try:
        if os.path.isfile(root):
            #删除文件
            os.remove(root);
            print '删除文件:'+root
        elif os.path.isdir(root):
            #删除文件夹
            shutil.rmtree(root);#此方法可以删除文件夹中有文件的文件夹
            print '删除目录'+root;
    except WindowsError:
        print '无法删除'+root;
         
#字节bytes转化k\m\g b
def formatSize(bytes):
    try:
        bytes = float(bytes);
        kb = bytes/1024
    except:
        print "传入字节格式错误"
        return 'Error';
    if kb>=1024:
        M = kb/1024;
        if M>=1024:
            G = M/1024;
            return '%fG'%(G);
        else: 
            return '%fM'%(M);
    else:
        return '%fkb'%(kb);
     
# print formatSize(61364164);

class DiskClean(object):
    
    del_file_paths = [];
    total_size = 0;
   
    def scan(self):
        for roots,files in os.walk(USER_PROFILE):
            for file in files:
                #返回后缀名
                file_extension = os.path.splitext(file)[1];
                if file_extension in del_extension.keys():
                    file_path = os.path.join(roots,file);
                    self.del_file_paths.append(file_path);
                    self.total_size += os.path.getsize(file_path);
                    
    def show(self):
        print '删除可节省:%s 空间' % formatSize(self.total_size)         
    def delete_files(self):
        for i in self.del_file_paths:
            del_dir_or_file(i);
Cleaner = DiskClean();
Cleaner.scan();
Cleaner.show();
if_del = raw_input('是否删除y/n\n');
if if_del == 'y':
    Cleaner.delete_files();

