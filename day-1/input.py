"""
Write a program that receives a person's name, greets
them then prints out the total number of characters in their name 
"""

name = input()
greetings = "Hello " + name + "!"
nameLen = len(name)

print(greetings)
print(nameLen)