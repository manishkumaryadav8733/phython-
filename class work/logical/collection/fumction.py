# def test():
#     print("test calling")
#     def square(a):
#         sq= a*a
#         print(f" square of {a} is {sq}")
#         def add(b):
#             sum = a + b
#             print(f"sum of {a} and {b} is {sum}")
#     def multiply(c):
#         mul = a * c
#         return mul
#         print(f"multiplication of {a} and {c} is {mul}")
#         test()
#         square(5)
#         multiply(10) 
#         def person(name,email,phone):               
#                  print(f"my name is {name} and my email is {email}")
#                     print(f"my phone number is {phone}")
                         
# def add(*a):
#     print(a)
#     add(10,20,30,40)
# def person(**a):
# print(a)
# person(45,54,545,45)
a= 10
def test():
    global a
    a= 20
    print(a)
    
test()
    print(a)    

