"""
Switch the values between variable `a` and `b` without touching
the code provided
"""

a = input()
b = input()
print("Old a: " + a)
print("Old b: " + b)
print()

# Your code goes below 👇🏾

temp = a
a = b
b = temp

# Your code above ☝🏾

print("New a: " + a)
print("New b: " + b)