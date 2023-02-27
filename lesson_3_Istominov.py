import random


# Task 1

min = random.randint(0, 60)
if min >= 0 and min <= 14:
    print(min)
    print("First quarter")
elif min >= 15 and min <= 30:
    print(min)
    print("Second quarter")
elif min >=31 and min <= 45:
    print(min)
    print("Third quarter")
else:
    print(min)
    print("Fourth quarter")


# Task 2

while True:
    try:
        birth_month = int(input("Enter number of your month of birth: "))
        break
    except ValueError:
        print("Please enter a number.")

if birth_month == 1 or birth_month == 2 or birth_month == 12:
    print("Зима - За вікном падав сніг.")
elif birth_month == 3 or birth_month == 4 or birth_month == 5:
    print("Весна - Все довкола розцвітало.")
elif birth_month == 6 or birth_month == 7 or birth_month == 8:
    print("Літо - Діти насолоджувались літніми канікулами.")
elif birth_month == 9 or birth_month == 10 or birth_month == 11:
    print("Осінь - Все довкола загоралось яскравими фарбами.")
else:
    print("Введіть число у діапазоні від 1 до 12")

# Task 3

number = random.randint(1, 999)
list_digits = list(map(int, str(number))) # x = [int(a) for a in str(number)]
sum_digits = sum(list_digits)
if (sum_digits % 3 == 0) and (list_digits[-1] % 2 == 0):
    print(f'Число {number} ділиться на 6')
else:
    print(f'Число {number} не ділиться на 6')

# Task 4

print("Введіть точки координат осей x, y")
while True:
    try:
        x = float(input("x = "))
        y = float(input("y = "))
        break
    except ValueError:
        print("Введіть число.")
if x > 0 and y > 0:
    print("Координати знаходяться у першій чверті")
elif x < 0 and y > 0:
    print("Координати знаходяться у другій чверті")
elif x < 0 and y < 0:
    print("Координати знаходяться у третій чверті")
elif x > 0 and y < 0:
    print("Координати знаходяться у четвертій чверті")
elif x == 0 and y > 0 or y < 0:
    print("Координати знаходяться на осі Y")
elif x > 0 or x < 0 and y == 0:
    print("Координати знаходяться на осі X")
else:
    print("Координати знаходяться в нульовій точці системи координат")
