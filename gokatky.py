xxxxxxxxxxxxxxxxxxxxxxx"""
with open("python.txt", "w") as file:
    file.write("Python is a high-level programming language.\n"
               "It is known for its simplicity and readability.\n"
               "Python's syntax allows developers to write fewer lines of code.\n"
               "This makes it an ideal language for beginners and experts alike.\n"
               "Python has a large community and extensive documentation.\n")


t_words = []
with open("python.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if 't' in word.lower():
                t_words.append(word)


print("Слова, содержащие букву 't' или 'T':")
for word in t_words:
    print(word)

file = open("directories.txt", "r")
file_content_by_lines = file.readlines()
print(file_content_by_lines)

login = input("Vvedite login: ")
password = input("Vvedite password: ")
with open("users.txt", "a") as file:
    file.write(f"{login} {password}\n")

file = open("wwwww.txt","r")
read = file.read()
if 'w' in read:
    print('W - est')
else:
    print('W - net')
file.close()


a = input("Войти или Рег : ")

with open("database.txt","r") as db:
  db = db.read()

if a =='Войти':
   user_username = input("your username: ")
   user_password = input("your password: ")
   user_datas = db.split(";")
   for user_data in user_datas:
     username, password = user_data.split(',')
     if username.strip("\n") == user_username and pasword.strip("\n") == user_pasword:
        print("Добро пожаловать")
        exit()

elif a == 'Рег':
    user_username = input("your username: ")
    user_password = input("your password: ")
    user_datas = db.split(";")

    for user_data in user_datas:
        username, password = user_data.split(',')
        if username.strip("\n") == user_username:
            print("такой username есть")
            exit()
    with open("databese.txt","a") as databese:
      database.wirie(f";{user_username},{user_password},{user_photo_patch}")
      print("Успех")
"
login = input("ведите логин: ")
pssword = input("ведите пороль: ")
photo_pathc = input("ведите путь к фото: ")

if photo_name.lower().endswith((".jpeg", ".jpg", ".png")):

    with open("registered_users.txt", "a") as file:
        file.write(f"Логин: {login}, Пароль: {password}, Имя файла фото: {photo_name}\n")
    print("Регистрация успешна!")
else:
    print("Ошибка: Неверное расширение файла фото.")
""
path_a = input("Введите путь до картинки которую меняете: ")
path_b = input("Введите путь до картинки на которую меняете: ")

if os.path.exists(path_a):
    if os.path.isfile(path_a):
        if os.path.exists(path_b):
            if os.path.isfile(path_b):
h                with open(path_a, "w") as file:
                    file.write(path_b)
        else:
            print("Картинка на которую необходимо изменть не найдена!")
else:
    print("Картинка которую необходимо измениь не найдена!")
""
a = input("log reg: ")

with open("database.txt","r") as db:
  db = db.read()

if a =='log':
   user_username = input("your username: ")
   user_password = input("your password: ")
   user_datas =db.split(";")
   for user_data in user_datas:
     username,password = user_data.split(",")
     if username.split("\n") == user_username and password.strip("\n") == user_password:
        print("wellcom")
        exit()
elif a =='reg':
   user_username = input("your username: ")
   user_password = input("your password: ")
   user_datas = db.split(";")
   for user_data in user_datas:        
     username,password = user_data.split(",")
     if username.split("\n") == user_username:
        print("такой username есть")
        exit()
   with open("database.txt","a") as database:
     database.write(f";{user_username},{user_password}")
     print("luck")
"""
