import os, sys
'''
ret= os.access('aa.txt',os.F_OK)
print('F_OK',ret)
ret= os.access('aa.txt',os.R_OK)
print('R_OK',ret)
ret= os.access('aa.txt',os.W_OK)
print('W_OK',ret)
ret= os.access('aa.txt',os.X_OK)
print('X_OK',ret)

currentPath=os.getcwd()
print('当前工作目录:',currentPath)
os.chdir("test")
nowPath=os.getcwd()
print('当前工作目录:',nowPath)
'''

'''
fd=os.open('test.txt',os.O_RDWR|os.O_CREAT)
msg='This is a test!'
ret=os.write(fd,bytes(msg,'utf-8'))
print(ret)
os.close(fd)
'''

'''
fd=os.open('test.txt',os.O_RDONLY)
msg=os.read(fd,10)
print(msg)
os.close(fd)
'''

#使用os.mkdir(path)创建目录,不可以创建带子目d录的文件夹
#os.mkdir('top')
#os.mkdir('test/top2')

#使用os.makedirs(path)递归创建目录,可以是包含子目录
#os.makedirs("path/new/new1")

#获取目录下文件os.listdir()
#dirlist=os.listdir("test")
#print(dirlist)

#使用os.walk()遍历目录
'''dirtuple=os.walk('test',topdown=True)
for root,dirs,files in dirtuple:
    print("根目录:",root)
    for name in dirs:
        print(os.path.join(root,name))
    for name in files:
        print(os.path.join(root,name))
'''

#修改目录
#os.rename('top','down')
#os.rename('test.txt','new.txt')

#os.renames('down','top/new')
#os.renames('new.txt','top/new/new1/new1.txt')

#删除目录
# os.rmdir()方法
#os.remove('top/new/new1/new1.txt') #删除一个文件
#os.rmdir('top/new/new1')  #删除一个文件夹
#os.makedirs('top/new/new1/new2/new3') #创建一个包含子目录的文件夹
#os.removedirs('top/new/new1/new2/new3') #递归删除top目录

'''
使用fileinput模块操作文件
'''
#读取两个文本文件内容
'''import fileinput

def demo_fileinput():
    with fileinput.input(['a.txt','aa.txt']) as lines:
        for line in lines:
            print('总行数%d' %fileinput.lineno(),'文件%s中的第%d行' %(fileinput.filename(),fileinput.filelineno()))
            print(line.strip())

demo_fileinput()
'''

#批量获取文件名
'''filenames=[]
for a, b, files in os.walk("test/top2"):
    if files:
        filenames.append([file[:-4] for file in files])
print(filenames)
f=open('Excel.xls',"w")
for files in filenames:
    for name in files:
        f.write(name[:-4]+"\t"+name[-4:]+'\n')
f.close()
'''

