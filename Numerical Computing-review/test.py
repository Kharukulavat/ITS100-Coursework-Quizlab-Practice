import numpy as np


a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = np.ones([4,4])
c = np.arange(1,100,2)
d = np.arange(0,101)
e=[]
for i in d:
   e.append("2**%d"%i)
print(e) 
print(np.sum(a))
print(a)
print(b)
print(c)