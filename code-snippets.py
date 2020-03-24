# %%
# Demo Point of Sales
import math
import datetime

milo_packet = 2000
dettol_cool = 300
eva_water = 1500

total = f"""
Bill of Quantity

=N= {milo_packet:>8,.2f} - Sachet Milo (Large)
=N= {dettol_cool:>8,.2f} - Dettol Cool (Big)
=N= {eva_water:>8,.2f} - Eva Bottle Water (Medium - 1 Carton)
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
print(str.upper("thank you shopping with us"))
print(str.upper("come again next time \n"))


# %%
import datetime

ict_staff = {
    'ekebo.etuk':'Ekebo Brown Etuk',
    'mary.abraham':'Mary Ekereobong Abraham',
    'uduakobong.ituen':'Uduakobong Ituen',
    'abasiubong.itama':'Abasiubong Itama',
    'isreal.ekanim':'Isreal George Ekanim'
}

qa_staff = {
    'edima.ubon':'Edima Ubon Jerry',
    'rose.genesis': 'Rose Genesis',
    'nsisong.akwaowo':'Nsisong Akwaowo',
    'ezekiel.ekoi':'Ezekiel Ekoi'
}

engr_staff = ict_staff.copy()

engr_staff.update(qa_staff)

for username, fullname in engr_staff.items():
    print(username + ": " + fullname)

print("\nEnd of List\n")

search = input("Enter UserID To Search: ")
print(ict_staff.get(search,'\nNo such staff in ICT, expanding search scope...\n'))
print(engr_staff.get(search,'\nNo such staff in Engineering, try again with a difference userID') + ' in Engineering\n')



# %%
