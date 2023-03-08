import math
#index error
a=[1,2,3]
try:
    print("Second element = ",a[1])
    print("Third element = ",a[3])
except IndexError:
    print("An index error occured")
print(".........................")
#zero division error
number=5
try:
    print("divided by 5/0",number/0)
except ZeroDivisionError:
    print("An zerodivison error occured")
print(".........................")
#value error

name='gowtham'
try:
    count=int(name)
except ValueError:
    print("An value error occurs")

print(".........................")
#key error
data={'name':'guna',
        'age':21,
        'gender':'male',
    }
try:
   value=data['palce']
except KeyError:
    print("An key error occurs")
print(".........................")
#else
count=5
try:
    count=str(count)
except ValueError:
    print("Invalid input")
else:
    print("Your count:", count)
print(".........................")
#finally
try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")
print(".........................")
#raise
class error(Exception):
    pass
class toosmaller(error):
    pass
class toolarger(error):
    pass
nums=10
while True:
    try:
        ch=int(input("Enter a number = "))
        if ch<nums:
            raise toosmaller#userdefined function
        elif ch>nums:
            raise toolarger
        break
    except toosmaller:
        print("you entered too small number")
    except toolarger:
        print("you entered too large number")
print("you enterd a coorect number")
print(".........................")

class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of negative number")
    return math.sqrt(num)
square_root(-1)