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
  
