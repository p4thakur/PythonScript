#Script to make sql update statement from csv
import pandas

df = pandas.read_excel('DeactiveAccount_correctAccount.xls')

list1=df.columns.ravel();
#print(df['account_number'].tolist())
lenderResponse= df['lender_response'];
modification=df['account_modification_time'];
accountnumber=df['account_number'];
print(len(accountnumber))
for i in range(len(accountnumber)):
  a='update accounts set lender_response=\''+str(lenderResponse[i])+ '\',account_modification_time=\''+str(modification[i])+'\' where account_number=\''+str(accountnumber[i])+'\';'
  f = open("demo.txt", "a")
  f.write(a)
  f.write("\n")
  
  
  /******
  # #Script to make sql update statement from csv
# import pandas

# df = pandas.read_excel('dueAmount.xls')

# list1=df.columns.ravel();
# #print(df['account_number'].tolist())
# due_date= df['due_date'];
# accountnumber=df['account_number'];
# print(len(accountnumber))
# for i in range(len(accountnumber)):
#   a='update accounts set due_date=\''+str(due_date[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'
#   f = open("demo.txt", "a")
#   f.write(a)
#   f.write("\n")
#Script to make sql update statement from csv
import pandas

df = pandas.read_excel('dueAmount.xls')

list1=df.columns.ravel();
#print(df['account_number'].tolist())
due_date1= df['due_date'];
accountnumber=df['account_number'];
print(len(accountnumber))
for i in range(len(accountnumber)):
  # a='update accounts set due_date=\''+str(due_date[i])+ '\' where account_number=\''+str(accountnumber[i])+'\';'
  a='INSERT INTO manual_update_audit (loan_account_number,`column`, `table`, update_type, old_value, new_value) '\
     'SELECT account_number, "due_date","accounts", "UPDATE", '\
     'JSON_OBJECT( "due_date",due_date ),JSON_OBJECT( "due_date",\''+str(due_date1[i])+'\') FROM accounts '\
      'where account_number=\''+str(accountnumber[i])+'\';'
  f = open("manualAudit.txt", "a")
  f.write(a)
  f.write("\n")
  ********/
