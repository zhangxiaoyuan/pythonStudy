#!usr/bin/python
#coding=utf-8


#while...else
count = 0
while count < 5:
	print 'count=', count
	count += 1
else:
	print count, 'more than 5'

count =0
while count < 5:
	print 'count=', count
	count +=1
	if count ==3:
		break;
else:
	print count ,'more than 5'

print 'if break can not execute else'

#for & for...else

i = 0
for word in 'python':
	print 'word ',i,word
	i +=1

list = ['123','abc', 12, 14, 15]
for ele in list:
	print "ele : ", ele

tuple= ('apple', "pear", 'banana')
for index in range(len(tuple)):
	print 'fruit is ', tuple[index]
for index in range(0,3):
	print "fuint :", tuple[index]

#for...else
for i in range(10,20):
	for j in range(2, i):
		if (i % j == 0):
			x = i /j
			print "%d = %d * %d," % (i,j,x)
			break;
	else:
		print i, 'is zhishu'


#pass unvaluable,just for fill ,empty sentense
for i in range(0, 3):
	if i == 2:
		pass
		print 'just pass sentense,empty.unvaluable'
	print 'value=', i


ivar1=10
var2 = 20;
print 'va = ', ivar1,var2
del ivar1
del var2
#print 'val = ', ivar1,var2   #wrong sentense, 2 para undefined


#random function
import random
fruit = ['apple','pear','banana','grape','mango',"xigua"]
print 'fruit : ', random.choice(fruit)

print 'a num in 100 adn 10000: ', random.randrange(5,10, 5)


str = 'hello world'
print str[0], str[1:5]
