
lambda_multiply = lambda a, b, c: f"Объём бассейна {a * b * c}" 
 
result = lambda_multiply(2, 3, 4) 
print(result)  


lambda_days_remaining = lambda days_passed: f"До нового года осталось {365 - days_passed} дней." 
 

days_passed = 100 
result = lambda_days_remaining(days_passed) 
print(result)  


def print_odd_numbers(n):
    if n <= 0:
        return
    if n % 2 != 0:
        print(n)
    print_odd_numbers(n - 1)


print_odd_numbers(10)


def remove_element_from_set(input_set):
    if len(input_set) == 0:
        return
    print(f"Текущее множество: {input_set}")
    element = input_set.pop()
    print(f"Удаленный элемент: {element}")
    remove_element_from_set(input_set)

my_set = {1, 2, 3, 4, 5}
remove_element_from_set(my_set)



import random


def generate_random_numbers():
    return [random.randint(10, 50) for _ in range(100)]


def remove_duplicates_decorator(func):
    def wrapper():
        numbers = func()
        unique_numbers = list(set(numbers))
        return unique_numbers
    return wrapper


@remove_duplicates_decorator
def generate_unique_random_numbers():
    return generate_random_numbers()


unique_numbers = generate_unique_random_numbers()
print(unique_numbers)

# Функция для запроса логина и пароля у пользователя
def get_credentials():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password

# Декоратор для шифрования данных
def encrypt_credentials(func):
    def wrapper():
        login, password = func()
        encrypted_login = ''.join(chr(ord(c) + 1) for c in login)
        encrypted_password = ''.join(chr(ord(c) + 1) for c in password)
        return encrypted_login, encrypted_password
    return wrapper

# Применение декоратора к функции
@encrypt_credentials
def get_encrypted_credentials():
    return get_credentials()


encrypted_login, encrypted_password = get_encrypted_credentials()
print("Зашифрованный логин:", encrypted_login)
print("Зашифрованный пароль:", encrypted_password)





lambda_multiply = lambda x: x * 1.185
numbers = [1745345, 98726, 439872634, 7312, 64872, 123687126, 9312, 4124, 231, 3123, 34, 3453]

result = [lambda_multiply(num) for num in numbers]
print(result)
\