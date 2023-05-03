class Train:
    def __init__(self, train_number, route):
        self.train_number = train_number
        self.route = route
        self.__train_cars = dict()

    def __len__(self):
        return len(self.__train_cars)

    def __setitem__(self, key, value):
        self.__train_cars[key] = value

    def __getitem__(self, item):
        return self.__train_cars[item]


class TrainCar:
    def __init__(self, train_car_number, train_car_class):
        self.train_car_number = train_car_number
        self.train_car_class = train_car_class
        self.__passengers = dict()

    def __len__(self):
        return len(self.__passengers)

    def __setitem__(self, key, value):
        self.__passengers[key] = {'name': value[0], 'boarding': value[1], 'destination': value[2], 'place': value[3]}

    def __getitem__(self, item):
        return self.__passengers[item]

    def __str__(self):
        for key, value in self.__passengers.items():
            print(f'name: {value["name"]} \ndestination: {value["boarding"]} - {value["destination"]} '
                  f'\nplace: {value["place"]}\n')
        return ''


train_01 = Train(57, 'Kyiv - Lviv')
train_car_01 = TrainCar(7, 'DeLuxe')
train_car_02 = TrainCar(13, 'Plazkart')
train_car_03 = TrainCar(5, 'Kupe')
train_01[1] = train_car_01
train_01[2] = train_car_02
train_01[3] = train_car_03

train_car_01[1] = ('Anastasiia Stepanova', 'Kyiv', 'Lviv', 13)
train_car_01[2] = ('Mariia Osadcha', 'Mykolaiv', 'Lviv', 1)
train_car_01[3] = ('Michail Ivanov', 'Vinnytsia', 'Lviv', 23)

train_car_02[1] = ('Grygorii Shevchenko', 'Ivano Frankivsk', 'Lviv', 15)
train_car_02[2] = ('Dmytro Vyshnia', 'Zhitomir', 'Khmelnitsky', 9)
train_car_02[3] = ('Diana Koshova', 'Kyiv', 'Lviv', 2)

train_car_03[1] = ('Ilya Stus', 'Kyiv', 'Ivano Frankivsk', 7)
train_car_03[2] = ('Olga Ryabenko', 'Lubar', 'Lviv', 6)

print(f'Number of train cars - {len(train_01)}\n')
print(f'Number of passengers in al train cars - {len(train_01[3])}\n')
print(f'Інформація про пасажирів у {train_car_01.train_car_number} вагоні')
print(train_01[1])
print(f'Інформація про пасажирів у {train_car_02.train_car_number} вагоні')
print(train_01[2])
print(f'Інформація про першого пасажира у 3 вагоні')
print(train_01[3][1])





