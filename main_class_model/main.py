#coding:utf-8
import re #正则表达式
import fileinput
'''
测试/使用说明:
请将新的测试数据,使用文本的形式存放在test-data文件夹下,同时修改代码末文件读取的路径
'''

class RomanNum(object):

    def getRomanNum(self,RomanStr):
        '''
        输入罗马数字字符串，输出转换后的阿拉伯字符串
        逻辑说明:原本是使用所有规则一个个if来判断处理的,但是这样的代码非常垃圾,学习后改进.
        使用正则的类似思想,对输入串判断romanpattern中规则出现的情况,
        例如以MXCVI为例,则在pattern的结果是:^M{1}C{0}XCX{0}VI{1} 1000+90+6这里就可以按照千百十分位来分别判断处理
        其中retnum则是存放转化后的阿拉伯数字,用于返回.
        '''
        #正则表达式进行匹配,判断输入是否合法
        if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',RomanStr)!=None:
            NumDic = {"pattern":"","retNum":0}#值记录区
            # 如测试数为 XCVI 则最后retNum 96 pattern ^M{0}C{0}XCX{0}VI{1} 展示出现数次
            RomanPattern = {
                "0":('','','','M'),             #          1000
                "1":('CM','CD','D','C',100), #900 400 500 100
                "2":('XC','XL','L','X',10), #90 40 50 10
                "3":('IX','IV','V','I',1)#9 4 5 1
                }
            i = 3
            NumItems = sorted(RomanPattern.items())#对字典先排序返回元组

            for RomanItem in NumItems:
                if RomanItem[0] != '0':#先统计千内的
                    patstr = NumDic["pattern"].join(['',RomanItem[1][0]])
                    #print "R "+RomanItem[1][0]
                    if re.search(patstr,RomanStr) != None:#先判断Romanstr中是否存在parstr
                        NumDic["retNum"] += 9*RomanItem[1][4] # +=90
                        NumDic["pattern"] = patstr #存放正则信息
                    else:
                        patstr = NumDic["pattern"].join(['',RomanItem[1][1]])
                        #print patstr
                        if re.search(patstr,RomanStr) != None:
                            NumDic["retNum"] += 4*RomanItem[1][4] #+=40
                            NumDic["pattern"] = patstr
                        else:
                            patstr = NumDic["pattern"].join(['',RomanItem[1][2]])
                            if re.search(patstr,RomanStr) != None:
                                NumDic["retNum"] += 5*RomanItem[1][4] # += 50
                                NumDic["pattern"] = patstr
                # test
                #print "retNum " + str(NumDic["retNum"]) ,
                #print "pattern " +NumDic["pattern"]

                if NumDic["pattern"] == '':
                    NumDic["pattern"] = '^'#标志
                tempstr = ''
                sum = 0
                for k in range(0,4):#处理连续出现几次
                    pstr = RomanItem[1][3].join(['','{']).join(['',str(k)]).join(['','}'])
                    patstr = NumDic["pattern"].join(['',pstr])
                    if re.search(patstr,RomanStr) != None:
                        sum = k*(10**i)
                        tempstr = patstr
                if tempstr <> '':#不等于即依旧为原始值
                    NumDic["pattern"] = tempstr
                else:
                    NumDic["pattern"] = patstr
                NumDic['retNum'] += sum
                i -= 1

            return NumDic['retNum']
            #return NumDic['pattern']
        else:
            print 'String is not a valid Roman numerals'

    def str_Resolve(self,input_line):
        '''
        输入每一行的字符串类型信息:如题目中的测试数据.返回分类机处理后的信息.

        程序代码说明:
        结构很明显,按照末尾字符是否在Romanarray中,判断是否是第一类定义单词输入
        否则判断是否以小写s结束,判断是否是作为第二类金币银币类型输入
        否则判断末尾是否是?号为第三类输入.进行按照空格划分之后判断第二个单词
        按照many和mach进行分别返回处理
        '''
        Romanarray=['I','V','X','L','C','D','M']
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

            temp_num =  self.getRomanNum(temp_str)
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

                return temp_str3+"is "+str(self.getRomanNum(temp_str1))#转化成数字并且输出


            elif input_line_array[1] == 'many':#处理ｍａｎｙ
                temp_str2 = ''
                temp_str4 = ''
                for i in range(4,len(input_line_array)-2):#取第５个到倒数第三个之间
                    temp_str4 += input_line_array[i]+' '
                    temp_str2 += word_dic[input_line_array[i]]#转化为字符进行ｒｏｍａ查询

                return temp_str4+input_line_array[-2]+' is '+ str(coin_dic[input_line_array[-2]]*self.getRomanNum(temp_str2) )+ ' Credits'#输出数量＊单位价值

if __name__ == "__main__" :

    #全局性变量
    word_dic = {}#以字典来对应单词和罗马数字
    coin_dic = {}#以字典来对应货币和价值

    for line in fileinput.input("../test-data/input_1.txt"):
        str_line=line[:-1]#去除行结尾的换行符号,未知为何会多出一个换行
        try:
            Roma = RomanNum()
            str_return = Roma.str_Resolve(str_line)
            if str_return:
                print str_return
        except:
            print "I have no idea what you are talking about"
