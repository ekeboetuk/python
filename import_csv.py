# %%
import datetime as dt
from re import sub
import csv

name_list = open('name_list.csv', encoding='utf-8', newline='')
with name_list as nl:
    nl.readline()
    reader = enumerate(csv.reader(nl))
    print('\n')
    for i, row in reader:
        #print(i, row)
        name = row[0].split(' ')
        first_name = name[0].strip()
        last_name = name[1].strip()
        phone_nos = row[1]
        fullname_sur = last_name +', ' + first_name
        print(f'{fullname_sur:<40}', phone_nos)

#print('Done')
#print('File is closed? ', nl.closed)
# %%
import datetime as dt
from re import sub
import csv, json

records = {}

with open('zbar_acct_stmt.csv', encoding='utf-8', newline='') as zas:
    reader = enumerate(csv.reader(zas))
    zas.readline()
    heading = f"""
    \n{'S/N':^5}{'TRANS DATE':<20}{'INCOME':>10}{'DESCRIPTION':^20}{'EXPENSES':>10}{'DESCRIPTION':^20}{'BALANCE':>12}"""
    print(heading)
    print('-'*100)
    total_income = 0
    total_expense = 0
    for i, row in reader:
        #print(i, row)
        trans_date = dt.datetime.strptime(row[0],'%A, %d %B %Y').date()
        income_str = (row[1].replace('₦','').replace(',','')).strip()
        income = float(income_str or 0)
        total_income += income
        inc_desc = row[2]
        expense_str = (row[3].replace('₦','').replace(',','')).strip()
        expense = float(expense_str or 0)
        total_expense += expense
        exp_desc = row[4]
        bbf_str =  (row[5].replace('₦','').replace(',','')).strip()
        bbf = float(bbf_str or 0)
        f_income = '₦'+f'{income:,.2f}'
        f_expense = '₦'+f'{expense:,.2f}'
        f_bbf = '₦'+f'{bbf:,.2f}'
        trans_date = f'{trans_date:%B %d, %Y}'
        if income == 0:
            f_income = ''
        if expense == 0:
            f_expense = ''
        #print(f'{i+1:^5}{trans_date:<20}{f_income:>10}{inc_desc[0:18]:^20}{f_expense:>10}{exp_desc[0:18]:^20}{f_bbf:>12}')

        records[i+1] = dict({'trans_date':trans_date,'income':income,'inc_desc':inc_desc,'expense':expense,'exp_desc':exp_desc,'bbf':bbf})

j_dump = json.dumps(records, indent=6)
print(j_dump)
with open('record_dump.json', 'w', encoding='utf-8') as of:
    json.dump(records, of, ensure_ascii=False)
print('\n')
print(f"{'Total Income = ':>20}", f'₦{total_income:,.2f}')
print(f"{'Total Expenses = ':>20}", f'₦{total_expense:,.2f}')
print(f"{'Balance = ':>20}", f'₦{total_income-total_expense:,.2f}')
    


# %%
