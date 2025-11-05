# Admin Identification sys
print("Hello, World!")
Admin = {"apoorva": "Apass", "himanshu": "Bpass"}
U = input("Enter Username ")
if U.lower() in Admin:
  P = input("enter Password ")
  if P == (Admin[U.lower()]):
    print("permission given")
  else:
    print("permission denied")
