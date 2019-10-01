#for

test_list = ['one','two','three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first+last)

    
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d: pass "%number)#print("{0}".format(number))

#for - range
add = 0
for i in range(1,11):#plus 1~10
    add = add + i
print(add)

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("pass: {0}".format(number))


#for using list
a = [1,2,3,4]
result = []
for num in a:#num에 리스트 한개의 값씩 넣는다
    result.append(num * 3)
print(result)