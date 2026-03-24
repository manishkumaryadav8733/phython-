import reduce from functools
# l = ["phython","php","java","node","android"]
# k = filter(lambda x:"a" in x,l)
# print(list(k))
# l = ["phython","php","java","node","android"]
# k = filter(lambda x:len(x)>4,l)
# print(list(k))
# l = [2,9,8,25,4,9,4,58,1,144,22,33]
# def sqrt(a):
#     return a**0.5
# k = filter(sqrt,l)
# print(list(k))
l = [10,20,30,40,50,60,70,80,90]
def add(a,b):
    return a+b
k = reduce(add,l)
print(k)       