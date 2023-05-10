from menu_class_description import Drinks


class VarvarDraft(Drinks):
    name = 'VarvarDraft'

    def __init__(self):
        super().__init__()
        self.volume = 500
        self.alcohol = True
        self.price = 85


class Cava(Drinks):
    name = 'Cava'

    def __init__(self):
        super().__init__()
        self.volume = 400
        self.alcohol = True
        self.price = 10


class Coffee(Drinks):
    name = 'Coffee'

    def __init__(self):
        super().__init__()
        self.volume = 50
        self.alcohol = False
        self.price = 60


class Whiskey(Drinks):
    name = 'Whiskey'

    def __init__(self):
        super().__init__()
        self.volume = 120
        self.alcohol = True
        self.price = 180


class Juice(Drinks):
    name = 'Juice'

    def __init__(self):
        super().__init__()
        self.volume = 400
        self.alcohol = False
        self.price = 110
