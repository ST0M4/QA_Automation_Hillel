from Lesson_11_12_howework import minus
from Lesson_11_12_howework.level_1.level_2 import root
from Lesson_11_12_howework.level_1.level_2.level_3.level_4.arithmetics import multiplication
import datetime


# Task 1 (Test Check)
print(minus(10, 2))
print(root(16))
print(multiplication(7, 7))

# Task 2


def divide():
    try:
        x = 1
        y = 0
        assert y != 0
        print(x / y)
    except AssertionError:
        print("AssertionError")


print(divide())


# Task 3


def desired_date():
    print(f'Введіть дату з якою хочете працювати')
    # date and time
    year = int(input('Введіть рік(xxxx): '))
    month = int(input('Введіть місяць(xx): '))
    day = int(input('Введіть день(1-31): '))
    hours = int(input('Введіть години: '))
    minutes = int(input('Введіть хвилини: '))
    seconds = 00
    dt = datetime.datetime(year, month, day, hours, minutes, seconds)
    return dt


def defining_operand():
    result = input('Вкажіть True або False (True, щоб додати дні,False, щоб відняти): ')
    return result


def days():
    day_count = int(input('Вкажіть кількість днів: '))
    return day_count


def date_calculation(date, days_count, operand):
    delta = datetime.timedelta(days_count)
    if operand == True:
        new_date = date + delta
    else:
        new_date = date - delta
    return print(new_date)


date_calculation(date=desired_date(), operand=defining_operand(), days_count=days())


# Task 4
def age_calculator(day, month, year):
    current_date = datetime.datetime.now()
    birth_date = datetime.datetime(year, month, day)
    age = (current_date - birth_date).days
    age_timestamp = datetime.datetime.timestamp(current_date) - datetime.datetime.timestamp(birth_date)
    return age, age_timestamp


my_age, my_timestamp = age_calculator(day=17, month=4, year=1993)
print(f"I'm {my_age} days old\nAnd the timestamp of my birthday is {my_timestamp}")
