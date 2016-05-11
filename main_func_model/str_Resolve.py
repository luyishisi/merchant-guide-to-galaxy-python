#coding:utf-8
from Roma_to_num_test import getRomanNum

Romanarray=['I','V','X','L','C','D','M']

word_dic = {}#以字典来对应单词和罗马数字
coin_dic = {}#以字典来对应货币和价值

def str_Resolve(input_line):
    '''
    输入每一行的字符串类型信息:如题目中的测试数据.返回分类机处理后的信息.

    程序代码说明:
    结构很明显,按照末尾字符是否在Romanarray中,判断是否是第一类定义单词输入
    否则判断是否以小写s结束,判断是否是作为第二类金币银币类型输入
    否则判断末尾是否是?号为第三类输入.进行按照空格划分之后判断第二个单词
    按照many和mach进行分别返回处理
    '''
    if input_line[-1] in Romanarray:
        input_line_array = input_line.split(' ')#以空格截取
        word_dic[input_line_array[0]] = input_line_array[2]#取第一个和最后一个元素
        return
    #print 'word_dic:',word_dic:

    elif input_line[-1] == 's':#以小写ｓ做为金币银币那些测试数据的识别符号
        input_line_array = input_line.split(' ')#以空格截取

        temp_str = ''
        for i in range(len(input_line_array)-4):
            temp_str += word_dic[input_line_array[i]]

        temp_num =  getRomanNum(temp_str)
        #print "input_line_array[-4]",input_line_array[-4]
        coin_dic[input_line_array[-4]] = int(input_line_array[-2])/int(temp_num)
        return
    #print 'coin_dic:',coin_dic

    elif input_line[-1] == '?': #以?为标志,判断是否是第三四类输入
        input_line_array = input_line.split(' ')
        #print "input_line_array:",input_line_array

        if input_line_array[1] == 'much':
            temp_str1 = ''
            temp_str3 = ''
            for i in range(3,len(input_line_array)-1):#抽取第四个到最后一个数组元素
                temp_str3 += input_line_array[i]+' '
                temp_str1 += word_dic[input_line_array[i]]

            return temp_str3+"is "+str(getRomanNum(temp_str1))#转化成数字并且输出


        elif input_line_array[1] == 'many':#处理ｍａｎｙ
            temp_str2 = ''
            temp_str4 = ''
            for i in range(4,len(input_line_array)-2):#取第５个到倒数第三个之间
                temp_str4 += input_line_array[i]+' '
                temp_str2 += word_dic[input_line_array[i]]#转化为字符进行ｒｏｍａ查询

            return temp_str4+input_line_array[-2]+' is '+ str(coin_dic[input_line_array[-2]]*getRomanNum(temp_str2) )+ ' Credits'#输出数量＊单位价值
