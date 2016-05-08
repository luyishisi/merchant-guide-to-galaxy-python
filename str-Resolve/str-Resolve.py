#coding:utf-8
import fileinput
from Roma_to_num_test import getRomanNum
Romanarray=['I','V','X','L','C','D','M']
#print Romanarray

input_line ='glob glob Silver is 34 Credits'

word_dic = {}#以字典来对应单词和罗马数字
coin_dic = {}#以字典来对应货币和价值

#input_line = 'glob is I'

def str_Resolve(input_line):
    #print input_line[-1]
    if input_line[-1] in Romanarray:
        input_line_array = input_line.split(' ')#以空格截取
        word_dic[input_line_array[0]] = input_line_array[2]#取第一个和最后一个元素

    print 'word_dic:',word_dic

    if input_line[-1] == 's':#以小写ｓ做为金币银币那些测试数据的识别符号
        input_line_array = input_line.split(' ')#以空格截取

        temp_str = ''
        for i in range(len(input_line_array)-4):
            temp_str += word_dic[input_line_array[i]]

        temp_num =  getRomanNum(temp_str)
        print "input_line_array[-4]",input_line_array[-4]
        coin_dic[input_line_array[-4]] = int(input_line_array[-2])/int(temp_num)

    print 'coin_dic:',coin_dic

    #input_line = 'how many Credits is glob glob Silver ?'

    if input_line[-1] == '?':
        #print "yes"
        input_line_array = input_line.split(' ')
        print "input_line_array:",input_line_array

        if input_line_array[1] == 'much':
            temp_str1 = ''
            for i in range(3,len(input_line_array)-1):#抽取第四个到最后一个数组元素
                print input_line_array[i],
                temp_str1 += word_dic[input_line_array[i]]
            print "getRomanNum:",getRomanNum(temp_str1) #转化成数字

        elif input_line_array[1] == 'many':#处理ｍａｎｙ
            temp_str2 = ''
            for i in range(4,len(input_line_array)-2):#取第５个到倒数第三个之间
                print input_line_array[i],
                temp_str2 += word_dic[input_line_array[i]]#转化为字符进行ｒｏｍａ查询
            #print temp_str2
            print "end",coin_dic[input_line_array[-2]]*getRomanNum(temp_str2)#输出数量＊单位价值


for line in fileinput.input("../test-data/input.txt"):
    str_line=line[:-1]
    print str_line
    str_Resolve(str_line)
