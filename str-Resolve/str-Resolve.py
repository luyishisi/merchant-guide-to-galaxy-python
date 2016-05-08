
#
'''

'''
Romanarray=['I','V','X','L','C','D','M']
#print Romanarray

input_line ='prok is V'

word_dic = {}#以字典来对应单词和罗马数字

if input_line[-1] in Romanarray:
    input_line_array = input_line.split(' ')#以空格截取
    word_dic[input_line_array[0]] = input_line_array[2]#取第一个和最后一个元素
    print word_dic
