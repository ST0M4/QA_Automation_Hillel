from menu_class_description import Salads


class Caezar(Salads):
    name = 'Caezar'

    def __init__(self):
        super().__init__()
        self.weight = 120
        self.calories = 120
        self.price = 120


class Olivie(Salads):
    name = 'Olivie'

    def __init__(self):
        super().__init__()
        self.weight = 80
        self.calories = 150
        self.price = 90


class CrabSticks(Salads):
    name = 'Crab Sticks'

    def __init__(self):
        super().__init__()
        self.weight = 135
        self.calories = 150
        self.price = 75
