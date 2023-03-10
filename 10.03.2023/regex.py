import re

# Matching any character except newline(.)
pattern1 = r".at"
string1 = "cat, hat, sat"
result1 = re.findall(pattern1, string1)
print(result1)  #['cat', 'hat', 'sat']
# ^(start)

pattern = r'^hello'
print(re.match(pattern, 'hello world!'))    # Match
print(re.match(pattern, 'goodbye world!'))  # No match
#$(ending)

pattern = "world$"
string1 = "hello world"
string2 = "goodbye world"
string3 = "hello universe"
matches1 = re.findall(pattern, string1)
matches2 = re.findall(pattern, string2)
matches3 = re.findall(pattern, string3)
print(matches1)  #['world']
print(matches2)  #['world']
print(matches3)  #[]
# *(zero or more occurrences)
pattern2 = r"ba*na"
string2 = "baana, banana, banaana"
result2 = re.findall(pattern2, string2)
print(result2)  #['baana', 'banana', 'banaana']
# ? (zero or one occurance)
pattern4 = r"colo?r"
string4 = "color, colour"
result4 = re.findall(pattern4, string4)
print(result4)  #['color', 'colour']
# | (like OR gate)
pattern5 = r"cat|dog"
string5 = "I have a cat and a dog"
result5 = re.findall(pattern5, string5)
print(result5)  #['cat', 'dog']
# +(one or more occurrences of the previous character)
pattern3 = r"go+l"
string3 = "gl, gol, gool, goooool"
result3 = re.findall(pattern3, string3)
print(result3)  # Output: ['gol', 'gool', 'goooool']
#[](any single character within the brackets)
pattern6 = r"[aeiou]"
string6 = "apple, orange, banana"
result6 = re.findall(pattern6, string6)
print(result6)  # ['a', 'e', 'o', 'a', 'a']
# {n} (exactly n occurrences of the previous character or group)
pattern9 = r"a{3}"
string9 = "aaa, a, aa, aaaaa"
result9 = re.findall(pattern9, string9)
print(result9)  #['aaa', 'aaa', 'aaa']
# [^] (any single character not within the brackets)
pattern7 = r"[^aeiou]"
string7 = "apple, orange, banana"
result7 = re.findall(pattern7, string7)
print(result7)  #['p', 'p', 'l', ',', ' ', 'r', 'n', 'g', ',', ' ', 'b', 'n', 'n']
#match
strings="gowthamraj"
pattern=r"raj"
match = re.match(pattern, strings)
if match:
    print("Match found!")
else:
    print("Match not found.")
print("...........................")
#search
fullname = "I am learning python regex"
frontname = r"python"
match = re.search(frontname, fullname)
if match:
    print("Match found!")
else:
    print("Match not found.")
print("...........................")
#findall
name= "Aspire system"
names = r"[aeiou]"
matches = re.findall(names, name)
print(matches)

print("...........................")
#replacing
newstring = "Hello, World!"
newpattern = r"World"
replacement = "Gowtham"
new_string = re.sub(newpattern, replacement, newstring)
print(new_string)

print("...........................")
#split
print(re.split(r'\W+',"we are one"))

