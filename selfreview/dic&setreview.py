#Example 8.18
s1 = input("Input string1: ")
s2 = input("Input string2: ")

#Solution 1
list1 = sorted(list(s1.lower()))
list2 = sorted(list(s2.lower()))

#To remove spaces if the inputs have them and check only for alphabets
list1 = [c for c in list1 if c.isalpha()]
list2 = [c for c in list2 if c.isalpha()]

if list1 == list2:
    print("Output: The input strings are anagrams")
else:
    print("Output: The input strings are not anagrams")


#Example8.17
text1 = input("Input string1: ")
set1 = set(list(text1))
text2 = input("Input string2: ")
set2 = set(list(text2))

intersec = set1&set2
sort = sorted(intersec) #To sort this intersec set as a list
print(sort)
print("Output:","".join(sort))
# print("Output:","".join(sorted(list(intersec))))


#Example 8.12
w = {}
text = input("Input a string: ")
for i in text:
    if i.isalpha() and i.lower() not in w:
        w[i.lower()] = 1
    else:
        continue
print("Output: ",end="")
for k in sorted(w.keys()):
    print(k, end="")
print() #just to move cursor down


s = input("Input a string: ")
alphabets = {}
for c in s:
    if c.isalpha():
        if c.lower(): #We don't have to check if it's in dictionary or not if we add this
            alphabets[c.lower()] = 1
print("Output: ", end="")
for k in sorted(alphabets.keys()):
    print(k, end="")
print()
# print("Output:","".join(sorted(alphabets.keys()))) also has the same output


#Example 8.9
w = {}
text = input("Input a string: ")
for i in text:
    if i.isalpha() and i.upper() in "AEIOU" and i.upper() not in w:
        w[i.upper()] = 1
    elif i.isalpha() and i.upper() in w:
        w[i.upper()] += 1
    else:
        continue 
print("Output:")
for k,v in sorted(w.items()):
    print(k,"=",v)

#Without using dictionary
s = input("Input a string: ")
a,e,i,o,u = 0,0,0,0,0
for c in s:
    if c.lower() == 'a':
        a += 1
    elif c.lower() == 'e':
        e += 1
    elif c.lower() == 'i':
        i += 1
    elif c.lower() == 'o':
        o += 1
    elif c.lower() == 'u':
        u += 1
print("Output:")
print("A =", a)
print("E =", e)
print("I =",i)
print("O =", o)
print("U =", u)


#Example 8.11
word = {}
while True:
    w = input("Input (DONE = exit): ")
    if w == "DONE":
        break
    elif w.lower() in word:
        word[w.lower()] += 1
    else:
        word[w.lower()] = 1
print("Output:")
for k,v in word.items():
    print(k,"=",v)
    
#Without using dictionary
words = []
while True:
    w = input("Input (DONE = exit): ")
    if w == "DONE":
        break
    for i in words: #check if w is in the list "words"
        if i[0] == w.lower(): #check if key is duplicated 
            i[1] += 1 #plus the value 
            break #to stop this loop when we found it duplicated then continue the process
    else:
        words.append([w.lower(),1]) #Add list of [key, value] to the list 
print("Output:")
for k in words:
    print(k[0],"=",k[1])  