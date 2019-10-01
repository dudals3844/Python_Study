word = "Hello"

print(word)

wordlinechange = "Hello \n World"

print(wordlinechange)

head = "Python"
body = " is fun"

print(head+body)


a = "Python"
print(a * 2)

#string length
b = "Life is too short"
print(len(b))

num = 3
banana = 4
print("I want eat %d apples and %d banana"%(num,banana))
# using format
print("I want eat {0} apples and {1} banana".format(num,banana))
print("I want eat {0} apples and {banana_index} banana".format(num,banana_index=banana))

#f fomating
name = "Choi"
f'MY name is {name}'

#char count
a = "hobby"
print(a.count('b')) #2 'b' in hobby

#find location char
print(a.find('b'))

#splite string
a = "Latte is horse"
print(a.split())

b = "a:b:c:d"
print(b.split(':'))