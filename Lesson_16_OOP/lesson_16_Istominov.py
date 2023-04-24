from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self):
        self.type_of_transport = None
        self.brand = None
        self.wheels = None
        self.engine = True

    @abstractmethod
    def passenger_seats(self, num):
        pass

    @abstractmethod
    def engine_type(self, typo):
        pass


class Cars(Transport):
    def __init__(self):
        super(Cars, self).__init__()
        self.type_of_transport = 'Ground'
        self.brand = None
        self.wheels = 4
        self.engine = True

    def passenger_seats(self, num):
        if num <= 5:
            return 'This is not a bus'
        elif num <= 10:
            return 'This is a bus'
        else:
            return 'Not valid number'

    def engine_type(self, typo):
        if typo == 'Electro':
            c = 'Electro car'
            return c
        else:
            c = 'Gasoline or Diesel car'
            return c


class Motorcycles(Transport):
    def __init__(self):
        super(Motorcycles, self).__init__()
        self.type_of_transport = 'Ground'
        self.brand = None
        self.wheels = 2
        self.engine = True
        self.passenger_limit = 2
        self.power = None

    def passenger_seats(self, num):
        pass

    def engine_type(self, typo):
        if typo == 'Electro':
            c = 'Electro motorcycle'
            return c
        else:
            c = 'Gasoline motorcycle'
            return c


class Yamaha(Motorcycles):
    def __init__(self):
        super(Yamaha, self).__init__()
        self.brand = 'Yamaha'
        self.power = 500

    def sound(self):
        print('Vroom Vroom')


motorcycle = Yamaha()
print(motorcycle.brand)
print(motorcycle.engine_type('Gas'))
car_01 = Cars()
print(car_01.passenger_seats(6))
motorcycle.sound()
