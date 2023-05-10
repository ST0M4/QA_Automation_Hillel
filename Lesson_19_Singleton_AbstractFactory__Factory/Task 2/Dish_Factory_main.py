from main_dishes import Pizza, Spaghetti, Tofu, Ribs
from Salads import Caezar, CrabSticks, Olivie
from Drinks import Cava, Coffee, Juice, VarvarDraft, Whiskey


# Task 2
class OrderPart:
    def __init__(self, table_num: int):
        self.table_num = table_num

    def order_main_dish(self, name: str):
        if name == 'Pizza':
            return Pizza()
        elif name == 'Spaghetti':
            return Spaghetti()
        elif name == 'Tofu':
            return Tofu()
        elif name == 'Ribs':
            return Ribs()
        else:
            print(f'No such dish in the menu')

    def order_salad(self, name: str):
        if name == 'Caezar':
            return Caezar()
        elif name == 'Crab Sticks':
            return CrabSticks()
        elif name == 'Olivie':
            return Olivie()
        else:
            print(f'No such dish in the menu')

    def order_drinks(self, name: str):
        if name == 'Cava':
            return Cava()
        elif name == 'Coffee':
            return Coffee()
        elif name == 'Juice':
            return Juice()
        elif name == 'VarvarDraft':
            return VarvarDraft()
        elif name == 'Whiskey':
            return Whiskey()
        else:
            print(f'No such drink in the menu')


order_1 = OrderPart(1)
print(f'Table # {order_1.table_num}')
main_dish_1 = order_1.order_main_dish('Ribs')
salad_1 = order_1.order_salad('Caezar')
drink_1 = order_1.order_drinks('Coffee')
total_price = main_dish_1.price + drink_1.price + salad_1.price
print(f'Table {order_1.table_num} ordered {main_dish_1.name}, {salad_1.name}, {drink_1.name}. Bill: {total_price}UAH.')
print(main_dish_1.dish_info())
print(salad_1.salad_info())
print(drink_1.drink_info())
print()
order_2 = OrderPart(13)
print(f'Table # {order_2.table_num}')
main_dish_2 = order_2.order_main_dish('Tofu')
salad_2 = order_2.order_salad('Crab Sticks')
drink_2 = order_2.order_drinks('Whiskey')
total_price1 = main_dish_2.price + drink_2.price + salad_2.price
print(f'Table {order_2.table_num} ordered {main_dish_2.name}, {salad_2.name}, {drink_2.name}. Bill: {total_price1}UAH.')
print(main_dish_1.dish_info())
print(salad_1.salad_info())
print(drink_1.drink_info())
