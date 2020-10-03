def iseven(n):
    return n%2==0

nums = [4,2,3,5,6,1,5,7]

evens = list(filter(iseven,nums))

print(evens)