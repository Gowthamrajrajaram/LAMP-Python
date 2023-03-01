print(2+3)
a=5
b=8
print(a+b)

#getting a input from user
name=input("Enter your name:")
print("Your name is:",name)

number=int(input("Enter your age:"))
if number>18:
 print("You are eligible to vote")
else:
 print("You are not eligible to vote")

#to find which type
print(type(5))
print(type("gowtham"))
print(type(5.5))
print(type(0))
print(type(True))
print(type(False))

#object identity

doc=50
docs=doc
print(id(doc))
print(id(docs))
docs=40
print(id(docs))
strings="Aspire system"
print(id(strings))
boolean=True
print(id(boolean))

#Multiple assignment
studio=data=base=50 #Assigning single value to multiple variables
print(studio)
print(base)
print(data)

Studio,Data,Base=80,56,6 #assigning multiple values to multiple variables
print(Studio)
print(Base)
print(Data)

# variable types
#local variable
def adds():
 assin=10
 lens=20
 copy=lens+assin
 print(copy)
adds()

#global variable
gain=100
def add():
  global gain
  print(gain)
  gain= 'Aspire'
  print(gain)
add()
print(gain)

#delete variable
var=10
obj=23
print(var)
#del var
print(var)
print(obj)