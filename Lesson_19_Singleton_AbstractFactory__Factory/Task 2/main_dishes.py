from menu_class_description import MainDishes


class Pizza(MainDishes):
    name = "Pizza Barbecue"

    def __init__(self):
        super().__init__()
        self.weight = 430
        self.calories = 870
        self.vegan = False
        self.price = 210


class Ribs(MainDishes):
    name = "Ribs"

    def __init__(self):
        super().__init__()
        self.weight = 300
        self.calories = 450
        self.vegan = False
        self.price = 250


class Spaghetti(MainDishes):
    name = "Spaghetti"

    def __init__(self):
        super().__init__()
        self.weight = 170
        self.calories = 350
        self.vegan = False
        self.price = 180


class Tofu(MainDishes):
    name = "Tofu"

    def __init__(self):
        super().__init__()
        self.weight = 150
        self.calories = 180
        self.vegan = True
        self.price = 155
