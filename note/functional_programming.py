#Python中的除了map和reduce外，还有一些别的如filter, find, all, any的函数做辅助（其它函数式的语言也有），可以让你的代码更简洁，更易读

print '过程式编程：'
nums = [2, -5, 9, 7, -2, 5, 3, 1, 0, -3, 8]

positive_cnt = 0
positive_sum = 0;

for i in range(len(nums)):
    if nums[i] > 0:
        positive_cnt += 1
        positive_sum += nums[i]

if positive_cnt > 0:
    print positive_sum / positive_cnt
else:
    print"error"

print '函数式编程:'
positive_nums = filter(lambda x: x > 0, nums)
print reduce(lambda x,y:x+y, positive_nums) / len(positive_nums)


#过程式编程
print '过程式编程:'
from random import random

time = 5
car_pos=[1,1,1]

while time:
    time -= 1

    print 5 - time 

    for i in range(len(car_pos)):
        if random() > 0.3:
            car_pos[i] += 1;
        
        print '-'*car_pos[i]
             


#过程式编程封装:
#些函数间必需知道其它函数是怎么修改它们之间的共享变量的，所以，这些函数是有状态的。
print '过程式编程封装:'
def move_cars():
    for i, _ in enumerate(car_positions):
        if random() > 0.3:
            car_positions[i] += 1
 
def draw_car(car_position):
    print '-' * car_position
 
def run_step_of_race():
    global time
    time -= 1
    move_cars()
 
def draw():
    print 5 - time
    for car_position in car_positions:
        draw_car(car_position)
 
time = 5
car_positions = [1, 1, 1]
 
while time:
    run_step_of_race()
    draw()


#函数式编程：
print '函数式编程Functional Programming：'
def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions)
 
def output_car(car_position):
    return '-' * car_position
 
def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}
 
def draw(state):
    print 5 - state['time']
    print '\n'.join(map(output_car, state['car_positions']))
 
def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 4,
      'car_positions': [1, 1, 1]})

#上面的代码依然把程序的逻辑分成了函数，不过这些函数都是functional的。因为它们有三个症状：
# 1）它们之间没有共享的变量。
# 2）函数间通过参数和返回值来传递数据。
# 3）在函数里没有临时变量。
# 4）我们还可以看到，for循环被递归取代了（见race函数）—— 递归是函数式编程中带用到的技术，正如前面所说的，递归的本质就是描述问题是什么
 
#pipeline:
#正常的普通函数编写：
def process(num):
    # filter out non-evens
    if num % 2 != 0:
        return
    num = num * 3
    num = 'The Number: %s' % num
    return num

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    print process(num)

# 输出：
# The Number: 6
# The Number: 12
# The Number: 18
# The Number: 24
# The Number: 30

#使用pipeline方式编写：
def even_filter(nums):
    for num in nums:
        if num % 2 == 0:
            yield num
def multiply_by_three(nums):
    for num in nums:
        yield num * 3
def convert_to_string(nums):
    for num in nums:
        yield 'The Number: %s' % num

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string(multiply_by_three(even_filter(nums)))
for num in pipeline:
    print num
    
#我们动用了Python的关键字 yield，这个关键字主要是返回一个Generator，yield 是一个类似 return 的关键字，
#只是这个函数返回的是个Generator-生成器。所谓生成器的意思是，yield返回的是一个可迭代的对象，并没有真正的执行函数。
#也就是说，只有其返回的迭代对象被真正迭代时，yield函数才会正真的运行，运行到yield语句时就会停住，然后等下一次的迭代。
#（这个是个比较诡异的关键字）这就是lazy evluation

#使用Map & Reduce，不要使用循环
def even_filter(nums):
    return filter(lambda x: x%2==0, nums)

def multiply_by_three(nums):
    return map(lambda x: x*3, nums)

def convert_to_string(nums):
    return map(lambda x: 'The Number: %s' % x,  nums)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pipeline = convert_to_string(
               multiply_by_three(
                   even_filter(nums)
               )
            )
for num in pipeline:
    print num

#但是他们的代码需要嵌套使用函数，这个有点不爽，如果我们能像下面这个样子就好了。

pipeline_func(nums, [even_filter,
                     multiply_by_three,
                     convert_to_string])

#那么，pipeline_func 实现如下：

def pipeline_func(data, fns):
    return reduce(lambda a, x: x(a),
                  fns,
                  data)
