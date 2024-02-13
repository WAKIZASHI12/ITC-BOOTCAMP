users = []
passwords = []
# 1. Зарегистрируйте пользователя
login_reg = input("Введите логин для регистрации: ")
password_reg = input("Введите пароль для регистрации: ")
# индекс пользавателя users и индекс passwords одинаковы
users.append(login_reg)
passwords.append(password_reg)
print("Пользователь зарегистрирован.")

# 2. Попросите пользователя войти
login_login = input("Введите логин для входа: ")
password_login = input("Введите пароль для входа: ")

# 3. Проверка данных
if login_login in users:
    user_index = users.index(login_login)
    if password_login == passwords[user_index]:
        print("ДОБРО ПОЖАЛОВАТЬ!")
else:
    print("Неправильный логин или пароль.")

