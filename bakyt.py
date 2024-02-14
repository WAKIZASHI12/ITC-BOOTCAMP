from os import write


login = input("log: ")
password = input("password: ")
photo = input("photo: ")

if photo.lower().endswith((".jpeg", ".jpg", ".png")):
   with open("database.txt","a") as data:
      data.write(f"{login},{password},{photo}: ")
      print("ura")
else:
   print("no")
