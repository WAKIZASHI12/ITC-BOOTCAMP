"""
for i in range(1,11):
     print(i)

num = 1
while num <= 5:
    print(num ** 2)
    num +=1

for i in range(2,20,2):
    print(i)
"  
a = int(input("Vvedite chislo"))
while a > 0:
    print(a ** 2)
if a <= 0:
    print(False)
else:
    print(False)
""
ter = ['banana', 'apple','toktosum']
for i in ter:
    print(i.upper())




user_input = int(input("Vvedite chislo"))
factorial = 1

while user_input > 0:
    factorial *= user_input
    user_input -= 1
    print(factorial)



a = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
numbers = []
letters = []
for i in a:
    if str(i).isdigit():
        numbers.append(int(i))
print(numbers)
for y in a:
    if str(y).isalpha():
        letters.append(y)
print(letters)


a = int(input("Vvedite chislo"))
multiplier = 1
while multiplier <= 10:
    result = a * multiplier
    print(result)
    multiplier += 1


word = " python"
for leitter in word:
    print(leitter)


num = int(input("vedite cislo"))
sum_result = 0
currect_number = 1
while currect_number <= num:
      sum_result += currect_number
      currect_number += 1
print(sum_result)

numbers_list = [1, 3, 5, 9, 12, 15, 18, 20]
for number in numbers_list:
    if number % 3 == 0:
         print(number)


while True:
    user_input = input("Vvedite chislo: ")
    if user_input.isdigit():
        print(int(user_input)**2)
    else:
        break
"""
rows = 50

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

