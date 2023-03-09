names = ['gowtham', 'guna', 'kavin', 'mano', 'ananth', 'gowtham', 'durai']
numbers=[1,2,3,4]
print(names.count('gowtham'))
names.append('bala')
print(names)
print(names.index('guna'))
names.sort()
print(names)
print(names.pop())
mynames=names.copy()
print(mynames)
names.extend(numbers)
print(names)
mynames.reverse()
print(mynames)
numbers.clear()
print(numbers)
print(names.index(2,4))
names.remove('guna')
print(names)
names.insert(2,'arun')
print(names)
#list comprension
newlist=[1,2,3,4,5,6]
square=[]
for i in newlist:
    square.append(i**2)
print(square)
numlist=[x for x in range(50) if x<20]
print(numlist)
squares = []


#nested list Comprehensions
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)