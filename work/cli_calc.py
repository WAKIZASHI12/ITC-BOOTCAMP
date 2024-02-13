available_operations = ['+','-','/','*','**','//','%']
print("Available math operations:" + " ".join(available_operations))
# Запрашиваем вводные данные
operation = input('Please enter math operation: ')
first_number = input('Enter first digit: ')
second_number = input('Enter second digit: ')

# Находим необходимую операцию
if operation == '+':
    print(int(first_number) + int(second_number))
elif operation == '-':
    print(int(first_number) - int(second_number))
elif operation == '/':
    print(int(first_number) / int(second_number))
elif operation == '*':
    print(int(first_number) * int(second_number))
elif operation == '**':
    print(int(first_number) ** int(second_number))
elif operation == '//':
    print(int(first_number) // int(second_number))
elif operation == '%':
    print(int(first_number) % int(second_number))
