
num = float(input("num: "))
squar = num ** 2
print(f"lvadrat{num} raven {squar}")
a = 12345
b = 2134567
c = 154672345
print((a+b+c)/3)



num1 = float(input("cislo"))
num2 = float(input("cislo2"))
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
print(f"Сумма: {sum_result}")
print(f"Разность: {difference_result}")
print(f"Произведение: {product_result}")
print(f"Частное: {quotient_result}")

numbers = [2, 4, 6, 8, 10]
sum = 0
for number in numbers:
    sum += number
print(f"сума чисел:{sum}")




import os
import random
import string

os.makedirs("fool", exist_ok=True)
import random

for i in range(5):
    os.system(f"touch fool/{random.randint(1, 100)}.txt")







import sys

a = int(input("Введите значение а: "))

b = int(input("Введите значение в: "))

if sys.getsizeof(a) > sys.getsizeof(b): 
    print("Значение а занимает больше памяти.")

elif sys.getsizeof(a) < sys.getsizeof(b):
    print("Значение в занимает больше памяти.")

else:
    print("Значения а и в занимают одинаковый объем памяти.")


import random

choices = ["rock", "paper", "scissors"]

user = input("choice :")
computer = random.choice(choices)
print(user)
print(computer)

if user == computer:
    print("draw")

elif user == "rock" and computer == "scissors":
    print("win")

elif user == "scissors" and computer == "paper":
    print("win")

elif user == "paper" and computer == "rock":
    print("win")

else:
    print("loose")


import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
number_one = []
number_two = []
number_three = []
number_four = []

currect_number = number_one
while names:
    player = random.choice(names)
    currect_number.append(player)
    names.remove(player)

    if currect_number == number_one:
        currect_number = number_two

    elif currect_number == number_two:
        currect_number = number_three

    elif currect_number == number_three:
        currect_number = number_four

    elif currect_number == number_four:
        currect_number = number_one


print(number_one)
print(number_two)
print(number_three)
print(number_four)

import string
import random

def generate_password(n):
    symbols = string.ascii_letters + string.digits
    return "".join(random.choice(symbols) for i in range(n))

N = int(input("Введите количество символов для пароля: "))
password = generate_password(N)
print(f"Сгенерированный пароль длиной {N} символов: {password}")

import sys

def main():
    for arg in sys.argv[1:]:
        print(arg)

if __name__ == "__main__":
    main()


import random

