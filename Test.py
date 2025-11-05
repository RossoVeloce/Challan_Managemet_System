# Imports
import mysql.connector as m
# Admin Identification sys
print("Hello hitmanshu")
print("Hello, World!")
Admin = {"apoorva": "Apass", "himanshu": "Bpass"}
U = input("Enter Username ")
if U.lower() in Admin:
  P = input("enter Password ")
  if P == (Admin[U.lower()]):
    print("permission given")
  else:
    print("permission denied")

def challancheck():
  Reg = input("Enter Vehicle Number")
  db = m.connect(localhost="host",user="root",pwd="",database="_")