#lambda function
#diff b/w lambda and def function
def cube(y):
    return y*y*y
 
lambda_cube = lambda y: y*y*y

print("Using function defined with `def` keyword:", cube(5))

print("Using lambda function:", lambda_cube(5))

def reciprocal( num ):  
    return 1 / num
lambda_reciprocal = lambda num: 1/ num   
print( "Def keyword: ", reciprocal(6) )  
print( "Lambda keyword: ", lambda_reciprocal(6) )

#lambda function with oneline
print((lambda x:(x % 2 and 'odd' or 'even'))(3))

numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"

print("Int formatting:", numeric(100))
print("float formatting:", numeric(9999.789535))

# lambda function using if-else
Max = lambda a, b : a if(a > b) else b
 
print(Max(1, 2))

# filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final= list(filter(lambda x: (x % 2 != 0), li))
print(final)

# map
lis = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
finallist = list(map(lambda x: x*2, li))
print(finallist)

#reduce
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)
