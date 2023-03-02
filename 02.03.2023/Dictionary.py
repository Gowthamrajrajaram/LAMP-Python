dicts={"name":"Gowtham",
      "age":21,
      "place":"salem",
      
      }
print(dicts)
print(dicts["name"])
del dicts['place']
print(dicts)
print('age' in dicts)
print('age' not in dicts)
dicts['place']='salem'
dicts['gender']='male'
print(dicts)
dicts.pop('age')
print(dicts)
print(dicts.keys())
print(dicts.values())

mydict=dicts.copy()
print(mydict)

#nested dictionary
myfamily = {
  "child1" : {
    "name" : "gowtham",
    "year" : 2004
  },
  "child2" : {
    "name" : "mano",
    "year" : 2007
  },
  "child3" : {
    "name" : "kavin",
    "year" : 2011
  }
} 
print(myfamily['child2']['year'])

#dict comperhension
values={x:x**2 for x in (2,3,4)}
print(values)

text={i:i for i in range(10)}
print(text)

texts={i:i for i in ('gowtham','kavin','guna','mano','ananth')}
print(texts)
texts_1={'name':i for i in ('gowtham','kavin','guna','mano','ananth')}
print(texts_1)