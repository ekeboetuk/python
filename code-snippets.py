# %% [markdown]
"""# MARKDOWN TEXT IN JUPYTERS NOTEBOOK


### Hello there, this is Ekebo Brown. For the next few days I'll be learning how to code with **Python** version while taking breaks in between to learn other codings that will make my studies more interesting it, like the ~~MarkDown~~ code. _The snippet above shows what I have been able to code so far being the elementary aspect of the lesson._ Stay tuned for updates and more  hardcore stuffs

- [ ] Jelly liquorice sweet roll tootsie roll I love cupcake.
- [ ] Lollipop sugar plum cake cake.
1. I love topping chocolate cake gummi bears gummi bears gummi bears.
1. I love chupa chups powder pie. 
1. Carrot cake dragée topping donut.  
1. Chocolate cake cupcake chupa chups lollipop candy canes cupcake.

[![Python Versions Logo](https://i7.pngguru.com/preview/481/959/714/django-python-computer-programming-programming-language-computer-software-python-logo-download.jpg)](https://www.python.com "Python Website")
"""

# %%
# Mathematical Operations
import math
import datetime

milo_packet = 2000
dettol_cool = 300
eva_water = 150

total = f"""
Bill of Quantity

=N= {milo_packet:>8,.2f} - Sachet Milo (Large)
=N= {dettol_cool:>8,.2f} - Dettol Cool (Big)
=N= {eva_water:>8,.2f} - Eva Bottle Water (Medium)
"""

teller_name = input("Enter Your First and Last Name: ")
space_index = teller_name.find(" ")
if space_index == -1:
    input("Please Enter Your First and Last Name: ")
else:
    last_name = teller_name[space_index + 1:len(teller_name)]
    first_initial = teller_name[0]

print(total)
print("Teller: " + last_name + ", " + first_initial + ".")
time_stamp = f"{datetime.datetime.now():%A %d.%m.%y %H:%M}"
print("Timestamp: " + str(time_stamp) + "\n")

week_number = int(f"{datetime.date.today(): %w}")
if week_number > 4:
    print("Happy Weekend Dear Customer!")
print(str.upper(str(week_number) + ": thank you shopping with us"))

# %%
