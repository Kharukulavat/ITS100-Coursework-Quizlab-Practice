#Problem from mix
import numpy as np
grade = {"A":4,"B+":3.5,"B":3,"C+":2.5,"C":2,"D+":1.5,"D":1,"F":0}
course = ["Math","Phy","Com","Eng"]
namelist = []
allgrade = []
for i in range(1,6):
    print("Student#%d"%i)
    name = input("Name: ") 
    namelist.append(name) #to add name to namelist
    for i in course:
        while True:
            g = input("%s: "%i) #grade for each subject
            if g in grade:
                allgrade.append(g)
                break
            else:
                print("- Error! Enter Again -")
                continue 
gpatable = np.reshape(np.array(allgrade), (5,4))

for c in course:
    print("\t%s"%c,end = "")
print("\tGPA")
for n in range(len(namelist)):
    print("%s\t"%namelist[0],gpatable[n,:])





                
                
                
                
                
                
                
                
                
                
                
#Problem from mix
# grade = {"A":4,"B+":3.5,"B":3,"C+":2.5,"C":2,"D+":1.5,"D":1,"F":0}
# course = ["Math","Phy","Com","Eng"]
# for i in range(1,6):
#     print("Student#%d"%i)
#     name = input("Name: ")
#     while True:
#         math = input("Math\t: ")
#         if math in grade:
#             print()
#         else:
#             print("- Error! Enter Again -")
#             continue
#         break
#     while True:
#         phy = input("Phy\t: ")
#         if phy in grade:
#             print()
#         else:
#             print("- Error! Enter Again -")
#             continue
#         break
#     while True:
#     com = input("Com\t: ")
#                 if com in grade:
#                     eng = input("Eng\t: ")
#                     if eng in grade:
#                         print()
#                     else:
#                         print("- Error! Enter Again -")
#                         continue
#                 else:
#                     print("- Error! Enter Again -")
#                     continue