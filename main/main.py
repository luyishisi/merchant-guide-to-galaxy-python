#coding:utf-8
from str_Resolve import *
import fileinput

for line in fileinput.input("../test-data/input_1.txt"):
    str_line=line[:-1]
    #print str_line
    str_return = str_Resolve(str_line)
    if str_return:
        print str_return
