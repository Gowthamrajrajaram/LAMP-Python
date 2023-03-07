#class and object
class student:
    subjects='Tamil'
    staffName='Kavin'

data=student()
print(data)
print(".....................")
#class attribute
class staff():
    salary=3000
    domain='english'
print(".....................")
#getattr method
print(getattr(staff,'salary'))
print(getattr(staff,'domain'))
print(getattr(staff,'staffcount',"No such attribute found"))
print(".....................")
#dotnotation
print(staff.salary)
print(staff.domain)
print(".....................")
#setter
setattr(staff,'name','guna')
setattr(staff,'staffcount',5)
print(staff.name)
print(staff.staffcount)
print(".....................")
#instance attribute
class user:
    course='python'

desk=user()
print(user.course)
print(user.__dict__)
print(desk.course)
print(desk.__dict__)
print(".....................")
#instance method
class vehicle:
    engine='2 stroke'
    enginetype='petrol'

    def twowheeler(self,enginesys):
        print(vehicle.engine)
        print(vehicle.enginetype)
        print(enginesys)

transport=vehicle()
transport.twowheeler('air cooled')
print(".....................")
# init method in Python
 
class user:
    def __init__(self, name):
        print("Call When new Instance Created")
        self.name = name
 
    def printall(self):
        print("Name : ", self.name)
 
 
obj = user("kavin kumar")
 
obj.printall()
print(obj.__dict__)
objs = user("kavin kumar")
objs.printall()
print(objs.__dict__)
print(user.__dict__)
print(".....................")
# Multiple Inheritance
 
class Father:
    def fishing(self):
        print("Fishing in Rivers")
 
    def chess(self):
        print("Playing Chess From Father")
 
 
class Mother:
    def cooking(self):
        print("Cooking Food")
 
    def chess(self):
        print("Playing Chess From Mother")
 
 
class Son(Mother,Father):
    def ride(self):
        print("Riding Bicycle")
o = Son()
o.ride()
o.fishing()
o.cooking()
o.chess()
print(".....................")
#iterator
fruits='apple','banana','graphs','pineapple'
fruit=iter(fruits)
print(next(fruit))
print(next(fruit))
print(next(fruit))
print(next(fruit))
print(".....................")
#iterable
for fruit in fruits:
    print(fruit)

