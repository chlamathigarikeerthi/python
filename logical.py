#logical operators
a = 25
citizen = True
print(age >= 18 and citizen == True)
age = 16
citizen = True
print(age >= 18 and citizen == True)
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