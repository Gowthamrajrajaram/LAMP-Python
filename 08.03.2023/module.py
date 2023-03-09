

class vehicle:
    def bike(self,enginetype,coolingsys):
        self.enginetype=enginetype
        self.coolingsys=coolingsys
        print("You are using a honda bike. It is type of",enginetype,"stroke engine and The engine is "+coolingsys+" cooling system")
    def car(self,engtype,cooling):
         self.engtype=engtype
         self.cooling=cooling
         print("You are using a KIA car. It is type of",engtype,"stroke engine and The engine is "+cooling+" cooling system")

def fun(num):
    if num%2==0:
        print("odd number: ",num)
    else:
        print("Even number: ",num)


def count_case(words):
    dic={ 'count':0,
       'num':0}
    for val in words:
        if val.isupper():
           dic['count']+=1
        elif val.islower():
            dic['num']+=1
        else:
            pass
    print("No. of Upper case characters : ",dic['count'])
    print("No. of Lower case Characters : ",dic['num'])