# age =70
#
# if age < 18:
#    print("under age")
#    print("You are too young")
# else:
#     print("Over age")
#
# name = input("Enter your name")
# age = int(input("Enter your age"))
#
# result = age + 10
#
# print(result)

# weight
# height

# bmi

# print bmi

# status
from math import pow

name = input("Enter your name:")
weight = int(input("Enter weight in kg"))
height = float(input("Enter your height in meters"))
bmi = height ** 2
bmi2 = weight / bmi

print(bmi2)

if bmi2 <= 15:
    print("You are very severly Underweight!")
elif bmi2 >= 15 and bmi2 <= 16:
    print("You are severly underweight")
elif bmi2 >= 16 and bmi2 <= 18.5:
    print("You are underweight")
if bmi2 >= 18.5 and bmi2 <= 25:
    print("Normal (health weight")
if bmi2 >= 25 and bmi2 <= 30:
    print("Overweight")
if bmi2 >= 30 and bmi2 <= 35:
    print("Obese Class I (Moderately obese)")
if bmi2 >= 35 and bmi2 <= 40:
    print("Obese Class II (Severely obese) ")
if bmi2 >= 40 and bmi2 <= 45:
    print("Obese Class III (Very severely obese)")
if bmi2 >= 45 and bmi2 <= 50:
    print("Obese Class IV (Morbidly Obese)")
if bmi2 >= 50 and bmi2 <= 60:
    print("Obese Class V (Super Obese) ")
if bmi2 > 60:
    print("Obese Class VI (Hyper Obese) ")
