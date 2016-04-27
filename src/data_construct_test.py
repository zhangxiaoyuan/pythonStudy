#!usr/bin/env python
#coding=utf-8

print 'this file is test for python data construct!!!!'

list = ["p",'pp',"ppp", 1,123,232,"234"]

print list
print list[2]
print list[:5]
print list[2:]
print list[2:4]

del list[1]
print list
print list[1]

print len(list)

list1= [1,2,3,4,5,6]

print list+list1
print list * 5
print 2 in list1
for x in list1: print x
#下标从右向左是从-1开始
print list1[-1]
##表示从-3开始到结尾
print list[-3:]
##表示从开始到-3
print list[:-3]
print list[0]
print list[-6]
print list[0] == list[-6]

print "+++++++++++++++++++++++++"
list = [1,2,3,4,"5",0,123,1,23,22,14,67,90,89]
tuple = (4,5,6,'7')
#print list + tuple   # 只能同类型才可以相加

#function for list&tupl
list.sort()
print list

#元组，元组的其他用法和列表一样，只不过元组不能修改元素
tup = (1)  #元组只有一个元素时，需要在末尾添加逗号(,)，否则就会被默认为一个数字
tup1 = (1,)
print tup
print tup1

tup2= (1,2,3,)
tup3= (4,5,6,'7')
tup3 = tup2 + tup3
tup4 = tup2 + tup3
print tup2
print tup3
#i组不允许删除单个元素，但是可以删除整个元组rint tup4
#
#del tup2[0]
print tup2
