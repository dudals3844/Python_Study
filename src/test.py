#laern list

odd = [1,2,3,4,5]

print(odd[0])

print(odd[-1])

a = [1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[-1][0])

b = [1,2,3,4,5]

print(b[0:2])

a = [1,2,3]
b = [4,5,6]
print(a+b)

#repeat list
print(a*3)
#list length
print(len(a))

#error a + "hi" because different type
print(str(a)+"hi")

#edit list
a = [1,2,3]
a[1] = 100
print(a)

#delete list element
del a[1]
print(a)

#plus list element
a = [1,2,3]
a.append(4)
print(a)

a = [4,3,2,1]
a.sort()
print(a)

a = [1,2,3,4]
a.reverse()
print(a)

print(a.index(1))

a.insert(0, 77)
print(a)

print(a.count(77))

a.extend([99,100])
print(a)