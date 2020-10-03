def mygenfun(lis):
    for i in lis:
        yield(i*i)

my_lis = mygenfun([5,6,2,1])

# print(my_lis)
print(next(my_lis))
print(next(my_lis))