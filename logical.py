#logical operators
a = 25
citizen = True
print(a >= 18 and citizen==True)
a = 16
citizen = True
print(a >= 18 and citizen==True)
has_card = False
has_cash = True
print(has_card or has_cash )
is_logged_in = True
print(not is_logged_in)
#atm eligibility checker
balance = 10000
withdrawal = 5000
print(withdrawal > 0 and withdrawal <= balance)
#student scholarship eligibility checker
marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance: "))
eligible = marks >= 85 and attendance >= 75
print("Scholarship Eligibility:", eligible)
#identity operators
a = None
print(a is None)
print(a is not None)
#bitwise operators
a = 5
b = 3
print(a & b)  
print(a | b)
print(a ^ b) 
#electric city bill calculator
units = int(input("Enter electricity units: ")) 
rate = 6
bill = units * rate
print("Electricity Bill:", bill) 
# travel expense calculator
travel = float(input("Travel expense: "))
food = float(input("Food expense: "))
hotel = float(input("Hotel expense: "))
total = travel + food + hotel
print("Total Expense:", total)
 