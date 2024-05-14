import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='12345',database='bank')
if conn.is_connected():
    print('connected succesfully')
cur = conn.cursor()
cur.execute('create table c(acct_no INT AUTO_INCREMENT,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(25),cr_amt float, PRIMARY KEY(acct_no) )')
