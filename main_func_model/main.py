#coding:utf-8
from str_Resolve import *
import fileinput
'''
测试/使用说明:
请将新的测试数据,使用文本的形式存放在test-data文件夹下,同时修改文件读取的路径
'''

for line in fileinput.input("../test-data/input_3.txt"):
    str_line=line[:-1]#去除行结尾的换行符号,未知为何会多出一个换行
    #print str_line
    try:
        str_return = str_Resolve(str_line)
        if str_return:
            print str_return
    except:
        print "I have no idea what you are talking about"
