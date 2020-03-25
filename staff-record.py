#%%
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

print(ekebo_etuk)
print('\n')

# %%
