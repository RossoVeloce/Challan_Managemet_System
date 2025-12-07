# Imports
import mysql.connector as m
import random
# Admin Identification sys
print("Hello hitmanshu")
print("Hello, World!")
"""Admin = {"apoorva": "Apass", "himanshu": "Bpass"}
U = input("Enter Username ")
if U.lower() in Admin:
  P = input("enter Password ")
  if P == (Admin[U.lower()]):
    print("permission given")
  else:
    print("permission denied")

ADD new values to table using:
INSERT INTO `challans` (`Vehicle_ID`, `Driver _D`, `Pending_Challans`, `Past_Challans`) VALUES ('0987654321', '1000000000', '7', '3') 

Create Table ChallanInfo
(Vehicle_ID varchar(10)NOT NULL UNIQUE,
 Challan_ID char(10) NOT NULL UNIQUE,
 Reason varchar(255)NOT NULL UNIQUE,
 Mode ENUM('MANUAL','AUTOMATED'),
 FOREIGN KEY (Vehicle_ID) REFERENCES vehicle_details(Vehicle_ID)
 ON UPDATE CASCADE ON DELETE CASCADE);
"""

def tablecheck():
  #Reg = input("Enter Vehicle Number")
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    cur.execute('show tables')
    print("Tables Available:",end=" ")
    for i in cur:
      print(list(i),end='')

    input()
  except:
    print("Connection failed !!")
    input()

def challancheck():
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    cur.execute('select * from challans')
    print("Challans:")
    for i in cur:
      print(list(i))

    input()
  except:
    print("Connection failed !!")
    input()

def specificcheck():
  Reg = str(input("Enter Vehicle Number: "))
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    Reg = "SELECT * FROM `challans` WHERE`Vehicle_ID`= '{}'".format(Reg)
    cur.execute(Reg)
    print("Challans:")
    for i in cur:
      print(list(i))

    input()
  except:
    print("Connection failed !!")
    input()


def add_chalan():
  # Reg = input("Enter Vehicle Number")
  try:
    db = m.connect(host="localhost", user="root", database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    cur.execute('select * from challaninfo')
    print("Challans:")
    for i in cur:
      print(list(i))
    val = []
    random_10_digit_number = random.randint(1000000000, 9999999999)
    modes = ["MANUAL", "AUTOMATED"]
    mode = random.choice(modes)
    for i in ["Vehicle_ID: ", "Chalan_ID: ", "Reason: ", "Mode: "]:
      if i == "Chalan_ID: ":
        val.append(str(random_10_digit_number))
      elif i == "Mode: ":
        val.append(str(mode))
      else:
        val.append(input(i))
    val = tuple(val)
    print(f"New challan details are: {val}")
    input()
    bleh = (f"INSERT INTO `challaninfo` VALUES (%s, %s , %s, %s, 'ACTIVE');")
    cur.execute(bleh, val)
    val = val[0]
    bleh = "SELECT COUNT(*) FROM challaninfo WHERE `Vehicle_ID`='{}' AND `Status`='ACTIVE';".format(val)
    cur.execute(bleh)
    for i in cur:
      M = list(i)
    M = M[0]
    bleh = "UPDATE `challans` SET Pending_Challans= {},Past_Challans=Past_Challans WHERE `Vehicle_ID` = '{}';".format(M,val)
    cur.execute(bleh)
    db.commit()
    cur.execute('select * from challaninfo')
    print("Challans:")
    for i in cur:
      print(list(i))
    input()
  except:
    print("Connection failed !!")
    input()

def removechallan():
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    M = int(input("Enter Challan ID: "))
    Reg = "UPDATE challaninfo SET Status= 'INACTIVE' WHERE `Challan_ID` = '{}';".format(M)
    cur.execute(Reg)
    Reg = "SELECT `Vehicle_ID` FROM `challaninfo` WHERE `Challan_ID`='{}';".format(M)
    cur.execute(Reg)
    M = str(M)
    for i in cur:
      M = list(i)
    M = M[0]
    print (M,type(M))
    Reg = "UPDATE `challans` SET Pending_Challans= Pending_Challans-1,Past_Challans=Past_Challans+1 WHERE `Vehicle_ID` = '{}' AND Pending_Challans>0;".format(M)
    cur.execute(Reg)
    db.commit()
    print("Change Success")
    #for i in cur:
      #print(list(i))
  except:
    print("Connection failed !!")

#User Interface
while True:
  Opinion = int(input("What would you like to do ? (integer input) \n 1.Tablecheck \n 2.Check all challans \n 3.Check your challans \n 4.Remove challan \n 5.Add challan \n "))
  if Opinion == 1:
    tablecheck()
    print() #formating
    print() #formatting
  elif Opinion == 2:
    challancheck()
    print() #formatting
  elif Opinion == 3:
    specificcheck()
    print() #formatting
  elif Opinion == 4:
    removechallan()
    print() #formatting
  elif Opinion == 5:
    add_chalan()
    print()  # formatting
  else:
    print("Exiting")
    break