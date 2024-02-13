"""
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
dates_of_birth.remove(1)
print(dates_of_birth, "remove")
"
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1.intersection_update(farm_2)
# print(farm_1)
farm_1.difference(farm_2)
print(farm_1)
""
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_1.add("cow")
print(farm_1)
farm_1.pop()
print(farm_1)
"
menu = {'lagman': 120, 'plov': 150, 'borsh': 90}
menu['besh_barmak'] = 130
menu['lagman'] = 135
menu.pop('borsh', None)
menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
print(menu)

user_credentials = {}
for i in range(3):
    user = input("name")
    password = input("password")
    user_credentials[user] = password
print("записаны даные:", user_credentials)

set_methods_set = {'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'}

dict_methods_set = {'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'}


common_methods = set_methods_set.intersection(dict_methods_set)

print("Common methods:", common_methods)
""
people_professions = {
    'wak': 'wak',
    'ivan':'e-sportsman',
    'nurlan': 'barista ',
    'toktosym': 'doter ',
    'bakyt': 'programmer '
}


for name, profession in people_professions.items():
    print(f"Здравствуйте {name}! Прекрасная профессия - {profession}.")

user_number = set()
for i in range(10):
    number = int(input("ведите число"))
    user_number.add(number)
frozen_user = tuple(user_number)
print("frozen number:", frozen_user)
"
outh_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
countries = list(set(outh_american_countries))
print("исходный список:", outh_american_countries)
print("без повтора:", countries)
"
suitcase = [] 
for i in range(5):
    item = input("добавить вещь")
    suitcase.append(item)
print("до удаление:", suitcase)
if suitcase:
    suitcase.pop()
print("после удаление последниего прелмета:", suitcase)

"""

farm_4 = {"dog", "cat", "mouse", "sheep"}
farm_5 = {"cow", "horse", "donkey", "cat", "dog"}


common_animals = farm_4.intersection(farm_5)

print("Общие животные на фермах:", common_animals)
animals_only_in_farm_5 = farm_5.difference(farm_4)

print("Животные, которые есть только на второй ферме:", animals_only_in_farm_5)
