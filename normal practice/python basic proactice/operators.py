# print(10+10)
# print('abc'+'abc')
# print("10"+10)
# print(True+True)
# print(False+False)
# print(True+1)
# print(True-1)


# print(10*10)
# print("a"*10)
# print(10//3)
# print(10%30)
# print(10**2)

# assignment operator , =         
a = 10

# a = a+20
# a+=20
# a-=20
# a/=20
# a%=20
# a**20
# a//3

# print(a)

from functools import reduce
a = [1,3,5,98,7,8,4,2]
b=  list(map(lambda x: x*x,a))   
c = list(filter(lambda x : x%2!=0,a))
d = (reduce(lambda x,y: x+y,a))
print(b,c,d)