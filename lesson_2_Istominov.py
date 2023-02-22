import math


# Exercise 1

first_name = input("What's your name? ")
last_name = input("What's your last name? ")
full_name = first_name + " " + last_name
print(full_name)
print(full_name.lower())
print(full_name.upper())
print(full_name.title())
print((first_name + ' ' + last_name + ' ')*5)
full_name = '\n\t     Andrii Istominov\t  '
print(full_name)
full_name = full_name.strip()
print(full_name)


# Exercise 2

radius = int(input("\nВведіть радіус кола: "))
circle_length = 2 * math.pi * radius
circle_area = math.pi * radius ** 2

if radius >= 0:
    print(f"Довжина кола складає {circle_length} , а площа круга {circle_area} ")
else:
    print("Введіть додатнє число")


# Exercise 3

dollar_buy_rate = 37.2
amount_uah = float(input("\nЯку суму ви хочете поміняти у долари?: "))
exchange_uah_dollar = amount_uah / dollar_buy_rate
exchange_uah_dollar = exchange_uah_dollar.__round__(2)
print("За поточним курсом ви отримаєте: {} $".format(exchange_uah_dollar))
