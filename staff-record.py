#%%
import datetime

class Staff:
    """ Plant Staff Class """
    def __init__ (self,fullname,employment_date,unit,id):
        self.fullname = fullname
        self.employment_date = employment_date
        self.unit = unit
        self.id = id

ekebo_etuk = Staff('Ekebo Brown Etuk','2018,9,1','ICT','IPC\\202\\2018')
employed = datetime.datetime.strptime(ekebo_etuk.employment_date,'%Y,%m,%d')
#print(f"{employed.date(): %d-%b-%y}")

with open('Family.txt',newline='') as fam:
    f = fam.readline()
    while f:
        values = f.split(',')
        for i, n in enumerate(values):
            if(i==0):
                print(f'{n:>5}',end='')
            else:
                print(f'{n:<18}',end='')
        print('\n')
        f = fam.readline()

staff_details = {
    'name':'',
    'id':'IPC/',
    'grade_level':'Grade 08 Level 06',
    'date_of_employment':'2006,01,01',
    'department':'',
    'unit':'',
    'supervisor':'',
    'transferred_from':'',
    'date_of_transfer':'',
    'entitlements':['leave','medical','wardrope','thirteen_month']
}

ekebo_etuk_details = ['Ekebo Brown Etuk','IPC/2018/223','Grade 08 Level 05','2018,9,1','Engineering','ICT','Isreal Ekanim','None','None',['22 Days Annual, 7 Days Casual & Sick leave',300000,1000000,122000]]

ekebo_etuk = dict.fromkeys(staff_details.keys())
# %%
