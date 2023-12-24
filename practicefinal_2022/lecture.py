L = input("Give a list: ")
a = ["1",'2','3','4']
print(a[1:-1])
print(type(L))
print(max([int(i) for i in L[1:-1].split(',')]))


# def f(x):
#     res = 0
#     while x > 0:
#         y = x % 10
#         res = res*10 + y
#         x = x//10
#     return res

# n = input("Input an integer: ")
# try:
#     n = int(n)
#     print("Output:", f(n))
# except:
#     print("Invalid input")