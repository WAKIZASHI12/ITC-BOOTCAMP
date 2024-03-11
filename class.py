class Laptop:
    def __init__(self, model):
        self.model = model
        self.specs = {}

    def add_processor(self, processor):
        self.specs['Процессор'] = processor

    def add_ram(self, ram):
        self.specs['Оперативная Память'] = ram

    def add_graphics_card(self, graphics_card):
        self.specs['Видео карта'] = graphics_card

    def add_hard_drive(self, hard_drive):
        self.specs['Жёсткий Диск'] = hard_drive

    def add_motherboard(self, motherboard):
        self.specs['Материнская плата'] = motherboard

    def add_screen_size(self, screen_size):
        self.specs['Размер экрана'] = screen_size

    def get_full_specs(self):
        return {'Модель Ноутбука': self.model, 'Характеристики': self.specs}


laptop = Laptop('Acer Nitro 5')
laptop.add_processor('Intel Core i7')
laptop.add_ram('16 ГБ')
laptop.add_graphics_card('NVIDIA GeForce GTX 1650')
laptop.add_hard_drive('SSD 512 ГБ')
laptop.add_motherboard('Acer')
laptop.add_screen_size('15.6 дюймов')

print(laptop.get_full_specs())


class Parser:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def get_keys_tuple(self):
        return tuple(self.data_dict.keys())

    def get_values_tuple(self):
        return tuple(self.data_dict.values())

    def get_keys_list(self):
        return list(self.data_dict.keys())

    def get_values_list(self):
        return list(self.data_dict.values())

    def get_keys_set(self):
        return set(self.data_dict.keys())

    def get_values_set(self):
        return set(self.data_dict.values())


classroom_data = {
    'student1': 'Alice',
    'student2': 'Bob',
    'student3': 'Charlie',
    'student4': 'David'
}

my_parser = Parser(classroom_data)

print(my_parser.get_keys_tuple())
print(my_parser.get_values_tuple())
print(my_parser.get_keys_list())
print(my_parser.get_values_list())
print(my_parser.get_keys_set())
print(my_parser.get_values_set())














class HotelDataParser:
    def __init__(self, data):
        self.data = data

    def get_all_hotel_names(self):
        return [hotel['name'] for hotel in self.data]

    def get_names_locations_dict(self):
        names = [hotel['name'] for hotel in self.data]
        locations = [hotel['location'] for hotel in self.data]
        return {'names': names, 'locations': locations}

    def add_status_id_to_markers(self):
        for hotel in self.data:
            for marker in hotel['markers']:
                marker['status_id'] = 1


classroom_data_2 = [
    {
        "name": "Hotel A",
        "location": "City A",
        "markers": [
            {"name": "Marker 1"},
            {"name": "Marker 2"}
        ]
    },
    {
        "name": "Hotel B",
        "location": "City B",
        "markers": [
            {"name": "Marker 3"},
            {"name": "Marker 4"}
        ]
    }
]

hotel_parser = HotelDataParser(classroom_data_2)

print(hotel_parser.get_all_hotel_names())
print(hotel_parser.get_names_locations_dict())

hotel_parser.add_status_id_to_markers()

for hotel in classroom_data_2:
    print(hotel)