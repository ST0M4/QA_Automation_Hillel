# from abc import abstractmethod, ABC
#
#
# class Cars(ABC):
#     def __init__(self):
#         self.brand = None
#         self.car_type = None
#         self.color = None
#         self.wheels = 4
#         self.engine = True
#         self.engine_type = None
#
#     def move(self):
#         print("Moving")
#
#
#     def stop(self):
#         print("Stop")
#
#
#     @abstractmethod
#     def refuel_type(self):
#         pass
#
#
# class Subaru(Cars):
#     def __init__(self):
#         super(Subaru, self).__init__()
#         self.brand = 'Impreza'
#         self.car_type = 'Sedan'
#         self.color = "Black"
#         self.engine_type = "Gas"
#
#
#     def refuel_type(self):
#         print("Gas 95")
#
#
# class Lexus(Cars):
#     def __init__(self):
#         super(Lexus, self).__init__()
#         self.brand = 'Rx 300'
#         self.car_type = 'HatchBack'
#         self.color = "White"
#         self.engine_type = "Diesel"
#     def refuel_type(self):
#         print("Diesel 95")
#
#
# subaru = Subaru()
# print(subaru.car_type)
# subaru.move()
# subaru.refuel_type()

import random

# Decorator prints function name as soon as it is called
# def func_name_print(func):
#     def print_name(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(func.__name__)
#         return result
#     return print_name
#
# # 3 functions to use the decorator on
# @func_name_print
# def add_one(number):
#     return number + 1
#
#
# @func_name_print
# def add_two(number):
#     return number + 2
#
#
# @func_name_print
# def complex_math(number_1, number_2):
#     a = ((number_1 + number_2)**4)/(number_2**number_1)
#     return a
#
# '''
# # call functions to demonstrate the decorator
# add_two(10)
# add_one(1)
# complex_math(1, 1)
# '''
#
#
# print(add_two(2))

# List comprehension task

list_of_integers = [random.randint(1, 10) for i in range(100)]               # List of 100 elements
count_elements = {k: list_of_integers.count(k) for k in list_of_integers}   # dictionary with each element's count

# print(list_of_integers)
print(count_elements)