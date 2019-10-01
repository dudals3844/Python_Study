#function
def add (a,b):
    return a + b

def say():
    print("Hi")

a = 1
b = 2
c = add(a,b)
print(c)
say()

result = add(a=3, b=7)
print(result)

#if i don't know how many input here
def add_many(*args):
    result = 0
    for i in args:
        result = result + 1
    return result

num = add_many(1,2,3,4,5,6,7,8,9,10)
print(num)#10개 있어서 10 출력


#function return always one
def add_mul(a,b):
    return a+b , a*b
result = add_mul(3,4)
print(result)#tuple return

#declare global variable
# a = 1
# def vartest(a):
    
#     a = a + 1
#     return a
# a = vartest(a)
# print(a)

a = 1 
def vartest(): 
    global a
    a = a + 1
    

vartest() 
print(a)

#lambda
add = lambda a, b : a+b#same def add(a,b): return a+b
result = add(1,2)
print(result)