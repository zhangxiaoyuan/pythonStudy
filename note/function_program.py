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
