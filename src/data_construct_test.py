
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
