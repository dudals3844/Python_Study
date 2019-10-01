#
a = [1,2,3]
b = a[:]
print(b)

#using copy
from copy import copy
b = copy(a)# == a[:]

print(b is a)

