from abc import ABC


class MainDishes(ABC):
    name: str = ''

    def __init__(self):
        self.weight = None
        self.calories = None
        self.vegan = bool
        self.price = 0

    def dish_info(self):
        if self.vegan:
            return f'The dish {self.name} doesnt contain animal products and is good for vegans. The dish weight is ' \
                   f'{self.weight} grams and has {self.calories} calories in it. The price is {self.price} UAH'
        else:
            return f'The dish {self.name} is for those who enjoy eating meat! The dish weight is ' \
                   f'{self.weight} grams and has {self.calories} calories in it.The price is {self.price} UAH'


class Salads(ABC):
    name: str = ''

    def __init__(self):
        self.weight = None
        self.calories = None
        self.price = 0

    def salad_info(self):
        return f'The dish weight is {self.weight} grams and has {self.calories} calories in it. The price is ' \
               f'{self.price} UAH'


class Drinks(ABC):
    name: str = ''

    def __init__(self):
        self.volume = None
        self.alcohol = bool
        self.price = 0

    def drink_info(self):
        if self.alcohol:
            return f'{self.name} contain alcohol in. Do not drive a car if you ready to party. A drink is ' \
                   f'{self.volume} ml. Its price is {self.price} UAH'
        else:
            return f'{self.name} is non alcohol. A drink is {self.volume} ml. Its price is {self.price} UAH'
