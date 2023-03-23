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
    # cur.execute("create database EEwarehouse")
    # dbs = cur.execute("create table warehouse_controller(Year varchar(20) not null, "
    #     + "Month varchar(10) not null, Day varchar(10) not null, "
    #     + "PartNumber varchar(20) not null, BeckhoffPart varchar(20) not null, "
    #     + "Quantity varchar(20) not null, Purpose varchar(20) not null, "
    #     + "POnumber varchar(20) not null, IPJnumber varchar(20), "
    #     + "RFQnumber varchar(20) not null, Position varchar(20) not null,"
    #     + "NoteDLSupporter varchar(40), NoteSystem varchar(20))")
    
    # cur.execute("alter table warehouse_controller add ID varchar(20) not null")

    #Delete column
    # cur.execute("ALTER TABLE warehouse_controller DROP COLUMN ID")

    sql = "update warehouse_controller SET NoteSystem = %s WHERE Position = %s and PartNumber = %s"
    val = ("","G1","EL3692")
    #insert value to database
    cur.execute(sql,val)
    #commit value
    myconn.commit()

except:
    myconn.rollback()

myconn.close()

 
