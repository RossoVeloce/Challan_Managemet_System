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
    print("permission denied")"""
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
  
tablecheck()
def challancheck():
  #Reg = input("Enter Vehicle Number")
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    cur.execute('select * from challans')
    print("Challans:(Police View)")
    for i in cur:
      print(list(i))
  except:
    print("Connection failed !!")
challancheck()