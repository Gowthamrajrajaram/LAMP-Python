#abs function is used to return the absolute value of a number.
firstnum=-0
print("the given number using absfunction",abs(firstnum))

#all  function accepts an iterable object
firstlist=[1,2,3,4]
print(all(firstlist))
secondlist=[1,2,0]
print(all(secondlist))
thirdlist=[False,1,2,3]
print(all(thirdlist))
fourthlist=[]
print(all(fourthlist))

#bin used to return the binary representation of a specified integer.
glob=10
print(bin(glob))
globs=1
print(bin(globs))
globel=15
print(bin(globel))

#bool() converts a value to boolean(True or False)
number=100
print(bool(number))
num=0
print(bool(num))

#bytes
string = "Hello World"
arr = bytes(string, 'utf-8')  
print(arr)  

#callable() is something that can be called
def built():
    non=5
print(callable(built))

non=5
print(callable(non))

#exce
nums= 5  
exec('print(nums==5)')  
exec('print(nums+4)')  

#sum
number = sum([1, 2,2 ])  
print(number)  

#any
sub=[1,2,3,4]
print(any(sub))

#ascii
normalText = 'Python is interesting'  
print(ascii(normalText))  

#bytes
string = "Python is programming language."  
       
arr = bytearray(string, 'utf-8')  
print(arr)  

#eval run the expression code
auto= 5  
print(eval('auto + 1'))  

#float
print(float(5))

# format
print(format(123, "d"))  #integer
  
print(format(123.4567898, "f")) #float
  
print(format(12, "b")) #binary 

#frozenset
letters = ('m', 'r', 'o', 't', 's') 
fee=frozenset(letters)
print(fee)
