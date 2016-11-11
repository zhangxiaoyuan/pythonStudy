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
