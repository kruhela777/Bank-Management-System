import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='12345',database='bank')
cur = conn.cursor()
cur.execute('create table user_table(username varchar(25) INT AUTO_INCREMENT,passwrd varchar(25),PRIMARY KEY(username) )')
print('1.REGISTER')
print('2.LOGIN')
n=int(input('enter your choice='))
if n== 1:
    name=input('Enter a Username=')
    passwd=int(input('Enter a 4 DIGIT Password='))
    V_SQLInsert="INSERT  INTO user_table (passwrd,username)     values (" +  str (passwd) + ",' " + name + " ') "
    cur.execute(V_SQLInsert)
    conn.commit()
    print('USER created succesfully')
if  n==2 :
    name=input('Enter your Username=')
    passwd=int(input('Enter your 4 DIGIT Password='))
    V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
    cur.execute(V_Sql_Sel)
if cur.fetchone() is  None:
    print('Invalid username or password')


