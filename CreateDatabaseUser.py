import mysql.connector
   
#Create the connection object
myconn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "ontuquocdat", database = "eewarehouse_update2")
   
#printing the connection object
print(myconn)

#tao cursor
cur = myconn.cursor()
# sql = ("insert into Beckhoff(module, quantity, purpose, note, position) "
#     + "values (%s, %s, %s, %s, %s)")

# val = ("EK1100", 100, "Spare", "PBP", "A3")

#Step 1
# cur.execute("create database EEwarehouse_update2")

#Step 2
try:
    # Time + Module + BeckhoffPart + Quantity + Purpose + POnumber + IPJnumber + RFQnumber + Position + NoteDLSupporter + NoteSystem
    # dbs = cur.execute("create table UserAccount(Initial varchar(20) not null, "
    #     + "DefaultPass varchar(20) not null, NewPass varchar(20) not null, "
    #     + "UpdateNote varchar(20) not null)") 

    # cur.execute("alter table UserAccount add Role varchar(20) not null")

    #Delete column
    # cur.execute("ALTER TABLE warehouse_controller DROP COLUMN ID")

    #Delete content
    # cur.execute("delete from UserAccount where ID = 21")


    #insert value to database
    # cur.execute(sql,val)
    #commit value
    myconn.commit()

except:
    myconn.rollback()

myconn.close()

 
