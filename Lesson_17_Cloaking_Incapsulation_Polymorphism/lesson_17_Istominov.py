from abc import ABC, abstractmethod


class Galleries(ABC):
    def __init__(self):
        self.name = None
        self.num_of_rooms = 0
        self.num_of_paintings = 0

    @abstractmethod
    def museum_greeting(self):
        pass


class DuLouvre(Galleries):
    def __init__(self):
        super().__init__()
        self.name = 'Du Louvre'
        self.num_of_rooms = 10
        self.num_of_paintings = 200

    def museum_greeting(self):
        print('Welcome to the most famous museum in the world - Louvre')


class VaticanMuseums(Galleries):
    def __init__(self):
        super().__init__()
        self.name = 'Du Louvre'
        self.num_of_rooms = 10
        self.num_of_paintings = 200
        self.__visitors = 0

    def visitors(self):
        self.__visitor_message()
        self.__add_visitors()
        return self.__visitors

    def __add_visitors(self):
        self.__visitors += 10
        return print(self.__visitors)

    def __visitor_message(self):
        print('This message appears everytime 10 new visitors enter')

    def museum_greeting(self):
        print('Welcome to Vatican museum')


class Paintings(DuLouvre):
    def __init__(self):
        super().__init__()
        self.__painting_author = None
        self.__painting_name = None
        self._painting_price = 0

    def painting_details(self, author, painting_name):
        self.__painting_author = author
        self.__painting_name = painting_name
        return print(f'The author of {self.__painting_name} is {self.__painting_author}')

    @property
    def painting_price(self):
        if self._painting_price != 0:
            return self._painting_price
        else:
            return 'No price yet was established'

    @painting_price.setter
    def painting_price(self, price):
        self._painting_price = price


museum_1 = DuLouvre()
museum_2 = VaticanMuseums()
museum_2.visitors()
museum_2.museum_greeting()
museum_1.museum_greeting()
museum_2.visitors()
painting_uno = Paintings()
painting_uno.painting_details('Vincent Van Gogh', 'Wheat Field with Crows')
print(painting_uno.painting_price)
painting_uno.painting_price = 10000
print(f'The new price of the painting is {painting_uno.painting_price}$')
