# %%
import datetime as dt
from re import sub
import csv

name_list = open('name_list.csv', encoding='utf-8', newline='')
with name_list as nl:
    nl.readline()
    reader = enumerate(csv.reader(nl))
    for i, row in reader:
        #print(i, row)
        name = row[0].split(' ')
        first_name = name[0].strip()
        last_name = name[1].strip()
        phone_nos = row[1]
        print(last_name +', ' + first_name + ' ->> ' + phone_nos)

#print('Done')
#print('File is closed? ', nl.closed)
# %%
import datetime as dt
from re import sub
import csv

with open('zbar_acct_stmt.csv', encoding='utf-8', newline='') as zas:
    reader = enumerate(csv.reader(zas))
    zas.readline()
    for i, row in reader:
        #print(i, row)
        trans_date = dt.datetime.strptime(row[0],'%A, %d %B %Y').date()
        income_str = (row[1].replace('₦','').replace(',','')).strip()
        income = float(income_str or 0)
        inc_desc = row[2]
        expense_str = (row[3].replace('₦','').replace(',','')).strip()
        expense = float(expense_str or 0)
        exp_desc = row[4]
        bbf_str =  (row[5].replace('₦','').replace(',','')).strip()
        bbf = float(bbf_str or 0)
        print(f'{i:>3}', f'{trans_date:%B %d, %Y}', f'₦{income:<12,.2f}', f'{inc_desc:<30}', f'₦{expense:<12,.2f}', f'{exp_desc:<30}', f'₦{bbf:<12,.2f}')

print('Done')
    


# %%
