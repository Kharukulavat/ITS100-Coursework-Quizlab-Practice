#Example 7.13 Fibo nacci sequences
F = [0,1]
while True:
    f = F[-1]+F[-2]
    if f < 100:
        F.append(f)
    else:
        break
print(F) #>>[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#Example 7.12
l = []
while True:
    try:
        x = input("Enter an integer: ")
        if x == "DONE":
            break
        elif float(x) > 0:
            l.append(float(x))
    except ValueError:
        print("Invalid value. Please input an integer!")
print("Sum = %.2f"%sum(l))




#Example 7.11
l = []
while True:
    try:
        x = int(input("Enter an integer: "))
        l.append(x)
        if x < 0:
            break
    except ValueError:
        print("Invalid value. Please input an integer!")
print("Input values =",l)
        



#Example 7.8
#using continue

s = input("Enter a string: ")
for c in s:
    if c.lower() in "aeiou":
        continue
    else:
        print(c, end="")
print()

#withput using continue
s = input("Enter a string: ")
for c in s:
    if c.lower() not in "aeiou":
        print(c, end="")
print()



#Example7.6 Prime factor

#using while loop
x = int(input("Enter an integer: "))
prime = True
i = 2
while i < x:
    if x % i != 0: #to check if the numbers other than 1 and itself are factors of this number
        i += 1
    else: #if x % i == 0
        prime = False
        break
if prime: # equal to if prime == True
    print(x,"is a prime number.")
else:
    print(x,"is not a prime number.")

#using for loop
x = int(input("Enter an integer: "))
prime = True
for i in range(2,x): #to check if the numbers other than 1 and itself are factors of this number
    if x % i == 0:
        prime = False
        break
if prime: # equal to if prime == True
    print(x,"is a prime number.")
else:
    print(x,"is not a prime number.")
        



#Example7.2
i = 1
sum = 0
while i <= 50:
    sum += i**2
    i += 1
print(sum)

import numpy as np
a = np.arange(1,51,1)
sq = a**2 #>> [   1    4    9   16   25   36   49   64   81  100  121  144  169  196
#   225  256  289  324  361  400  441  484  529  576  625  676  729  784
#   841  900  961 1024 1089 1156 1225 1296 1369 1444 1521 1600 1681 1764
#  1849 1936 2025 2116 2209 2304 2401 2500]
print(np.sum(sq))
