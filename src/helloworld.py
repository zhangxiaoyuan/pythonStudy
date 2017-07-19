#！/usr/bin/env python3
# -*- coding: utf-8 -*-

#上两行注释意思：
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码

print('hello world')
print(100+200)

#print()函数
print("hello world")
#print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出,,会依次打印每个字符串，遇到逗号“,”会输出一个空格
print("hello", "world")
#print()可以打印整数和计算结果
print(100)
print(200-800)
print(20*89)
#多行字符串输入：
print('''abc
efg
hig''')

#input()函数，用户输入字符串保存到一个变量中,
#input()函数输入的都是字符串
#name = input()
#firstname = input("input first name:")
#print('hello', firstname)


#布尔值
print(True)
print(False)
print(1>2)
print(1<2)
print(True and False)
print(True or False)
print(False or True)
print(not False)

#age = input('age:')
#if age > '18':
#	print('成年')
#else:
#	print('未成年')


#python中同一变量可以反复赋值，而且可以是不同的数据类型
#这种变量本身类型不固定的语言称之为动态语言
a = 100
print(a)
a = "abc"
print(a)
a = False
print(a)

#两种除法表示法：
print('10/3=', 10/3)
print('10//3=', 10//3)

s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(s3)
print(s4)

#python字符串编码格式采用Unicode：
#ord()函数将字符转换为Unicode编码，chr()函数将Unicode编码转化为字符
print(ord('A'))
print(ord("a"))
print(ord("中"))
print(ord("国"))
print(chr(ord('A')))
print(chr(ord("国")))

a = 'hello %s' % 'abc'
b = 'hi %s, you have %d money' % ('mic', 100000)
c = '%f, %.2f, %2d-%02d' % (3.1415923, 3.1415, 1, 10)
d = "grouth rate: %d %%" % (70)
print(a)
print(b)
print(c)
print(d)

s1 = 72
s2 = 85
rate = "%.1f %%" % ((85-72)/72 * 100)
print("score from %d increase to %d, rate is %s" % (s1, s2, rate))

#list集合
listq = ['abc', 'def', "ghi"]
print(listq)
print('len=%d' % (len(listq)))
print(listq[0], listq[2])
print(listq[-1])

#list有序表的相关操作
print("list opertion:")
listq.append("jkl")
print(listq)
listq.insert(1, "000")
print(listq)
listq.pop()
print(listq)
listq.pop(0)
print(listq)
listq[0] = "aaa"
print(listq)
listq[1] =345
listq[2] = False
print(listq)

#list的二维表
listp = [123, True, 'abc', listq]
print(listp)
print(listp[0], listp[3][2])
listp = []
print(listp)

#tuple固定元素的list，没有相关操作，初始化之后就不能改变元素值
tuplep = (123, False, "abc", [1, True, 'def'])
print(tuplep)
tuplea = ()
print(tuplea)
#只有一个元素的tuple定义时必须添加一个，
tupleb = (1, )
print(tupleb)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])


#判断语句
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


#循环操作：
print("循环操作:")
names = ['abc', 'def', 'ghi']
for name in names:
	print(name)

#range()函数可以生成一个整数序列
print(list(range(5)))
print(tuple(range(10)))
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print("hello %s" % name)

i = 0
while i < len(L):
	print("hello %s" % L[i])
	i = i + 1

#dictionary字典处理
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
#要避免key不存在的错误，有两种办法，
#一是通过in判断key是否存在：
print('Thomas' in d)
#二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))
d.pop('Bob')
print(d)

#set处理，自动剔除重复值
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
s.add(4)
s.add(5)
print(s)
s.remove(1)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set((2, 3, 4, 5))
print(s1 & s2)
print(s1 | s2)

n1 = 255
n2 = 1000
print(hex(n1))
n3 = hex(n2)
print(n3)

#函数定义
print("函数定义：")
def calc_abs(x):
	if x > 0:
		return x
	else:
		return -x


#空函数
def calc_empyt():
	pass

import math
#返回多个值的函数
def return_more_val(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)

	return nx, ny


print(calc_abs(1))
print(calc_abs(-10))

nx, ny = return_more_val(100, 100, 60, math.pi / 6)
print(nx, ny)

realTuple = return_more_val(100, 100, 60, math.pi / 6)
print(realTuple)
