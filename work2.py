"""
dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
for key, value in dict1.items():
    result = ""
    if value % 3 == 0:
       result += "hi"
    if value % 5 == 0:
       result += "bye"
    print(f"{key} = {result}")


text = '''
В 1960-е годы в СССР начались попытки запускать аппараты к Венере в рамках космической программы «Венера».
Первый пуск был неудачными, но уже второй аппарат Венера-1 достиг зоны действия тяготения планеты,
где с ним было потеряна связь — он пролетел на расстоянии 100 000 км от поверхности.
В 1965 году результат был уже лучше — 24 000 км.
Венера-4 доставила спускаемый аппарат и смогла получить данные о давлении,
что использовали при построении следующих аппаратов.
Венера-7 впервые совершила мягкую посадку на другую планету — в 1970-м году.
'=А Венера-9 в 1975 году впервые передала телевизионную панораму с Венеры на Землю.
'''
words = text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
most_common_word = max(word_counts, key=word_counts.get)
logest_word = max(words, key=len)
print("часто встречаются:", most_common_word)
print("самое длиное  слов:", logest_word)

my_friends = {
 "Joomart": "+996555246810",
 "Adinai": "+996555013579",
 "Ermek": "+996777013579",
 "Atai": "+996777246810",
 "Aslan": "+996999246810",
 }

his_her_friends = {
 "Lyazat": "+996551123456",
 "Salavat": "+996552234567",
 "Daniyar": "+996553345678",
 "Bolot": "+996554456789",
 "Alymbek": "+996555501234",
 "Dastan": "+996556678912",
 "Maksat": "+996557789012",
 "Aibek": "+996558890123",
 }
our_friends = {}
our_friends.update(my_friends)
our_friends.update(his_her_friends)
print(our_friends)
"
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
megre = months_a.update(months_b)
print(months_a)
months_a.update(['Dec'])
print(months_a)
for month in months_a:
    print(month)
x = {1, 2, 3} 
y = {4, 3, 6}
intersection = x.intersection(y)
print(intersection)
"""

list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
elemets = [element for element in list_1 if element in list_2]
print(elemets)
