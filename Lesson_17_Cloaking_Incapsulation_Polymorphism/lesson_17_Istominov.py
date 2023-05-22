from abc import ABC, abstractmethod


class Galleries(ABC):
    def __init__(self):
        self.name = None
        self.num_of_rooms = 0
        self.num_of_paintings = 0

    @abstractmethod
    def museum_greeting(self):
        pass


# class SpanishGallery(Galleries):
#     def __init__(self, country: str, paintings: int):
#         super().__init__()
#         self.country = country
#         self.paintings = paintings
#         self.greeting = None
#         self.num_of_rooms = 0
#         self.price = 0
#
#     def add_num_of_paintings(self, new_ammount: int):
#         self.paintings = self.paintings + new_ammount
#         return self.paintings
#
#     def minus_num_of_paintings(self, new_ammount: int):
#         self.paintings = self.paintings - new_ammount
#         return self.paintings
#
#     def num_of_rooms(self):
#         if self.paintings < 50:
#             self.num_of_rooms = 5
#         elif self.paintings < 100:
#             self.num_of_rooms = 8
#         elif self.paintings < 150:
#             self.num_of_rooms = 15
#         else:
#             print('NO ROOMS ANYMORE!')
#         return self.num_of_rooms
#
#     def museum_greeting(self):
#         self.greeting = 'Welcome to Spanish Gallery!'
#         return self.greeting
#
#
# exhibition = SpanishGallery('Spain', 78)
# price = exhibition.price
# print(price)

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

    @property
    def get_visitors(self):
        return self.__visitors

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


class Painting(DuLouvre):
    def __init__(self, author, painting_name: str, price: int):
        super().__init__()
        self.__painting_author = author
        self.__painting_name = painting_name
        self._painting_price = price

    def painting_details(self, author: str, painting_name: str):
        self.__painting_author = author
        self.__painting_name = painting_name
        return print(f'The author of {self.__painting_name} is {self.__painting_author}')

    @property
    def painting_author(self):
        return self.__painting_author

    @property
    def painting_name(self):
        return self.__painting_name

    @property
    def painting_price(self):
        if self._painting_price != 0:
            return self._painting_price
        else:
            return 'No price yet was established'

    @painting_price.setter
    def painting_price(self, price):
        self._painting_price = price


# museum_1 = DuLouvre()
# museum_2 = VaticanMuseums()
# museum_2.visitors()
# museum_2.museum_greeting()
# museum_1.museum_greeting()
# museum_2.visitors()
# painting_uno = Paintings()
# painting_uno.painting_details('Vincent Van Gogh', 'Wheat Field with Crows')
# print(painting_uno.painting_price)
# painting_uno.painting_price = 10000
# print(f'The new price of the painting is {painting_uno.painting_price}$')
