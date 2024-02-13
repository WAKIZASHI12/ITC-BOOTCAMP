"""
a = input("log or reg: ")
with open("database.txt","r") as db:
    db = db.read()

if a == 'log':
    user_username = input("your username: ")
    user_password = input("your password: ")
    user_datas = db.split(";")
    for user_data in user_datas:
        username,password = user_data.split(",")
        if username.strip("\n") == user_username and password.strip("\n") == user_password:
            print("wellcom")
            exit()
elif a == 'reg':
    user_username = input("your username: ")
    user_password = input("your password: ")
    user_datas = db.split(";")
    for user_data in user_datas:
        username,password = user_data.split(",")
        if username("\n") == user_username:
           print("no")
           exit()
with open("database.txt","a") as database:
    database.write(f"{user_username} {user_userpassword}: ")
print("luck")
"""





login = input("Введите логин: ")
password = input("Введите пароль: ")
photo_path = input("Укажите путь к фото: ")

valid_extensions = ['jpeg', 'jpg', 'png']

# Проверка расширения файла
if photo_path.endswith(tuple(valid_extensions)):
    # Проверка существования файла
    file_exists = False
    try:
        with open(photo_path, 'rb'):
            file_exists = True
    except FileNotFoundError:
        pass

    if file_exists:
        # Запись информации о пользователе
        with open('registered_users.txt', 'a') as users_file:
            users_file.write(f"Логин: {login}, Пароль: {password}, Путь к фото: {photo_path}\n")
        print("Регистрация успешна!")
    else:
        print("Файл не найден.")
else:
    print("Неверный путь к фото или неподдерживаемое расширение.")

