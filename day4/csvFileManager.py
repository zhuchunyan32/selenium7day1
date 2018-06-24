#1.要想读取csv文件,首先要导入csv代码库
#这个csv不用下载,是python内置的代码库
#如果要读取excel需要下载响应的代码库:xlrd
#怎么下载:1.通过命令下载:在dos窗口中,输入pip install -U xlrd
#selenium的离线包,也可以通过命令行在线安装
#pip install -U selenium
#-U是升级到最新版的意思
#pip是python语言最常用的项目管理工具,和java中的maven类似
#如果你又安装python2,同时安装python3,可能需要把pip改成pip3
#2.点击File->点击settings->project下面的interpreter->+-->搜索选中xlrd并安装

import csv
#指定要读取文件的路径
path='D:/zhuchunyan/selenium7day/data/testdata.csv'
#因为字符串中包含反斜线\t,怎么办
#1.每个\前面加一个\斜线, 2.把每个反斜线都改成正斜线/
#因为java和python都是跨平台语言,在字符串中两个反斜线会根据转义字符的规则自动转成一个反斜线
#在windows操作系统中,用反斜线表示目录结果
#但是在linux系统中,只有正斜线/才能表示目录,用双反斜线就失去了跨平台的能力,linux用不了
#如果用正斜线,代码同时可以在linux和window中执行
#3.在字符串外面加上字母r,会认为中间所有的字符串不存在转义字符
#如果用双反斜线
print(path)
#3.打开路径所对应的文件
file=open(path,'r')
#4.读取文件的内容,通过什么来读取?我们是不是导入了csv代码库,还一直没用
#reader()方法是专门用来读取文件的
data_table=csv.reader(file)
#5.打印data_table中的每一行数据,循环
#for是循环的关键字,item代表每一行,每循环一次,item就代表最新的一行数据
#data_table表示整个文件中的所有数据

for item in data_table:
    print(item)
    #这样就成功读出所有数据了
    #很多的测试用例可能都需要从excel中读取数据,所以应该对这些代码做一个简单封装,建一个文件叫csvFileManager2
    #把以上代码封装到一个方法中,并且再建一个文件来读取封装好的方法