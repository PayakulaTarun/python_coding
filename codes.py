#Variables and Data Types

# Write a program to declare an integer variable and print its value
"""
num = 10
print(num)
"""
# Create a program that takes user input for their age and prints it.
"""
num = int(input("enter your age"))
print(num)
"""
#Write a program that calculates the area of a rectangle (length * width).
"""
length = int(input("enter your length"))

width = int(input("enter your width"))

area = length * width

print("Area of rectangle is", area)
"""
#Create a program that swaps the values of two variables.
"""
a = int(input("enter your number"))

b = int(input("enter your second number"))

a, b = b, a

print("After swapping, a is", a, "and b is", b)"""

#Write a program that concatenates two strings and prints the result.
"""
str1 = "Hello"

str2 = "World"

result = str1 + " " + str2

print(result)
"""
#Develop a program that converts a Fahrenheit temperature to Celsius
"""
fahrenheit = int(input("Enter the temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(fahrenheit, "Fahrenheit is equal to", celsius, "Celsius")
"""
#Create a program that takes a number as input, squares it, and prints the result.
"""
num = int(input("Enter a number: "))

result = num ** 2

print("The square of", num, "is", result)
"""

#Write a program that checks if a number is divisible by both 5 and 7.
"""
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 7 == 0:
    print(num, "is divisible by both 5 and 7.")
else:
    print(num, "is not divisible by both 5 and 7.")
"""
# Develop a program that calculates the average of three numbers.
"""
num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

num3 = int(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3

print("The average of", num1, ",", num2, "and", num3, "is", average)
"""

#Create a program that uses different data types (int, float, string) in one statement.
"""
num = int(input("enter a number"))
float_num = float(input("enter a float"))
str_num = input("enter a string")

print(num, float_num, str_num)
"""
#Write a program to check if a given year is a leap year.
"""
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
"""

#Create a program that generates a random number and prints it.
"""
import random

random_num = random.randint(1, 100)

print("The random number is", random_num)
"""
# Write a program that calculates the simple interest using user input for principal, rate, and time.
""""
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time in years: "))

interest = (principal * rate * time) / 100

print("Simple Interest is", interest)
"""
# Develop a program that converts a string to uppercase.
"""
str = input("Enter a string: ")

print("Uppercase version:", str.upper())
"""
#Create a program that checks if a given number is positive, negative, or zero.
"""
num = int(input("Enter a number: "))

if num > 0:
    print(num, "is positive.")
elif num < 0:
    print(num, "is negative.")
else:
    print(num, "is zero.")
"""
#Write a program that concatenates three strings and prints the result
"""
str1 = "Hello"
str2 = "World"
str3 = "!"

result = str1 + " " + str2 + str3
print(result, "is positive  and " + str1 + " is negative "  + str2 + " is zero  " + str3 + " is one")
"""
#Develop a program that converts a given number to a binary representation.
"""
def decimal_to_binary(num):
    binary=""
    while num > 0:
        binary=str(num%2)+binary
        num=num//2
    return binary or 0
num=int(input("Please enter a number"))
binary=decimal_to_binary(num)
print(binary)
"""
#Create a program that uses the `len()` function to find the length of a list.
"""
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("The length of the list is:", length)
"""
#Write a program that uses the `input()` function to get the user's name and prints a greeting.
"""
name = input("Enter your name: ")
print("Hello", name)
"""
# Develop a program that calculates the sum of digits in a given number
"""
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
"""
# Print() method Python

# **Basic Print:**- Write a program that prints "Hello, World!" to the console
"""
print("Hello, World!")
"""

#. **Multiple Prints:**- Create a program that uses multiple `print` statements to output a message with line breaks

"""
print("Hello")
print("world!")
"""
# **Formatted Output:**- Write a program that uses formatted strings to print variables with descriptive messages.
"""
name = input("Enter your name: ")
print(f"my name is : {name}")
"""
# **String Concatenation:**- Develop a program that prints the concatenation of two strings
"""
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)
"""
# **Escape Characters:**-Create a program that uses escape characters to print a multi-line string.
"""
print("hello \n world!")
"""
#**Print without Line Break:**- Write a program that prints multiple items on the same line without line breaks.
"""
print("Hello", "World", sep=" ")
"""
#. **Variable Printing:**- Develop a program that takes user input and prints a personalized greeting
"""
name = input("Enter your name: ")
print("Hello", name)
"""
#**Number Printing:**- Create a program that prints the result of a mathematical expression
"""
a =  int(input("enter a number: ")) 
b = int(input("enter another number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
"""
#. **Precision Printing:**- Write a program that uses formatted strings to print a floating-point number with two decimal places.
"""
number = float(input("Enter a number in float"))
print(f"the number with 2 decimal places {number:.2f}")
"""
#**Print with Separator:**- Develop a program that prints multiple items separated by a specific character
"""
a=input("Enter a name: ")

b=input("Enter a number: ")

print(a,b,sep=" @ ")
"""
#**Printing Variables and Constants:**- Create a program that prints the value of a variable and a constant
"""
a=int(input("Enter a number"))

print(a)
"""
#**Print with End Parameter:**- Write a program that prints multiple items with a custom `end` parameter.
"""
a=int(input("Enter a number"))
b=input("Enter a name")
print(a,b,end=".......")
"""
#**Printing Raw Strings:**- Develop a program that uses a raw string to print a path without interpreting escape characters.
"""
path = r"D:\python\Python_beginner questions.pdf"
print(path)
"""
# **Print with Triple Quotes:**- Create a program that uses triple-quoted strings to print a multi-line message
"""
#print("""#Hello
#World!""")

# **Printing Special Characters:**- Write a program that prints special characters (e.g., copyright symbol, newline) using Unicode escape sequences.
"""
print("\u00A9") # copyright symbol
print("\n") # newline
"""
#. **Print with Separator and End:**- Develop a program that uses both the `sep` and `end` parameters in the `print` function

"""
a=input("Enter a name: ")

b=input("Enter a number: ")

print(a,b,sep=" @ ", end=".......")
"""
#**Formatted Output with Arithmetic:**- Create a program that uses formatted strings to print the result of an arithmetic expression.
"""
a=int(input("Enter a number: "))

b=int(input("Enter another number: "))

print(f"Addition: {a+b}")

print(f"Subtraction: {a-b}")

print(f"Multiplication: {a*b}")

print(f"Division: {a/b}")
"""
#. **Print with File Parameter:**- Write a program that prints to a file using the `file` parameter in the `print` function
"""
with open("output.txt", "w") as file:
    print("Hello, World!", file=file)
"""
#**Conditional Printing:**- Develop a program that uses the `print` function inside a conditional statement.
"""
a=int(input("Enter a number: "))

if a > 0:
    print("The number is positive")
elif a < 0:
    print("The number is negative")
else:
    print("The number is zero")
"""
# **Print with f-strings:**- Write a program that uses f-strings to print variables and expressions.
"""
name = input("Enter your name: ")

age = int(input("Enter your age: "))

print(f"Hello, {name}! You are {age} years old.")
"""