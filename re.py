numbers = (1,2,3,4,5,6)
print(numbers[3:5])

lol = [1,'hello',True,3.14,(1,2,3)]
print(lol)

names = [ 'bakyt', 'nurlan', 'tocto', 'nek']
n = " ".join(names)
print(n)

a = [1,2,3,4]
b = [5,6,7,8,9]
a.extend(b)
print(a)


names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
a = names.count('jack')
print(a)
names.append('oskar')
print(names)
if 'oskar' in names:
     names.remove('oskar')
print(names)

list = []
list.append('nikita')
list.append('2004')
list.append('python')
print(list)

pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
i_loop = pythonList.index("loop")
pythonList.pop(i_loop)
print(pythonList)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
product_resulit = a[0] * a[1] * a[2] * a[3] * a[4] * a[5] * a[6] * a[7] * a[8] * a[9] * a[10]
print(product_resulit)


numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
print(numbers[1:3])


a = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
numbers = []
b = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
letters = []
for i in a:
    if str(i).isdigit():
        numbers.append(int(i))
print(numbers)
for y in b:
    if str(y).isalpha():
        letters.append(y)
print(letters)
