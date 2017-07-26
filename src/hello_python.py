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


#函数默认参数的坑
def add_end(L=[]):
	L.append("end")
	return L

l1 = [1,2,3]
l2 = [1, '2', "3"]
print(add_end(l1))
print(add_end(l2))

print(add_end())
print(add_end())
print(add_end())


def add_end1(L=None):
	if L is None:
		L = []
	else:
		L.append("end")

	return L

print(add_end1())
print(add_end1())
print(add_end1())

print(add_end1([1,2,3]))

#可变参数
def variable_var(*nums):
	sum = 0
	for num in nums:
		sum = sum + num * num
	return sum

l1=(1,2,3)
l2=[1,2,3]
print(variable_var(1,2,3))
#print(variable_var('1', '2', '3'))
print(variable_var(*(1,2,3)))
print(variable_var(*[1,2,3]))
print(variable_var(*l1))
print(variable_var(*l2))

#关键字参数
def key_val_func(name, age, **other):
	print("name:%s, age:%d" % (name, age))
	print("other ", other)
	print("name:", name, 'age:', age, 'other:', other)
	print("name:%s, age:%d, other:%s" % (name, age, other))

	return

print(key_val_func('abc', 90))
print(key_val_func('def', 80, gender='male', score=99))


#组合参数处理：
print('组合参数顺序：普通参数（位置参数）> 默认参数 > 可变参数 > 命名关键字参数 > 关键字参数')
def f1(a, b, c=0, *d, **e):
	print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'e=', e)

def f2(a, b, c=0, *, d, **e):
	print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'e=', e)

ll = [1,2,3]
print(f1(1,2))
print(f1(1,2,3))
print(f1(1, 2, c=3))
print(f1(1,2,3,*ll))
print(f1(1,2,3,(1,2,3)))
print(f1(1,2,3,[1,2,3],(4,5,6)))
print(f1(1,2,3,[1,2,3],(4,5,6),{'key':2, 'value':'456'}))
print(f1(1,2,3,[1,2,3],(4,5,6),{'key':2, 'value':'456'}, age=90, name='zhg', scoere=99))
print(f2(1, 2, d=99, ext=None))


#切片操作符Slice
print("切片操作sliece：")
listq = [1,4,5,6,7,8,9,0]
listp = range(0, 100, 5)
tupleq1 = (9,8,7,6,5,4,3,2,1)

print(listq[0:5])
print(listq[:7])
print(listq[1:5:2])
print(listp[-1])
print(list(listp[-5:-1]))
print(tupleq1[-3:])
print(tupleq1[-5:-1:2])
print(tupleq1[:6:3])
print(list(listp[::5]))
print(tupleq1[:])
print((1,2,3,4,5,6,7,8)[2:5:1])
print([9,8,7,6,5,4,3,2,1][-8::2])
print('abcdefghi'[::2])


print("迭代操作：")
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
	print(d[key])

for val in d.values():
	print(val)

for k,v in d.items():
	print('k=', k, ' v=', v)

for key in "ABCabc":
	print(list(d.values()))

print(d.values())
print(d.items())
print([k+" = "+str(v) for k,v in d.items()])

for idx, val in enumerate(['A' ,'B', 'c']):
	print(idx, " ",  val)


print("列表生成式：")
print(list(range(10)))
print(list(range(1,20,2)))

L = []
for x in range(11):
	L.append(x * x)

print(L)

print(list(x * x for x in range(11)))
print(list(x * x for x in range(11) if x %2 == 0))
print([m + n for m in "ABC" for n in "zxy"])
print([k+" = "+str(v) for k,v in d.items()])


import os
print([d for d in os.listdir('.')])
for d in os.listdir('.'):
	print([d])

L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])


def triangles(n):
	L = [1,]	
	while n > 0:
		yield L
		L = [1] + [] + [1]

print("生成器有两种方式：1.将列表生成式的[]改成()。2.")
g = (x*x for x in [1,2,3,4,5,6])

#print(g)
#print(next(g))
#print(next(g))

def print_generator():
	for x in g:
		print(x)

print_generator()

def fib(max):
	n, a, b = 0,0,1
	while n < max:
		print(b)
		a,b= b, a+b
		n = n+1
	return 'done'

print(fib(6))

def generator_fib(x):
	n , a, b = 0, 0 , 1
	while n < x:
		yield b
		a, b = b, a+b
		n = n+1
	return 'done'

print(generator_fib(6))
for n in generator_fib(6):
	print(n)

gg = generator_fib(6)
while True:
	try:
		x = next(gg)
		print(x)
	except StopIteration as e:
		print("return ", e.value)
		break

def test_gene():
	yield 1
	print("step1")
	print("step2")
	yield 'AC'
	print("step3")
	yield 5

for n in test_gene():
	print(n)


