obj=(1,2,3,5,4,5,[1,5,6,8],{1,32,5,5},'python')
print(type(obj))
print(obj)
print(obj.count(5))
print(obj.index(5))
print(obj*2)
print(obj[2:5])
print(obj[5:8])
print(obj[2:])
print(obj[:5])
print(obj[-1:])
chars=('a','b','c')
char=('d','e','f')
print(char+chars)
for i in char:
    print(i)