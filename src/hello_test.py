#!/usr/bin/env python
# coding=UTF-8

'''
#这是注释：
#!/usr/bin/evn python 这个写法好一些，没有直接指定解释器路径，
#!/usr/bin/python 这个是硬编码指定了解释器路径
'''

print "hello world, hello python, 你好，世界"

if 0:
	print ("true");
else:
	#\表示连接符，和C语言相同，(){}[]中的语句就不需要使用\
	print ("1+\
	2+\
	3")

days = ["monday", "Tuesday", "wensday", \
		"Thursday", \
		"Friday", "Sunday"]


#文本语句定义
word = 'word'
sentense = "zhe shi yi ge ju zi"
paragraph = """ 这个是一个段落
    包含两行的语句
	"""
anotherParagraph = '''这是单引号的段落，
	也包括两行语句'''

print word
print sentense
print paragraph
print anotherParagraph;

#转义字符
raw_input("\n\ninput enter prss to exit");

#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
word1=1;word2=2;word3=3;print word2;


#像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
if "suit":
	print "suit"
elif 'suit1':
	print 'suit1'
else:
	print "suit3"

#弱类型语言，没有变量类型，根据赋值进行内存分配，每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
number = 226310 #整形
weight = 80     #整形字符串
height = 179.5  #浮点型
name = "zhangxiaoyan" #
a = b = c = 1
a1,b1,c1 = 1,2,'3'

print number; print weight
print height
print name
print a, b, c;
print a1,b1,c1



#Numbers nu = 100
#print nu


#数据类型
var = 1
var2 = 2
print var, var2
var = 3
print var
#长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型
var = 1000L
print var
var = 100.01
print var

string = '123456'
print string
#用：取值，包含左边界值，但是不包含右边界值，包括string[0],不包括string[2]
print string[0:2]
print string[2:-1] #从右向左读取最后一个表示为-1

string1 = "hello world"
print string1
print string1[0]
print string1[2:5]
print string1[2:]   #表示从第几个下标开始到结束
print string1 * 2   #*表示重复动作几次
print string1[0:2] * 2  
print string1 + 'test'   #表示字符串连接
print string1[2:5] + "test"


#python List
#列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list # 输出完整列表
print list[0] # 输出列表的第一个元素
print list[1:3] # 输出第二个至第三个的元素 
print list[2:] # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2 # 输出列表两次
print list + tinylist # 打印组合的列表
list[1]= '13abc'

print list


#python tuple
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple # 输出完整元组
print tuple[0] # 输出元组的第一个元素
print tuple[1:3] # 输出第二个至第三个的元素 
print tuple[2:] # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2 # 输出元组两次
print tuple + tinytuple # 打印组合的元组

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]

#tuple[2] = 1000 # 元组中是非法应用
list[2] = 1000 # 列表中是合法应用

print tuple
print list



#python元字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one'] # 输出键为'one' 的值
print dict[2] # 输出键为 2 的值
print tinydict # 输出完整的字典
print tinydict.keys() # 输出所有键
print tinydict.values() # 输出所有值


#类型转换
x= "123"
b = int(x)
print b
c = long(x)
print c
d = float(x)
print d
e = complex(x)
print e
f = str(e)
print f
g = repr(x)  #转换为表达式字符串
print g
h = eval(g)  #用来计算在字符串中的有效Python表达式,并返回一个对象
print h