print("杨辉三角：")
from functools import reduce

def triangles():
	L =  [1]
	while True:
		yield L
		L = [L[0]] + [L[n] + L[n+1] for n, v in enumerate(L[0:len(L) - 1])] + [L[-1]]

'''
def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]
'''
n = 0
for x in triangles():
	print(x)
	n = n + 1
	if n == 10:
		break

print("高阶函数:")
def high_order_func(x,y,abs):
	return abs(x) + abs(y)

print(high_order_func(-1,-90,abs))
l1 = [1,2,3,4,5,6,7,8,9,10]
print(sum(l1))

print("map函数作用于序列中每一个单独元素，readuce函数将序列中每个元素产生关系")
def map_test(x):
	return x*x

print(list(map(map_test, l1)))
print(list(map(str, l1)))
print(list(map(float, l1)))

from functools import reduce
def reduce_test(x,y):
	return x*10+y
print(reduce(reduce_test, l1))

def fn(x,y):
	return x*10+y

def char2num(x):
	return {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]

print(reduce(fn, map(char2num, '99876543')))
print("字符串数字转化成整数")
def str2num(a):
	def fun(x,y):
		return x *10+y
	
		
	return reduce(fun, map(char2num, a))	

print(str2num('998768644'))
print(int("123456789"))

print("输入字符串的第一个字母转换为大写")
L1 = ['adam', 'LISA', 'barT']
def first_2_upper(x):
	return x[0].upper()+x[1:].lower()

print(list(map(first_2_upper, L1)))

L2 = [3,5,7,9]
def prod(x,y):
	return x*y
print(reduce(prod, L2))

'''
def str2float(s):
	def fun1(x,y)
		return x*10+y
	def char2num(x):
		if for m in x if x[m] =='.':
			yield
		return {'0':0, '1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[x]
	def add(x,y):
		x+y
	return reduce(fun1, map(char2num, s))
'''


print("将字符串转换为浮点数：")
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str_to_float(s):
	nums = map(lambda ch:CHAR_TO_FLOAT[ch], s)
	point = 0
	def to_float(f, n):
		nonlocal point
		if n == -1:
			point = 1
			return f
		if  point == 0:
			return f* 10 + n
		else:
			point = point * 10
			return f+n/point

	return reduce(to_float, nums, 0.0)

print(str_to_float('123.456'))
print(str_to_float('.456'))


print('filter函数：')
def is_odd(n):
	return n %  2 == 1

print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9])))


print('筛选素数：')
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x : x % n > 0

def primies():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

for n in primies():
	if n < 20:
		print(n)
	else:
		break

print(next(_odd_iter()))

print("计算回数：")

lk = [1,2,3,4,5]
print(lk[::-1])
def is_palindrome1(x):
	l = list(str(x))
	for n,v in enumerate(l):
		if l[n] == l[len(l) - n - 1]:
			continue
		else:
			return

	return x

def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

print("排序函数sorted:")
print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21], key=abs))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

L2 = sorted(L, key=by_name)
print(L2)
print(sorted(L, key=by_name, reverse=True))
print(sorted(L, key=by_score, reverse=True))

print("函数作为返回值：")
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
        	#print(n)
            ax = ax + n
        return ax
    return sum()

print(lazy_sum(1,2,32,3,4,5,6))
f = lazy_sum(1,2,32,3,4,5,6)
print(f)
#print(f())

args = [1,2,3,3,43,4,5]
for x in args:
	print(x)

print('闭包特性：牢记：函数只是被创建，但是没有执行，只有在调用时才执行')
def count():
	fs = []
	for i in range(1,4):
		def abc():
			return i * i

		fs.append(abc)
	return fs

f1,f2,f3 = count()
print(count())
print(f1())
print(f2())
print(f3())


def count():
	fs = []
	for i in range(1,4):
		def abc(j):
			return j * j

		fs.append(abc(i))
	return fs

#f1,f2,f3 = count()
#print(f1())
#print(f2())
#print(f3())
f = count()
print(f)

def count():
	fs = []
	for n in range(1,4):
		def a(i):
			def b():
				return i * i
			return b
		fs.append(a(n))

	return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

print("匿名函数lambda:")
print(list(map(lambda x: x*x*x, [1,2,3,4,5,6,7,8])))

print("装饰器：")
def now():
	print("time:2017-07-26")
import functools

f = now
f()
print(f.__name__)

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print("call %s()" % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def printData(a, b, c):
	print('data: 2017-07-26 ', a, b, c)

f = printData
f(1,2,3)
print(f.__name__)

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print("%s %s()" % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log("execute")
def printData(a, b, c):
	print('data: 2017-07-26 ', a, b, c)

f = printData
f(2,3,4)
print(f.__name__)
print(log.__name__)
#print(decorator.__name__)
