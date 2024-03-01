#Exercise 1
print("-------------Exercise 1-------------")
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))

print("Hello,",name, surname + ". Your age is", age)

#Exercise 2
print("-------------Exercise 2-------------")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)

#Exercise 3
print("-------------Exercise 3-------------")
score = float(input("Enter your score: "))

if score >= 90:
    grade = "5"
elif score >= 75:
    grade = "4"
elif score >= 50:
    grade = "3"
else:
    grade = "2"

print("Your grade is:", grade)

#Exercise 4
print("-------------Exercise 4-------------")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n1 % n2 == 0:
    result = "can"
else:
    result = "can't"
print(n1, result, "be divided by", n2)

#Exercise 6
print("-------------Exercise 6-------------")
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    print("The triangle is:", triangle_type)
else:
    print("The triangle specified is impossible to draw")

#Exercise 7
print("-------------Exercise 7-------------")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Division by zero"
    else: 
        result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)