#function
def value():
    print("I am learning functions")
value()
print("...........")
#return function
def values(num,val):
    return num*val
print(values(5,2))
print("...........")
#keyword function
def docs(name,fun):
    spl=[]
    while name<fun:
        spl.append(name)
    return spl
result=docs(fun=11,name=1)
print(result)
print("...........")
#higher   order function
def apply_to_list(func, lst):
    return [func(x) for x in lst]
def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squares = apply_to_list(square, numbers)
print(squares)
print("...........")
#higher order function
def add_number(n):
    def add_n(x):
        return x + n
    return add_n
add_five = add_number(5)
result = add_five(3)   # result is 8
print(result)
print("...........")
#higher order function
def multifun(func,farg1,farg2):
    return func(farg1,farg2)
def sum(x,y):
    return x*y
print(multifun(sum,10,5))
