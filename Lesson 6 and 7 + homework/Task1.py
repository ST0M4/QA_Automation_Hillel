import math


# Task 1
# Просимо юзера ввести значення сторін фігури
def enter_side(side_name):
    try:
        side = float(input(f'Введи довжину сторони {side_name}: '))
        if side < 0:
            raise ValueError
    except ValueError:
        print(f'Довжина сторони {side_name} має бути числом та бути більшим за 0.0. Введіть значення ще раз!\n')
        return enter_side(side_name)
    return side


# Визначаємо чи фігура прямокутник за теоремою Піфагора
def rectangle_check(ab, bc, cd, da) -> bool:
    diagonal_1 = math.sqrt(ab**2 + bc**2)
    diagonal_2 = math.sqrt(cd**2 + da**2)
    if diagonal_1 == diagonal_2 and AB != BC and CD != DA:
        print("Це прямокутник!")
        return True
    return False


# Перевіряємо чи наш чотирикутник це квадрат
def square_check(ab, bc, cd, da) -> bool:
    if ab == bc == cd == da:
        return True
    return False


# Рахуємо площу нашого прямокутника
def square_rectangle(ab, bc) -> float:
    return ab * bc


#  Юзер вводить значення 4 сторін
AB = enter_side('AB')
BC = enter_side('BC')
CD = enter_side('CD')
DA = enter_side('DA')

# Повідомляємо нашого юзера що наша фігура це прямокутник
if rectangle_check(AB, BC, CD, DA):
    print(f'Площа прямокутника = {square_rectangle(AB, BC)}')
# Повідомляємо юзера що фігура квадрат
elif square_check(AB, BC, CD, DA):
    print("Фігура квадрат")
else:
    print('Фігура не прямокутник')
