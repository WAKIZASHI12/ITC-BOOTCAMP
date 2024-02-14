# d
#список 

values = [1,"apple",{"a","b","c"},[1,2,3],(4,5,6)]
# список проверки
convertible_list =[]
for item in values:
    convertible = isinstance(item,(list,set,tuple,dict))
convertible_list.append(convertible)
can_covert = all(convertible_list)
# print("можно ли конвертировать values в set",can_covert)


spisok = set()
for i in range(5):
    number = int(input("ведите число"))
    spisok.add(number)
# print(min(spisok))



user = ()
# user_input =str(input("ведите функцию"))
if user_input =='print':
    print("fun print")
elif user_input == 'len':
    print("len")
elif user_input == 'input':
    print("input")
else:
    print("net")
""

while True:
    syma = float(input("ведите сумму займа(не меньше 50 000): "))
    if syma >= 50000:
        break
    else:
        print("сума должна быть  не мене 50000.")
interest_rate = 3.47
interest_amaut = syma*(interest_rate/100)
total = syma + interest_amaut
print("переплата составит:{:.2f}".format(total))


list()

numbers =  [10, 20, 30, 40, 50]
if numbers:#проверить не пуст ли список
    total =sum(numbers)
    aveng = total/len(numbers)
    print("srednie znachenie",aveng)
else:
    print("error")


try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)
except FileNotFoundError:
    print("Ошибка: файл не найден!")
except PermissionError:
    print("Ошибка: отсутствуют права доступа к файлу!")
except IsADirectoryError:
    print("Ошибка: указанный путь является директорией, а не файлом!")
except Exception as e:
    print(f"Произошла ошибка: {e}")




# Предположим, что значения переменных могут быть введены пользователем
numerator = input("Введите числитель: ")
denominator = input("Введите знаменатель: ")

try:
    result = float(numerator) / float(denominator)
    print("Результат деления:", result)
except ValueError:
    print("Ошибка: введены неверные данные! Пожалуйста, введите числовые значения.")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")


dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

for key in dict_.keys():
    try:
        print(key + 'abc')
    except TypeError:
        print(f"Ошибка: ключ '{key}' не является строкой!")
