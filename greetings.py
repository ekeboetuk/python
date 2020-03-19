# %%
import datetime

print("Good morning user. Please supply us with your: ")

names = input("Full Names: ")
dob = input("Date of Birth (YYYY-M-D): ")
date_of_birth = datetime.date(1985, 6, 20)
age = datetime.date.today() - date_of_birth

print("Welcome " + names + ", \nwe are pleased to meet you")
print("You are  " + str(age.days//365) + " years and " + str((age.days%365)//30) + " months old!")

# %%
