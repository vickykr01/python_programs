# Write a program that asks the user for their name and age, then prints a sentence like: "Hello vicky, you are 21 years old!"

name = input("Enter your name:")
age = int(input("Enter your age:"))
print("Hello", name, "you are" , age, "years old!")

#Take two numbers as input from the user and print their sum, difference, product, and quotient
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

#Ask the user to enter two integers and one float. Convert them all to floats and print their average.
c = int(input("enter first num: "))
d = int(input("enter second num: "))
e = float(input("enter third num:  "))
avg = (float(c + d + e)/3)
print("Average:", avg)

#The user enters a string containing a number (e.g., "45"). Convert it to: an integer, a float, and a string again. Print all three values with their types.
f = input("Enter a number as a string: ")
g = int(f)
h = float(f)
i = str(f)
print("Integer:", g, type(g))
print("Float:", h, type(h))
print("String:", i, type(i))

#Take a decimal number as input (like 45.78) and output its: integer part (45) and fractional part (0.78)
j = float(input("Enter a decimal number: "))
k = int(j)
l = j - k
print("Integer part:", k)
print("Fractional part:", l)