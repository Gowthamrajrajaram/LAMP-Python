#Treating the functions as objects. 
def shout(text):
    return text.upper()
print(shout('Hello'))
yell = shout
print(yell('Hello'))

#Passing the function as an argument 
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting = func("Hi, I am created by a function passed as an argument.")
    print (greeting)
greet(shout)
greet(whisper)

#Returning functions from another function.
def create_adder(x):
    def adder(y):
        return x+y
    return adder
adds = create_adder(15)
print(adds(10))

# code for testing decorator chaining
def decor1(func):
	def inner():
		high = func()
		return high * high
	return inner

def decor(func):
	def inner():
		highs = func()
		return 2 * highs
	return inner
@decor1
@decor
def num():
	return 10
@decor
@decor1
def num2():
	return 10
print(num())
print(num2())
