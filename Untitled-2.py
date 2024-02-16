
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y

# Примеры использования функций
print(add(5, 3))       # Вывод: 8
print(subtract(10, 4)) # Вывод: 6
print(multiply(2, 6))   # Вывод: 12
print(divide(8, 2))     # Вывод: 4.0
print(divide(5, 0))     # Вывод: Ошибка: деление на ноль


def dsf(dict1,dict2):
    for key, value in dict2.items():
        dict1[key] = value
    return dict1

dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}

ds = dsf(dict1,dict2)
print(ds)


def order_food_and_drink():
    food = input("Что бы вы хотели заказать на еду? ")
    drink = input("Что бы вы хотели заказать на напиток? ")

    with open("menu.txt", 'w') as file:
        file.write(f"Заказ на еду: {food}\n")
        file.write(f"Заказ на напиток: {drink}\n")

    print("Ваш заказ был записан в файл menu.txt на рабочем столе.")


order_food_and_drink()




import os

def create_file_with_word(word):
    current_directory = os.path.dirname(file)
    file_patch = os.patch.join(current_directory, f"{word}.txt")

    with open(file_patch,'w') as file:
        file.write(f" создать фаил с именем: {word}.txt")
    print(f"Файл с именем '{word}.txt' был успешно создан в текущей директории.")
word = input("slovofile")
create_file_with_word(word)

def main_function():
    print("я главная функция")

    def nested_function():
        print("я вложеная функция")

    nested_function()

main_function()

def dsf(dict1):
    keys = tuple(dict1.keys())
    values = tuple(dict1.values())
    return keys,values
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_tuple, value_tuple = dsf(my_dict)
print("tuple",value_tuple)
print("keys",keys_tuple)




my_list = [1, 'mario',3.2]
def length():
    result = 0
    for _ in my_list:
        result += 1
    print(f"сьрока состоит из {0}".format(result))
length()




def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    num = int(input("Введите число: "))
    if is_prime(num):
        print(f"{num} - простое число")
    else:
        print(f"{num} - не является простым числом")

if __name__ == "__main__":
    main()

def dsf(dict1,dict2):
    return[dict1,dict2]
dict1 = 12
dict2 = "bakytkrasavchik"
result = dsf(dict1,dict2)
print(result)

def er():
    num = int(input("cislo"))
    for _ in range(num):
        print("er()")

er()





def format_salary(name, salary=5000):
    return f"{name.upper()} - {salary}"

def generate_list_of_elements():
    n = int(input("Введите число N: "))
    elements_list = list(range(1, n+1))
    return elements_list

# Пример использования первой функции
name = input("Введите имя пользователя: ")
salary = float(input("Введите зарплату пользователя (если не указана, будет установлена зарплата по умолчанию 5000): "))
result = format_salary(name, salary)
print(result)

# Пример использования второй функции
elements = generate_list_of_elements()
print("Сгенерированный список элементов:", elements)