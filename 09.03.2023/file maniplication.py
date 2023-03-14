
#Python code to create a file
file = open('file.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#append
file = open('file.txt', 'a')
file.write("This will add this line")
file.close()

#read
file = open('file.txt','r')
for each in file:
   print (each)
print(file.read())

#with
with open("file.txt", "w") as f:
    f.write("Hello World!!!")

#split
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print (word)

