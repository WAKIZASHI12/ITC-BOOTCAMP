

class factory:
    def engine(self):
        return "Двигатель создан"
    
    def bridge(self):
        return "Ходовая часть создана"
    
class toyota(factory):
    def wheels(self):
        return "Колёса готовы"
    
    def windows(self):
        return "Стёкла готовы"


toyota_instance = toyota()
result_list = []

result_list.append(toyota_instance.engine())
result_list.append(toyota_instance.bridge())
result_list.append(toyota_instance.wheels())
result_list.append(toyota_instance.windows())
print(result_list)




class Zoo:
    def __init__(self):
        self.animal_1 = "Тигр"
        self.animal_2 = "Бегемот"
        self.animal_3 = "Жираф"
        self.animal_4 = []
zoo = Zoo()
zoo.animal_1 = "Лев"
zoo.animal_4 = [zoo.animal_2,zoo.animal_3]
zoo.animal_3 = "Змея"

print(zoo.animal_1)
print(zoo.animal_2)
print(zoo.animal_3)
print(zoo.animal_4)