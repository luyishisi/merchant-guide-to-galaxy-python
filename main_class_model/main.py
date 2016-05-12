#-*- coding: utf-8 -*-
import re #正则表达式
import fileinput
# Description : 测试/使用说明:
#
# Input : 请将新的测试数据使用txt存放在test-data文件夹下,同时修改代码末文件读取的路径
#
# Output : 测试结果
class RomanNum(object):

    def get_roman_num(self, RomanStr):
        # Description : 使用正则的类似思想,对输入串判断romanpattern中规则出现的情况,
        #               例如以MXCVI为例,则在pattern的结果是:^M{1}C{0}XCX{0}VI{1}
        #               1000+90+6这里就可以按照千百十分位来分别判断处理
        #               其中retnum则是存放转化后的阿拉伯数字,用于返回.
        #
        # Input :罗马数字字符串
        #
        # Output : 等价的阿拉伯字符串
        if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'\
        , RomanStr) != None:
            NumDic = {"pattern":"", "retNum":0}#数值存储区
            RomanPattern = {
                "0":('', '', '', 'M'),             #          1000
                "1":('CM', 'CD', 'D', 'C', 100), #900 400 500 100
                "2":('XC', 'XL', 'L', 'X', 10), #90 40 50 10
                "3":('IX', 'IV', 'V', 'I', 1)#9 4 5 1
                }
            i = 3
            NumItems = sorted(RomanPattern.items())#对字典先排序返回元组

            for RomanItem in NumItems:
                if RomanItem[0] != '0':#先统计千内的
                    PatStr = NumDic["pattern"].join(['', RomanItem[1][0]])
                    if re.search(PatStr, RomanStr) != None:
                        #先判断Romanstr中是否存在parstr
                        NumDic["retNum"] += 9*RomanItem[1][4] # +=90
                        NumDic["pattern"] = PatStr
                    else:
                        PatStr = NumDic["pattern"].join(['', RomanItem[1][1]])
                        if re.search(PatStr, RomanStr) != None:
                            NumDic["retNum"] += 4*RomanItem[1][4]
                            NumDic["pattern"] = PatStr
                        else:
                            PatStr = NumDic["pattern"].\
                            join(['', RomanItem[1][2]])
                            if re.search(PatStr, RomanStr) != None:
                                NumDic["retNum"] += 5*RomanItem[1][4]
                                NumDic["pattern"] = PatStr

                if NumDic["pattern"] == '':
                    NumDic["pattern"] = '^'#标志
                TempStr = ''
                Sum = 0
                for k in range(0, 4):#处理连续出现几次
                    pstr = RomanItem[1][3].\
                    join(['', '{']).join(['', str(k)]).join(['', '}'])
                    PatStr = NumDic["pattern"].join(['', pstr])
                    if re.search(PatStr, RomanStr) != None:
                        Sum = k*(10**i)
                        TempStr = PatStr
                if TempStr != '':
                    NumDic["pattern"] = TempStr
                else:
                    NumDic["pattern"] = PatStr
                NumDic['retNum'] += Sum
                i -= 1

            return NumDic['retNum']
        else:
            print 'String is not a valid Roman numerals'

    def str_resolve(self, InputLine):
        # Description : 按照输入中的未字母,尾问号,以及much,many来做分类
        #
        # Input :测试数据
        #
        # Output : 分类机处理后的信息.
        RomanArray = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        if InputLine[-1] in RomanArray:
            InputLine_array = InputLine.split(' ')#以空格截取
            WordDic[InputLine_array[0]] = InputLine_array[2]#取第一个和最后一个元素
            return
        elif InputLine[-1] == 's':#以小写ｓ做为金币银币那些测试数据的识别符号
            InputLine_array = InputLine.split(' ')
            TempStr = ''
            for i in range(len(InputLine_array)-4):
                TempStr += WordDic[InputLine_array[i]]
            TempNum = self.get_roman_num(TempStr)
            CoinDic[InputLine_array[-4]] = \
            int(InputLine_array[-2])/int(TempNum)
            return
        elif InputLine[-1] == '?': #以?为标志,判断是否是第三四类输入
            InputLine_array = InputLine.split(' ')
            if InputLine_array[1] == 'much':
                TempStr1 = ''
                TempStr3 = ''
                for i in range(3, len(InputLine_array)-1):#抽取第四个到最后一个数组元素
                    TempStr3 += InputLine_array[i]+' '
                    TempStr1 += WordDic[InputLine_array[i]]
                return TempStr3+"is "+str(self.get_roman_num(TempStr1))
            elif InputLine_array[1] == 'many':
                TempStr2 = ''
                TempStr4 = ''
                for i in range(4, len(InputLine_array)-2):#取第５个到倒数第三个之间
                    TempStr4 += InputLine_array[i]+' '
                    TempStr2 += WordDic[InputLine_array[i]]
                return TempStr4+InputLine_array[-2]+' is '\
                + str(CoinDic[InputLine_array[-2]]*\
                self.get_roman_num(TempStr2)) + ' Credits'

if __name__ == "__main__":

    WordDic = {}#以字典来对应单词和罗马数字
    CoinDic = {}#以字典来对应货币和价值

    for Line in fileinput.input("../test-data/input_3.txt"):
        StrLine = Line[:-1]#去除行结尾的换行符号,未知为何会多出一个换行
        try:
            Roma = RomanNum()
            str_return = Roma.str_resolve(StrLine)
            if str_return:
                print str_return
        except:
            print "I have no idea what you are talking about"
