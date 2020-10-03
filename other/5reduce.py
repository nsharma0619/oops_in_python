from functools import reduce

nums = [4,2,3,5,6,1,5,7]

sum = reduce(lambda a, b: a+b,nums)

print(sum)