# %%
# Demo Point of Sales
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
