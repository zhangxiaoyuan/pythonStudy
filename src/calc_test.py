#!var/bin/env python
#coding=utf-8

a = 4
b = 5
print a**b  #幂 - 返回x的y次幂

c = 9.0
d = 2.0
print c/d
print c//d   #取整除 - 返回商的整数部分
print (c==d)
print (c!=d)
print (c<>d)  #不等于 - 比较两个对象是否不相等,这个运算符类似 != 。

a = 60
b = 1
print a^b  #异或操作，同一位上相同返回0，不同返回


#python逻辑运算符(and or not)
a = 20
b = 10
if ( a and b ):
	print "1 - 变量 a 和 b 都为 true"
else:
	print "1 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
	print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
	print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if ( a and b ):	  
	print "3 - 变量 a 和 b 都为 true"
else:
	print "3 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
	print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
	print "4 - 变量 a 和 b 都不为 true"

if not( a and b ):
	print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
	print "5 - 变量 a 和 b 都为 true"


#python成员运算符(in not in)
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
	print "1 - 变量 a 在给定的列表中 list 中"
else:
	print "1 - 变量 a 不在给定的列表中 list 中"

if ( b not in list ):
	print "2 - 变量 b 不在给定的列表中 list 中"
else:
	print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if ( a in list ):
	print "3 - 变量 a 在给定的列表中 list 中"
else:
	print "3 - 变量 a 不在给定的列表中 list 中"


#python身份运算符(is is not) //x is y, 如果 id(x) 等于 id(y) , is 返回结果 1
a = 10
b = 20
if (a is b):
	print "a is b"
else:
	print 'a is not b'

if (id(a) == id(b)):
	print 'id(x) is id(b)'
else:
	print "id(x) is not id(b) "

if (a is not b):
	print "a is not b"
else:
	print 'a is b'
	

#运算符优先级
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print "(a + b) * c / d 运算结果为：",  e

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print "((a + b) * c) / d 运算结果为：",  e

e = (a + b) * (c / d);    # (30) * (15/5)
print "(a + b) * (c / d) 运算结果为：",  e

e = a + (b * c) / d;      #  20 + (150/5)
print "a + (b * c) / d 运算结果为：",  e
