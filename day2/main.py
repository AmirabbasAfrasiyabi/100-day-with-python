
# x = input()
# print(x[2])

"""
print("hello" + "world")
print("123" + "345")
print(123 + 456)
"""

"""
Num_Char = len((input("What is your name ?")))
New_Num_char = str(Num_Char)
print(" your name has" + " " + New_Num_char + " " + "Characters.")
"""

"""
Two_Digit_Number = input()
First_Digit = Two_Digit_Number[0]
Second_Digit = Two_Digit_Number[1]
result = First_Digit + Second_Digit
result2 = int(First_Digit) + int(Second_Digit)
print(result)
print(result2)
"""

"""
print(3*3 +3/3 -3)
"""

"""
#calculator
height = input()
weight = input()
BMI = int(int(weight) / float(height))
print(f"my Bmi is {BMI}")
"""

"""
age = input()

age_as_int = int(age)

year_remaining = 90 - age_as_int
day_remaining = year_remaining *365
weeks_remaining = year_remaining *52
month_remaining = year_remaining *12

print(f"You have {day_remaining}days and {weeks_remaining}week and {month_remaining} month")
"""

"""
print("Welcome to the tip Calculator!")
bill = float(input("what was the total bill ? $"))
tip = int(input ("How much would you  like to give ? 10 , 12 , 15"))
people = int(input("How many people to split this bill ?"))
tip_as_percent = tip / 100
total_tip_amount = bill *tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2) 
print(f"Each person should pay{final_amount}")
"""