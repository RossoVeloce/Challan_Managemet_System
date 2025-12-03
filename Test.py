# Imports
import mysql.connector as m
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
INSERT INTO `challans` (`Vehicle ID`, `Driver ID`, `Pending Challans`, `Past Challans`) VALUES ('0987654321', '1000000000', '7', '3') """
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
  except:
    print("Connection failed !!")
  
def challancheck():
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    cur.execute('select * from challans')
    print("Challans:")
    for i in cur:
      print(list(i))
  except:
    print("Connection failed !!")

def specificcheck():
  Reg = str(input("Enter Vehicle Number: "))
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    Reg = "SELECT * FROM `challans` WHERE`Vehicle ID`= '{}'".format(Reg)
    cur.execute(Reg)
    print("Challans:")
    for i in cur:
      print(list(i))
  except:
    print("Connection failed !!")

#User Interface
while True:
  Opinion = int(input("What would you like to do ? (integer input) \n 1.Tablecheck \n 2.Check all challans \n 3.Check your challans \n"))
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
  else:
    print("Exiting")
    break