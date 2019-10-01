#Dictionary
dic = {'name':'pey','phone':'01099533844','birth':'970912'}

#plus dictionary
dic['sex'] = 'male'
print(dic)

#remove dictionary
del dic['birth']
print(dic)

#key and value
print(dic['phone'])

#print key
print(dic.keys())

#print value
print(dic.values())

#print key and value both
print(dic.items())

#cofirm key in dictionary
print('male' in dic)
print('name' in dic)