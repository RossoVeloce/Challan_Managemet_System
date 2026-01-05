# Imports
import mysql.connector as m
import random
print("Hello, World!")

def check(Reg):
  db = m.connect(host="localhost",user="root",database="_")
  cur = db.cursor()
  cur.execute('select vehicle_ID from vehicle_details')
  M = []
  for i in cur:
    M.extend(list(i))
  if str(Reg) in M:
    return("Y")
  else:
    return("N")

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

    input("\nPress Enter to continue: ")
  except:
    print("Connection failed !!")
    input("Press Enter to continue: ")

def challancheck():
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    cur.execute('select * from challans')
    print("|Vehicle ID| |Driver ID| |Pending Challans| |Past Challans|")
    for i in cur:
      print(list(i)) #ISSUE: Format is wrong

    input("\nPress Enter to continue: ")
  except:
    print("Connection failed !!")
    input("\nPress Enter to continue: ")

def specificcheck():
  Reg = str(input("Enter Vehicle Number: "))
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    Reg = "SELECT * FROM `challans` WHERE`Vehicle_ID`= '{}'".format(Reg)
    cur.execute(Reg)
    print("|Vehicle ID| |Driver ID| |Pending Challans| |Past Challans|")
    for i in cur:
      print(list(i)) #ISSUE: Formatting is wrong

    input("\nPress Enter to continue: ")
  except:
    print("Connection failed !!")
    input("\nPress Enter to continue: ")

def add_chalan():
  # Reg = input("Enter Vehicle Number")
  try:
    db = m.connect(host="localhost", user="root", database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    cur.execute('select Vehicle_ID, Driver_Name from vehicle_details')
    Reg = ""
    print("Vehicles are:")
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
        M = input(i)
        Reg = Reg+check(M)
        val.append(M)
    if Reg == "YN" or Reg =="YY":
      val = tuple(val)
      print(f"New challan details are: {val}")
      input("\nPress Enter to continue: ")
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
    else:
      print("Invalid Vehicle ID !")
    input("\nPress Enter to continue: ")
  except:
    print("Connection failed !!")
    input("\nPress Enter to continue: ")

def removechallan():
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    Reg = "SELECT * FROM `challaninfo`"
    cur.execute(Reg)
    print("|Vehicle ID|","\t|Challan ID|","\t|Reason|","\t|Mode|","\t|Status|")
    for i in cur:
      print(list(i))
    M = int(input("Enter Challan ID: "))
    Reg = "UPDATE challaninfo SET Status= 'INACTIVE' WHERE `Challan_ID` = '{}';".format(M)
    cur.execute(Reg)
    Reg = "SELECT `Vehicle_ID` FROM `challaninfo` WHERE `Challan_ID`='{}';".format(M)
    cur.execute(Reg)
    M = str(M)
    for i in cur:
      M = list(i)
    M = M[0]
    Reg = "UPDATE `challans` SET Pending_Challans= Pending_Challans-1,Past_Challans=Past_Challans+1 WHERE `Vehicle_ID` = '{}' AND Pending_Challans>0;".format(M)
    cur.execute(Reg)
    db.commit()
    print("Change Success")
    #for i in cur:
      #print(list(i))
  except:
    print("Connection failed !!")

def add_vehicle():
  try:
    db = m.connect(host="localhost",user="root",database="_")
    print("Successfully connected :)")
    cur = db.cursor()
    Reg = int(input("Enter vehicle number: "))
    M = int(input("Enter Driver ID: "))
    val = input("Enter Driver Name")
    cur.execute("INSERT INTO `vehicle_details` (`Vehicle_ID`, `Driver_ID`, `Driver_Name`) VALUES ('{}', '{}', '{}')".format(Reg,M,val))
    cur.execute("INSERT INTO `challans`(`Vehicle_ID`, `Driver_ID`, `Pending_Challans`, `Past_Challans`) VALUES ('{}','{}','0','0')".format(Reg,M))
    db.commit()
  except:
    print("Connection failed !!")
    

#User Interface
while True:
  Opinion = input("\nWhat would you like to do ? (integer input) \n 1.Tablecheck \n 2.Check all challans \n 3.Check your challans \n 4.Remove challan \n 5.Add challan \n 6.Add vehicle \n -->")
  if Opinion == '1' or Opinion.lower() == 'tablecheck':
    tablecheck()
    print() #formating
  elif Opinion == '2':
    challancheck()
  elif Opinion == '3':
    specificcheck()
  elif Opinion == '4' or Opinion.lower() == 'remove challan':
    removechallan()
  elif Opinion == '5' or Opinion.lower() == 'add challan':
    add_chalan()
  elif Opinion == '6' or Opinion.lower() == 'add vehicle':
    add_vehicle()
  else:
    print("Exiting")
    break