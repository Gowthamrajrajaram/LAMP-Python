#Arithmetic operator #numbers
#add
first=5
second=2
print(first+second)
#sub
print(first-second)
#multi
print(first*second)
#div
print(first/second)
#reminder
print(first%second)
#floor division
print(first//second)
#Exponentiation
print(first**second)

#assignment operator
#equal
firstele=5
secondele=2
thirdele=3
#+=
firstele+=1
print(firstele)
#-=
firstele-=2
print(firstele)
#*=
firstele*=2
print(firstele)
#/=
firstele/=2
print(firstele)
#%=
firstele%=2
print(firstele)
#//=
secondele//=5
print(secondele)
#**=
thirdele**=5
print(thirdele)
#&=
first&=3
print(first)
#|=
first|=2
print(first)
#^=
first^=4
print(first)
#>>=
first>>=2
print(first)
#<<=
first<<=1
print(first)

#comparision operator
print(5==5)
print(5==4)
print(1!=2)
print(1!=1)
print(6>5)
print(2>3)
print(5>=2)
print(4>=4)
print(8<=6)
print(4<=4)

#logical operator
#and
logic=5
print(logic<11 and 6>=logic)
print(logic>6 and 6>=logic)
print(logic==11 and 6>=logic)
print(logic^11 and 4==logic)
#or
print(logic<11 or 6>=logic)
print(logic>6 or 6>=logic)
print(logic==11 or 6>=logic)
print(logic==0 or 4==logic)
#not
print(not(logic > 3 and logic < 10))
print(not(logic < 3 and logic > 10))

#identity operators
print('gowtham' is 'gowtham')
print('gowtham' is not 'gowtham')

#membership operator
back = ["apple", "banana"]
print("banana" in back)
print("banana" not in back)

#bitwise operator
bit=5
bits=3
#&
print(bit&bits)
#|
print(bit|bits)
#^
print(bit^bits)
#~
print(~bits)
#<<
print(bit<<bits)
#>>
print(bit>>bits)