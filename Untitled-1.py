п
some_list = ["bakyt", "Iphone", "macbook", "apple"]

def reverse_list():
    middle = len(some_list) // 2
    return some_list[:middle][::-1] + some_list[middle:][::-1]

print(reverse_list())
print(some_list[::-1])

def generate_fibonacci(n):
    fibonacci_numbers = [1, 1]
    for i in range(2,n):
        next_number = fibonacci_numbers[i-1]+fibonacci_numbers[i-2]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers
fibonacci_sequence = generate_fibonacci(10)
print(fibonacci_sequence)




def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def call_functions(a, b):
    sum_result = addition(a, b)
    difference = subtraction(a, b)
    return sum_result, difference
a = 4
b = 3
result = call_functions(a,b)
print("sum:",result[0])
print("difference:",result[1])





def create_file(filename):
    with open(filename, 'w') as file:
        file.write("This is a new file created by the user.")
filename = input("Введите имя файла: ")
function_name = create_file

function_name(filename)

import random

def gen_number():
    prefix = "0444"
    number = prefix + ''.join(random.choice('145790') for _ in range(6))
    return number

# Пример использования функции для генерации номера
phone_number = gen_number()
print(phone_number)