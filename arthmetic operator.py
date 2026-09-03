#arthimetic operater

a = 10
b = 3

print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Remainder:", a%b)
print("Exponentiation:", a**b)

#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

#student marks calculator
name = input("Enter student name: ")
marks1 = int(input("Enter python marks: "))
marks2 = int(input("Enter java marks: "))
marks3 = int(input("Enter SQL marks: "))
total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3
print("\n----- Student Report -----")
print("Name:", name)
print("Total Marks:", total_marks) 
#shopping bill calculator
price1 = float(input("Enter product 1 price: "))
price2 = float(input("Enter product 2 price: "))
price3 = float(input("Enter product 3 price: "))
total_price = price1 + price2 + price3
discount = total_price * 10 / 100
final_price = total_price - discount
print("Discount:", discount)
print("Final amount:", final_price)
print("total Bill:", total_price)
#assignment operators
x = 10
x+= 5
print( x)
x -=2
print(x)
x*=3
print(x)

#bank balance
balance = 10000
deposit = 5000
balance+= deposit
print("After deposit:", balance)
withdraw = 2000
balance -= withdraw
print("After withdrawal:", balance)

#comparison operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
#age eligibility checker
age = int(input("Enter your age: "))
print("Eligible:", age >= 18)
#pass or fail checker
marks = int(input("Enter your marks: "))
print("Passed:", marks >= 40)
#login validation
correct_username = "admin"
correct_password = "123"
username = input("Enter username: ")
password = input("Enter password: ")
print("username == correct_username)
print("password == correct_password)
